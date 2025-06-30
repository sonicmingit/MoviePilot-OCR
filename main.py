import base64
import io
import re
import cv2
import numpy as np
from PIL import Image
from fastapi import FastAPI
from pydantic import BaseModel
from paddleocr import PaddleOCR

app = FastAPI()

# 初始化 PaddleOCR，使用中文模型
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

class OCR(BaseModel):
    base64_img: str

@app.get("/")
async def root():
    return {"message": "MoviePilot OCR API"}

@app.post("/captcha/base64")
async def captcha_base64(data: OCR):
    base64_img = clean_base64(data.base64_img)
    try:
        img_b = base64.b64decode(base64_img.encode('utf-8'))
    except Exception as e:
        return {"error": "Base64 解码失败", "detail": str(e)}

    try:
        img = Image.open(io.BytesIO(img_b)).convert("RGB")
    except Exception as e:
        return {"error": "图像解码失败", "detail": str(e)}

    mask_npl = np.array(img, dtype=np.uint8)

    ret, thresh = cv2.threshold(mask_npl, 1, 255, cv2.THRESH_BINARY)

    thresh1 = noise_unsome_pixel(thresh)
    gray_image = around_white(thresh1)

    results = ocr.ocr(gray_image, cls=True)
    try:
        result = ''.join(re.findall(r'[A-Za-z0-9]', results[0][0][1][0]))
    except Exception as e:
        print(str(e))
        result = ''
    return {"result": result}

def clean_base64(b64str: str) -> str:
    """去除 data:image 前缀，清洗字符串，补齐 base64 长度"""
    if b64str.startswith('data:image'):
        b64str = re.sub(r'^data:image\/\w+;base64,', '', b64str)
    b64str = b64str.replace('\n', '').replace('\r', '').replace(' ', '')
    while len(b64str) % 4 != 0:
        b64str += '='
    return b64str

def around_white(img):
    """图像边缘设置为白色"""
    w, h, s = img.shape
    for _w in range(w):
        for _h in range(h):
            if (_w <= 5) or (_h <= 5) or (_w >= w - 5) or (_h >= h - 5):
                img[_w, _h, 0] = 255
                img[_w, _h, 1] = 255
                img[_w, _h, 2] = 255
    return img

def noise_unsome_pixel(img):
    """邻域非同色降噪处理"""
    w, h, s = img.shape
    for _w in range(1, w - 1):
        for _h in range(1, h - 1):
            center_color = img[_w, _h]
            top_color = img[_w, _h + 1]
            bottom_color = img[_w, _h - 1]
            left_color = img[_w - 1, _h]
            right_color = img[_w + 1, _h]

            cnt = 0
            if np.array_equal(top_color, center_color):
                cnt += 1
            if np.array_equal(bottom_color, center_color):
                cnt += 1
            if np.array_equal(left_color, center_color):
                cnt += 1
            if np.array_equal(right_color, center_color):
                cnt += 1

            if cnt < 1:
                img[_w, _h, 0] = 255
                img[_w, _h, 1] = 255
                img[_w, _h, 2] = 255
    return img

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=9899, reload=False)
