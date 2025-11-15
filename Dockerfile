FROM python:3.9.7-slim-buster

# FIX FOR pycairo / meson / pkg-config
RUN apt-get update && apt-get install -y \
    git curl python3-pip ffmpeg \
    pkg-config libcairo2-dev libjpeg-dev zlib1g-dev libfreetype6-dev \
    cmake build-essential

RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/

RUN pip3 install -U -r requirements.txt

CMD ["bash", "start.sh"]
