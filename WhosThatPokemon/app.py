from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow import keras 
from keras.models import load_model
from keras.preprocessing import image 
import numpy as np
import os
import json
import requests
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
        predicted_class_name = class_indices.get(predicted_class_index, None)
        if predicted_class_name is not None:
            # Fetch the Pokémon data from the PokeAPI
            api_url = f'https://pokeapi.co/api/v2/pokemon/{predicted_class_name.lower()}'
            response = requests.get(api_url)
            if response.status_code == 200:
                pokemon_data = response.json()
                sprite_front = pokemon_data['sprites']['front_default']
                sprite_back = pokemon_data['sprites']['back_default']
                pokemon_cry = f'https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_data["id"]}.ogg'
            else:
                sprite_front = sprite_back = pokemon_cry = None
            print(f"Predicted class name: {predicted_class}")
            # Pass the result to the template
            return render_template('result.html', pokemon=predicted_class, probability=predicted_probability, image_path=file_path, sprite_front=sprite_front, sprite_back=sprite_back, pokemon_cry=pokemon_cry)
        else:
            return render_template('error.html', message="Pokemon class index out of range.")
    
    
    return None

if __name__ == '__main__':
    app.run(debug=True)
