import dht11
import RPi.GPIO as GPIO
import time
from sensor.gpio_setup import DHT11_PIN

sensor = dht11.DHT11(DHT11_PIN)

def read_dht11():
    for _ in range(10):
        result = sensor.read()
        if result.is_valid():
            return result.temperature, result.humidity
        time.sleep(1)

    return None, None
