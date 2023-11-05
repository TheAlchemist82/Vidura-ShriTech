# emotion-detection-ML
Submission for ShriTech 2023

# Libraries used

## 1. Keras

      Keras is a high-level deep-learning API of the Tensorflow platform for implementing neural networks.
      In the project, we have used a variety of image preprocessing, models, and layer classes to build a Convolutional Neural Network from scratch, with help of internet resources mentioned at the end of the document.

## 2. pandas

      A widely used, flexible and fast data manipulation tool, used as the primary library for handling data in the project.

## 3. numpy

      Standard python library to add functionality of C and Fortran into Python

## 4. os

      Standard Python library to execute system commands through the python shell.

# Dataset

The dataset used is the 'Face expression recognition dataset' from kaggle.com

# Theory

A Convolutional neural network is the best kind of neural network for image processing.
They comprise of 3 main layers

1. **Convolutional Layer**: The convolutional layer is the core building block of a CNN, and it is where the majority of computation occurs. It requires a few components, which are input data, a filter, and a feature map.
2. **Pooling Layer**: Also known as downsampling, conducts dimensionality reduction, reducing the number of parameters in the input
3. **Fully Connected Layer**: The pixel values of the input image are not directly connected to the output layer in partially connected layers. However, in the fully-connected layer, each node in the output layer connects directly to a node in the previous layer.

# face_rec.ipynb
This file is a **jupyter notebook file** that trains our machine learning model. 
It outputs 2 files
- emotiondetector.h5 (binary)
- emotiondetector.json (json)

# realtimedetection_main.py
Uses OpenCV to access the user's webcam and saves the recorded videos in the *./videos* folder with the date and time.

# Specifications
The model has an 80% accuracy and classifies emotion under 7 labels. 
- Neutral
- Happy
- Sad
- Angry
- Fear
- Disgust
- Surprise

# Vidura
To run the main project, run the mainapp.py file

Machine Learning and Facial Recognition done by ***ANGAD BISEN***
GUI and App built by ***JAYANT MITTAL***

# Acknowledgements
The ML model was adapted from https://www.youtube.com/@ProgresswithPython and built of off his existing GitHub repository.
Several online resources like Stackoverflow and Documentation for various libraries were used.
