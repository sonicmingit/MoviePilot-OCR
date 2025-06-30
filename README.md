# 构建
docker build -t movie-ocr:1.0 . && docker run -d --name movie-ocr:1.0 -p 9899:9899 movie-ocr:1.0



# MoviePilot OCR

MoviePilot使用的验证码OCR识别服务，成功率90%以上。

## 已知问题
- [ ] 对CPU架构有要求，否则无限重启
