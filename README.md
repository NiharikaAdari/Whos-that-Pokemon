# Pokémon Image Classifier



## Project Overview
This project is a web-based application designed to classify images of Pokémon using a machine learning model and dynamically generate silhouettes of the uploaded images. It serves as an interactive tool for Pokémon enthusiasts and showcases the integration of machine learning models in web applications for image recognition and manipulation.

<img width="1263" alt="image" src="https://github.com/NiharikaAdari/Whos-that-Pokemon/assets/130190699/b81719c4-641c-4268-8cb2-4587981e2e83">
<img width="1251" alt="image" src="https://github.com/NiharikaAdari/Whos-that-Pokemon/assets/130190699/05f0e712-2143-4051-a95d-a58d3b55ecb9">
<img width="1253" alt="image" src="https://github.com/NiharikaAdari/Whos-that-Pokemon/assets/130190699/51022b79-6786-4aa0-9080-d4bb1675fc27">







![showcase](https://github.com/NiharikaAdari/Whos-that-Pokemon/assets/130190699/a75f3353-1551-49c1-9da6-3f7fb9d851db)

## Features
- **Image Classification:** Utilizes a Convolutional Neural Network (CNN) to classify Generation 1 Pokémon images, identifying the Pokémon's name from an uploaded image.
- **Silhouette Generation:** Transforms uploaded images into black silhouettes, offering users a fun way to guess the Pokémon before seeing the classification results.
- **Interactive Web Interface:** A user-friendly web interface that allows users to upload images, view silhouettes, and receive instant classification results.
- **Play Sound!** hear the classic, "Who's that Pokemon?" from the show!
  
## Technologies Used
- **TensorFlow & Keras:** For designing, training, and deploying the CNN model.
- **Flask:** A lightweight WSGI web application framework used to serve the model and handle web requests.
- **HTML/CSS/JavaScript:** For building the interactive front-end.
- **Jupyter Notebook**
  
## How It Works
- **Model Training:** The CNN model is trained on a dataset containing images of all Generation 1 Pokémon, with each class representing a different Pokémon. The model learns to recognize various features and characteristics unique to each Pokémon.

- **Web Application:** The Flask backend serves the trained model and handles image uploads from users. Upon uploading an image, the application processes the image, making it ready for classification.

- **Image Classification:** The processed image is fed into the trained model, which predicts the Pokémon's name based on learned features.

- **Silhouette Generation:** For uploaded images, a JavaScript function converts the image into a black silhouette, displaying it to the user for a fun guessing game before revealing the classification results.

- **Result Display:** The application displays the original image, its silhouette, and the classification result (Pokémon's name) alongside the model's confidence level.

## Project Structure
- app.py: Flask application file containing route definitions and model loading.
- model/: Directory containing the trained TensorFlow/Keras model.
- static/: Contains static files like CSS, JavaScript, and images used in the web interface.
- templates/: HTML files for the web interface.
- model.ipynb: CNN model 
