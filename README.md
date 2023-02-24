# HT_bot for Raspberry Pi 3
To run this application you need a DHT22 Humidity and Temperature sensor, cabled to your Raspberry.

## Depedencies
- Adafruit DHT Library:
- pyTelegramBotAPI

```bash
pip3 install Adafruit_DHT
```

```bash
pip3 install pyTelegramBotAPI
```

## Launching Bot

- Create a Telegram bot and insert the API Token in parameters.py file
- Type in which PIN number is linked the DATA jumper of the DHT22 sensor in parameters.py file

```bash
python3 main.py
```
- send the /status command in the bot chat to receive the sensor informations.

Feel free to improve and propose improvements for this project.
