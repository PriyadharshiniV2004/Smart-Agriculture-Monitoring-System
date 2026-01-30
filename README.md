# 🌱 Smart Agriculture Monitoring System using IoT & Deep Learning

A **real-time intelligent agriculture monitoring system** that integrates **IoT sensors, Raspberry Pi, and Convolutional Neural Networks (CNNs)** to monitor environmental conditions and automatically detect **plant leaf diseases and pest infestations**, with **instant SMS alerts** to farmers.

This repository accompanies our **peer-reviewed research paper published in the IJERT journal**.

---

## 📌 Publication

📰 **Journal**: International Journal of Engineering Research & Technology (IJERT)  
📄 **Paper Title**: Smart Agriculture Monitoring System  
🔗 **Paper Link**:  
👉 **[Click here to view the published IJERT paper](https://www.ijert.org/smart-agriculture-monitoring-system)**

> The research presented in this repository is fully aligned with the methodology, experiments, and results reported in the IJERT publication.

---

## 🚜 Problem Statement

Traditional agricultural monitoring methods rely heavily on **manual inspection** and **experience-based decision making**, which are:
- Time-consuming
- Error-prone
- Inefficient for large-scale farming

Early detection of **plant diseases, pest attacks, and adverse soil conditions** is critical to improving crop yield, reducing pesticide usage, and ensuring sustainable agriculture.

---

## 🎯 Project Objectives

- Monitor **temperature, humidity, and soil moisture** in real time  
- Detect **plant leaf diseases** using CNN-based image classification  
- Identify **pest infestations** from images  
- Deploy models on **Raspberry Pi (edge device)**  
- Send **real-time SMS alerts** using Twilio  
- Reduce manual labor and improve decision-making for farmers  

---

## 🧠 System Overview

The system consists of three major components:

1. **IoT Sensor Module**
   - DHT11 sensor for temperature & humidity
   - Resistive soil moisture sensor

2. **Image Processing & Deep Learning Module**
   - CNN-based disease and pest classification
   - Trained on Kaggle plant disease and pest datasets
   - Achieved ~96–98% accuracy

3. **Communication Module**
   - Twilio SMS API for instant farmer alerts

All processing is handled on a **Raspberry Pi 4B**, enabling real-time edge intelligence.

---

## 🏗️ System Architecture

`Sensors → Raspberry Pi → Image Processing (CNN) → Decision Logic → SMS Alerts`


The Raspberry Pi acts as the central processing unit, continuously acquiring sensor data and processing images to identify anomalies.

---

## 🛠 Hardware Components

| Component | Description |
|---------|-------------|
| Raspberry Pi 4B | Central processing unit |
| DHT11 Sensor | Temperature & humidity measurement |
| Soil Moisture Sensor | Soil water content detection |
| Camera Module / USB Camera | Leaf & pest image capture |

---

## 💻 Software Stack

- Python 3
- TensorFlow & Keras
- OpenCV
- NumPy
- RPi.GPIO
- Twilio API
- DHT11 Library


---

## 🧪 Deep Learning Models

The following architectures were analyzed and compared:

- VGG-16
- ResNet-50
- Inception
- AlexNet
- **Proposed Optimized CNN Model**

### 📊 Performance Summary

| Model | Test Accuracy |
|------|---------------|
| VGG-16 | 82.75% |
| AlexNet | 90.68% |
| ResNet-50 | 98.73% |
| Inception | 99.98% |
| **Proposed CNN** | **96–98%** |

The proposed CNN achieves **high accuracy with lower computational complexity**, making it suitable for **edge deployment on Raspberry Pi**.

---

## 📸 Image Preprocessing

To enhance model robustness:
- HSV color-space conversion
- Leaf segmentation
- Noise reduction
- Normalization
- Data augmentation (rotation, flip, zoom, contrast)

These steps significantly improve generalization under real-world conditions.

---

## 📲 SMS Alert System

The system automatically sends SMS alerts when:
- Soil moisture is low (irrigation required)
- Extreme temperature or humidity is detected
- A plant disease or pest infestation is identified

Alerts are delivered using the **Twilio API**, enabling instant farmer response.

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

`pip install -r requirements.txt`

### 2️⃣ Configure Twilio Credentials

Edit:

`src/utils/config.py`

### 3️⃣ Run the System

`python src/main.py`

---
## 📄 Research Validation

This implementation is experimentally validated and corresponds directly to the methodology, datasets, results, and conclusions presented in the IJERT journal paper.

All accuracy plots, confusion matrices, and experimental results are included in the docs/ folder.

---

## Authors

  - Praveen Kumar G
  - Kalaiarasan T
  - Divya A
  - Priyadharshini V

---

## 🔮 Future Scope

  - Real-time camera-based continuous monitoring
  - Drone-based field inspection
  - Predictive disease outbreak analysis
  - Integration with mobile applications
  - AI-driven irrigation and pesticide control

---

## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this work with proper citation.

---
## ⭐ Citation

If you use this work in your research, please cite our IJERT paper.

Author(s), "Smart Agriculture Monitoring System", 
International Journal of Engineering Research & Technology (IJERT)

