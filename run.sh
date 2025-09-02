docker build -t xwatchdog .
docker run -d --restart unless-stopped xwatchdog