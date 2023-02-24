import Adafruit_DHT as dht
import time
import telebot
import parameters
import sys

# sensor configuration
DHT_SENSOR = dht.DHT22
DHT_PIN = parameters.DHT_DATA_PIN

# Telegram configurations
BOT_TOKEN = parameters.BOT_TOKEN

if BOT_TOKEN == '':
    print('Check bot parameters in parameters.py file!')
    sys.exit(1)

# bot initializer
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["status"])
def get_room_status(command):
    print("Request received.")
    status = read_data_from_sensor()
    bot.send_message(command.from_user.id, f"Temperature: {status[0]} - Humidity: {status[1]}")


# reads values from DHT sensor
def read_data_from_sensor():
    data = []
    humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
    while humidity is None or temperature is None:
        time.sleep(3)
        humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)

    data.append(float("{:.2f}".format(temperature)))
    data.append(str(int(humidity)) + ' %')
    return data


print('*** bot started ***')
# listening for commands
bot.infinity_polling(timeout = 90)
