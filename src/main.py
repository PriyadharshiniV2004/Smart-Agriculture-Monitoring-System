from sensor.dht11_reader import read_dht11
from sensor.soil_moisture import read_soil_moisture
from vision.predict import predict_image
from alerts.sms_alert import send_sms
import cv2
import time

print("🌱 Smart Agriculture Monitoring System Started")

# Read sensors
temperature, humidity = read_dht11()
soil_status = read_soil_moisture()

print(f"Temperature: {temperature} °C")
print(f"Humidity: {humidity} %")
print(f"Soil Moisture: {'Dry' if soil_status == 1 else 'Wet'}")

# Send alerts for soil
if soil_status == 1:
    send_sms("⚠️ Soil is DRY. Irrigation required!")

# Disease detection (sample image)
image_path = "data/sample_images/tomato_leaf.jpg"
image = cv2.imread(image_path)

if image is not None:
    disease, confidence = predict_image(image, model_type="tomato")
    print(f"Disease Detected: {disease} ({confidence}%)")

    if confidence > 80:
        send_sms(f"🍅 Tomato Disease Detected: {disease} ({confidence}%)")

time.sleep(2)
