# Image-Recognition-System

An image classification web app that allows users to upload images and receive real-time predictions using a deep learning model.

## 🔍 Description

This project demonstrates the use of deep learning for object recognition. It uses a pre-trained model (trained on ImageNet) to identify objects in uploaded images and provides predictions via a web interface.

## 🚀 Features

- Upload images through a simple web UI
- Real-time object prediction using TensorFlow/Keras
- Supports various object categories from ImageNet
- Built with Python and Flask
- Displays the uploaded image with prediction results

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Flask (Web Framework)
- HTML / CSS
- OpenCV (optional, for image preprocessing)

## 📁 Project Structure

image_classifier_app/
├── app.py # Flask backend
├── model/
│ └── model.h5 # Pre-trained model (ImageNet-based)
├── static/
│ └── uploads/ # Stores uploaded images
├── templates/
│ ├── index.html # Upload page
│ └── result.html # Prediction result page
├── requirements.txt
└── README.md

## ▶️ How to Run

1. **Clone the repo**  
'''bash
git clone https://github.com/yourusername/image-recognition-app.git
cd image-recognition-app

Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Place the model
Make sure your pre-trained model.h5 is placed in the model/ directory.

Run the app

bash
Copy
Edit
python app.py
Open in browser
Go to: http://127.0.0.1:5000/

📌 Output Example
Upload an image of a car, and get:
Prediction: pickup

📚 Acknowledgments

TensorFlow ImageNet models
Flask Web Framework


