# Telegram_CAM_Bot

Telegram bot for ESP-Cam module. 

## Architecture


## Build Image TG-Bot
```BASH
git clone https://github.com/geksogen/Telegram_CAM_Bot.git
cd TG_Bot
sudo docker build -t tg_bot:1 .
sudo docker run --rm -d --name tg_bot --network=host tg_bot:1
```

## To-do
https://medium.com/@tomer.klein/real-time-uptime-monitoring-with-uptime-kuma-and-grafana-16638d6a579f - Monitoring
https://admintuts.net/server-admin/how-to-configure-mosquitto-with-nginx-reverse-proxy/ - MQTT-Nginx-SSL
https://github.com/YamlEngineer/TelePlate/tree/main - Pyrogram to Docker/Docker-compose
