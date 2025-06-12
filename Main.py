import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Shape of x_train:", x_train.shape) # (60000, 28, 28)
print("Shape of y_train:", y_train.shape) # (60000,)
print("Shape of x_test:", x_test.shape)   # (10000, 28, 28)
print("Shape of y_test:", y_test.shape)   # (10000,)

# Display a sample image
plt.figure(figsize=(2,2))
plt.imshow(x_train[0], cmap='gray')
plt.title(f"Label: {y_train[0]}")
plt.show()

print("Pixel values range from:", x_train.min(), "to", x_train.max()) # 0 to 255
print("Unique labels:", np.unique(y_train)) # [0 1 2 3 4 5 6 7 8 9]

