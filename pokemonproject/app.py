from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow import keras 
from keras.models import load_model
from keras.preprocessing import image 
import numpy as np
import os
import json
app = Flask(__name__)

# Load your trained model
model = load_model('model.keras')

# Load class indices
with open('class_indices.json', 'r') as f:
    class_indices_str = json.load(f)
    class_indices = {int(k): v for k, v in class_indices_str.items()}
# This function inverts the class_indices dictionary to get a mapping from index to class



def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Rescale the image

    preds = model.predict(img_array)
    return preds

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction using the same preprocessing as in the notebook
        img = image.load_img(file_path, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Rescale the image

        preds = model.predict(img_array)
        predicted_class_index = np.argmax(preds, axis=1)[0]
        predicted_probability = np.max(preds)

       
        # Debug prints
        print("Prediction vector:", preds)
        print("Predicted class index:", predicted_class_index)
 
        predicted_class =  class_indices.get(predicted_class_index, "Class index out of range")

        print(f"Predicted class name: {predicted_class}")
        # Pass the result to the template
        return render_template('result.html', pokemon=predicted_class, probability=predicted_probability, image_path=file_path)
    
    
    return None

if __name__ == '__main__':
    app.run(debug=True)
