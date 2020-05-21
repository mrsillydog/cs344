# Exploring Variational Autoencoders with fashion_mnist

This project is based around the topic of variational autoencoders, or VAES. VAES are a technology in the field of realistic image autogeneration, and additionally allow us to develop models which are capable of determining which images are similar to one another. I used this technology principally with Keras' fashion_mnist dataset in an effort to improve the example VAE trained on Keras' mnist in Chapter 8.4 of F. Chollet's Deep Learning with Python Notebooks.

This project was built using Keras 2.2.4-tf with Tensorflow running underneath. All code is contained within report.ipynb; it contains a total of five separate VAE examples.

Version 1. F. Chollet's VAE from Chapter 8.4 of Deep Learning with Python Notebooks on the mnist dataset.
Version 2. My VAE on the mnist dataset.
Version 3. F. Chollet's VAE on the fashion_mnist dataset.
Version 4. My VAE on the fashion_mnist dataset.
Version 5. My VAE on the cifar10 dataset.

These are the libraries that must be imported to create the VAE. Keras 2.2.4-tf must be installed within Tensorflow 2 (https://www.tensorflow.org/install) beforehand with access to the NumPy library (https://numpy.org/).

from tensorflow import keras
from tensorflow.keras import backend as K
import tensorflow.keras
from tensorflow.keras import layers
from tensorflow.keras import backend as K
from tensorflow.keras.models import Model
import numpy as np

All datasets imported from here:

from tensorflow.keras.datasets import *

These are the libraries that must be imported to view results of the VAE trained on various datasets. In order to view, matplotlib (https://matplotlib.org/), scipy (https://www.scipy.org/), and pandas (https://pandas.pydata.org/) must be installed.

import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd