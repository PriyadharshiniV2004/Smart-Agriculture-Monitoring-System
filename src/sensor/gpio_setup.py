import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

SOIL_SENSOR_PIN = 4
DHT11_PIN = 27

GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
