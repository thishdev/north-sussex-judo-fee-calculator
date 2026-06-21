FROM debian:bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DISPLAY=:99 \
    HOME=/home/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        fluxbox \
        novnc \
        python3-tk \
        websockify \
        x11vnc \
        xauth \
        xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .
COPY docker/start-container.sh /usr/local/bin/start-container.sh

RUN chmod +x /usr/local/bin/start-container.sh

EXPOSE 5900 6080

CMD ["/usr/local/bin/start-container.sh"]
