FROM python:3.10.11-slim-bullseye
ENV LANG="C.UTF-8" \
    TZ="Asia/Shanghai" \
    REPO_URL="https://github.com/sonicmingit/MoviePilot-OCR.git" \
    WORKDIR="/app"
RUN apt-get update -y \
    && apt-get install -y \
        git \
        ffmpeg \
        libgomp1 \
        libsm6 \
        libxrender1 \
        libxext6 \
        libgl1 \
        libssl1.1 \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf \
        /tmp/* \
        /var/lib/apt/lists/* \
        /var/tmp/*
RUN git clone -b main ${REPO_URL} ${WORKDIR}
WORKDIR ${WORKDIR}
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf \
        /tmp/* \
        /root/.cache \
        /var/tmp/*
EXPOSE 9899
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9899"]
