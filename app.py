from flask import Flask, render_template, request, redirect
import os
import uuid
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions
import numpy as np

app = Flask(__name__)
model = MobileNet(weights='imagenet')

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def model_predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded = decode_predictions(preds, top=1)[0][0]
    label = decoded[1]
    confidence = decoded[2]
    return f"{label} ({confidence * 100:.2f}%)"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect('/')
    file = request.files['image']
    if file.filename == '':
        return redirect('/')
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    label = model_predict(filepath)
    return render_template('result.html', label=label, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
