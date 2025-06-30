# MoviePilot OCR

MoviePilot使用的验证码OCR识别服务，成功率90%以上。

## 已知问题
- [ ] 对CPU架构有要求，否则无限重启

---

# 更新内容


---

````markdown
# MoviePilot-OCR

🎯 基于 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 的验证码识别服务，使用 FastAPI 提供 REST 接口，支持 Base64 图像识别，部署简单，性能优良。

---

## ✨ 功能特性

- ✅ 支持图像验证码识别，提取纯字母数字结果
- ✅ 接口标准，支持 Base64 原始格式或带前缀的格式（`data:image/png;base64,...`）
- ✅ 使用 PaddleOCR 中文识别模型，准确率高
- ✅ 内置图像预处理：边缘置白、邻域降噪
- ✅ 支持 Docker 快速部署

---

## 🚀 在线接口说明

| 方法 | 路径              | 描述                 |
|------|-------------------|----------------------|
| GET  | `/`               | 测试服务是否运行         |
| POST | `/captcha/base64` | 提交 Base64 图像，返回识别结果 |

### 🔖 请求参数（JSON）

```json
{
  "base64_img": "data:image/png;base64,..."
}
````

或：

```json
{
  "base64_img": "iVBORw0KGgoAAA..."
}
```

### 🔖 返回示例

```json
{
  "result": "X7T3C"
}
```

---

## 🐳 Docker 快速部署

### 1️⃣ 构建镜像

```
docker pull sonicming/moviepilot-ocr:latest
```

```bash
docker build -t moviepilot-ocr:latest .
```

### 2️⃣ 运行容器

```bash
docker run -d \
  --name moviepilot-ocr \
  -p 9899:9899 \
  moviepilot-ocr:latest
```

### 3️⃣ 验证接口

```bash
curl http://localhost:9899/
```

---

## 🧱 本地运行（开发调试）

### 依赖环境

* Python 3.10+
* PaddleOCR（已在 `requirements.txt` 中）
* OpenCV、Pillow、Uvicorn 等

### 启动方式

```bash
pip install -r requirements.txt
python main.py
```

访问：[http://localhost:9899/docs](http://localhost:9899/docs) 查看在线 Swagger 文档

---

## 📁 项目结构

```
.
├── Dockerfile
├── main.py                 # 主程序入口
├── requirements.txt        # 依赖包
└── README.md
```

---

## 📄 License

MIT License © 2025 \[Your Name]

---

> 欢迎使用和修改本项目，如有建议或问题欢迎提 Issue！

```

---

### ✅ 使用建议

- 项目命名建议使用 `moviepilot-ocr` 或更具语义的中文拼音（如 `captcha-ocr-api`）
- `README.md` 中可以加入截图、识别样例或模型精度等内容来增强吸引力
- 如果你打算发布 Docker Hub 镜像，也可以附上 `docker pull` 指令

需要我再帮你生成 `requirements.txt`、`.dockerignore` 或 `.gitignore` 文件也可以继续说。
```

