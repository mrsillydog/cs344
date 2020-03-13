###############################
# lab06_3.py prints out some basic data about the boston_housing price dataset from keras
#
# Written by for CS344 at Calvin University
#
# @author isa3
# @version 13march2020
###############################

#PYTHONPATH = /usr/local/lib/python3.6/dist-packages/

import numpy as np
from tensorflow.python.keras.datasets import boston_housing

#a.
(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()


def print_structures():
    #i. training
    print(
        'training images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
                len(train_images), 
                train_images.ndim, 
                train_images.shape, 
                train_images.dtype
        ),
        'testing images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
                len(test_labels), 
                train_labels.ndim, 
                test_labels.shape, 
                test_labels.dtype
        )
    )
print_structures()

'''
results: 
i. 404 training images, 102 testing images
ii. 2 dimensions, (404,13) shape, float64 data type for training
    1 dimension, (102,) shape, float64 data type for testing
'''