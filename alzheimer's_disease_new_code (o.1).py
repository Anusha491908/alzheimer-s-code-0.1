# -*- coding: utf-8 -*-
"""Alzheimer's disease new code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_8o0rdOsqKodz6ewdEj0cCR14b9OW3hw
"""

!pip install cartopy
import  tensorflow as tf

from google.colab import drive

('/content/drive/MyDrive')

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import tensorflow as tf
import random 
import cv2

import keras
from PIL import Image
from random import randint
from keras.layers import GlobalAveragePooling2D, GlobalMaxPooling2D, Reshape, Dense, multiply, Permute, Concatenate, Conv2D, Add, Activation, Lambda
from keras import backend as K
from keras.activations import sigmoid
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
from keras import initializers
from keras.models import Sequential

!python --version

pip install tensorflow

import keras
from keras.utils import to_categorical

print(tf.__version__)
print(keras.__version__)

train_path= "/content/drive/MyDrive/Alzheimer_s Dataset/train"
test_path= "/content/drive/MyDrive/Alzheimer_s Dataset/test"

import tensorflow as tf
from tensorflow import keras
import warnings
from tensorflow.keras import layers

# Load the dataset
train_data = keras.preprocessing.image_dataset_from_directory(
    '/content/drive/MyDrive/Alzheimer_s Dataset/train',
    image_size=(150, 150),
    batch_size=32,
    shuffle=True,
    seed=42,
    validation_split=0.2,
    subset='training'
)

test_data = keras.preprocessing.image_dataset_from_directory(
    '/content/drive/MyDrive/Alzheimer_s Dataset/test',
    image_size=(150, 150),
    batch_size=32,
    shuffle=True,
    seed=42,
    validation_split=0.2,
    subset='validation'
)

pip install matplotlib-venn

import os

from keras.preprocessing.image import ImageDataGenerator

train_batches = ImageDataGenerator(validation_split=0.1) \
                .flow_from_directory('/content/drive/MyDrive/Alzheimer_s Dataset/train',  
                                     classes = ['NonDemented', 'VeryMildDemented', 
                                                'MildDemented', 'ModerateDemented'], 
                                     subset='training',
                                     batch_size=10)

validation_batches = ImageDataGenerator(validation_split=0.1) \
                     .flow_from_directory('/content/drive/MyDrive/Alzheimer_s Dataset/train', 
                                          classes = ['NonDemented', 'VeryMildDemented', 
                                                     'MildDemented', 'ModerateDemented'], 
                                          subset='validation',
                                          batch_size=10)
                
test_batches = ImageDataGenerator() \
                    .flow_from_directory('/content/drive/MyDrive/Alzheimer_s Dataset/test', 
                                         classes = ['NonDemented', 'VeryMildDemented', 
                                                    'MildDemented', 'ModerateDemented'], 
                                         batch_size=10, 
                                         shuffle=False)

import os

pip install datasets

data = {'NonDemented':      0, 
        'VeryMildDemented': 0, 
        'MildDemented':     0,
        'ModerateDemented': 0}
import os
for cls in os.listdir(train_path):
    for img in os.listdir(train_path + '/' + cls):
        data[cls] = data[cls] + 1

keys = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
plt.bar(keys, values, color=(0.7, 0.2, 0.4, 0.9), width = 0.4)

img_size = 224
num_classes = 4
model = Sequential([
    layers.Input((img_size, img_size, 3)),
    layers.Rescaling(1./255),
    layers.Conv2D(32, 3, activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2),
    layers.Conv2D(64, 3, activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2),
    layers.Conv2D(128, 3, activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2),
    layers.Conv2D(256, 3, activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2),
    layers.Flatten(),
    layers.Dense(300, activation='relu'),
    layers.Dense(150, activation='relu'),
    layers.Dropout(0.25),
    layers.Dense(num_classes, activation='softmax')
])

import keras

metrics = [keras.metrics.CategoricalAccuracy(name='accuracy'),
           keras.metrics.Precision(name='precision'),
           keras.metrics.Recall(name='recall'),
           keras.metrics.AUC(name='auc')]

from tensorflow.keras.models import Model

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os 
import random 
import cv2

from keras.api._v2.keras import models
from keras.models import Model
optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), 
loss='categorical_crossentropy',
list:metrics

epo = 5
b_size = 8

history = Model.fit("/content/drive/MyDrive/Alzheimer_s Dataset/train",
                   validation_split=validation_split,
                    steps_per_epoch=len(train_batches),
                    validation_steps=len(validation_split),
                    epochs=epo,
                    batch_size=b_size, 
                    verbose=2)