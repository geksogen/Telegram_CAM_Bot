from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import paho.mqtt.client as mosquitto
import time
from datetime import datetime
import threading

import buttons
import keyboards
from custom_filters import button_filter

import logging
import logging.config



API_ID = 21497875
API_HASH = '7f95a52a1683a9be79d8813da6056a42'
BOT_TOKEN = '6088638632:AAEZAcA6HzQtCoeNnqY0x5ccMfbF5Z0610M'

MQTT_HOST = "fairfoot513.cloud.shiftr.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_LOGIN = "fairfoot513"
MQTT_PASSWORD = "CBPB0ntFBGMo1x2t"
CLIENT_ID = "MQTT-Telegram-Bot"

def on_connect(client, userdata, flags, rc):
    client.subscribe("PICTURE")

def on_message(client, userdata, msg):
    if msg.topic == "PICTURE":
        if msg.payload != b'None':
            with open(f"photo.jpeg", "wb") as file:
                file.write(msg.payload)

def publish(mqttc):
     msg_count = 0
     while msg_count < 1:
         msg = f"image: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
         result = mqttc.publish('SMILE', msg)
         status = result[0]
         if status == 0:
             print(f"Send image `{msg}` to topic `{'SMILE'}`")
         else:
             print(f"Failed to send image to topic {'SMILE'}")
         msg_count += 1

mqttc = mosquitto.Client(client_id=CLIENT_ID)
mqttc.username_pw_set(MQTT_LOGIN, MQTT_PASSWORD)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE)

tr = threading.Thread(target=mqttc.loop_start())
tr.start()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


bot = Client(
 api_id=API_ID,
 api_hash=API_HASH,
 bot_token=BOT_TOKEN,
 name="ESP32-Cam-Bot",
)

# -4161519996    # test
# -1002076082505 # prod
# https://t.me/ESP32CAM_Pic_bot
# https://t.me/raw_data_bot # ID chat

chat_id = -4161519996



@bot.on_message(filters=filters.command('start'))
async def time_command(client: Client, message: Message):
    await message.reply(f"Привет я бот, который умеет показывать фото с твоей камеры.", reply_markup=keyboards.main_keyboard)

@bot.on_message(filters=filters.command("photo") | button_filter(buttons.photo_button))
async def time_command(client: Client, message: Message):
    #mqttc.loop_start()
    # Publish
    publish(mqttc)
    time.sleep(1)
    document = open('photo.jpeg', 'rb')
    await bot.send_document(chat_id, document)
    #os.remove("images/photo.jpeg")

bot.start()
