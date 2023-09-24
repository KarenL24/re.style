import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys
print(sys.executable)
import sys
sys.path.append('path/to/tensorflow')

# storing the dataset path
clothing_fashion_mnist = tf.keras.datasets.fashion_mnist
 
# loading the dataset from tensorflow
(x_train, y_train),(x_test, y_test) = clothing_fashion_mnist.load_data()
 
# displaying the shapes of training and testing dataset
print('Shape of training cloth images: ', x_train.shape)
 
print('Shape of training label: ', y_train.shape)
 
print('Shape of test cloth images: ', x_test.shape)
 
print('Shape of test labels: ', y_test.shape)