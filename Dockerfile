FROM python:3.10-slim-bullseye

# avoid interactive
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git curl python3-pip ffmpeg \
    pkg-config libcairo2-dev libjpeg-dev zlib1g-dev libfreetype6-dev \
    cmake build-essential build-essential libpangocairo-1.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["bash", "start.sh"]
