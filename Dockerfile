FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    git curl ffmpeg \
    pkg-config libcairo2-dev libjpeg-dev zlib1g-dev libfreetype6-dev \
    cmake build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install -U pip

# Copy project
COPY . /app/
WORKDIR /app/

# Install Python libs
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
