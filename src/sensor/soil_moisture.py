import RPi.GPIO as GPIO
from sensor.gpio_setup import SOIL_SENSOR_PIN

def read_soil_moisture():
    """
    Returns:
    1 -> Dry soil
    0 -> Wet soil
    """
    return GPIO.input(SOIL_SENSOR_PIN)
