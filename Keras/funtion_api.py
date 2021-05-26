from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow import keras
import numpy as np
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
import tensorflow as tf


(x_train, y_train), (x_test, y_test) = mnist.load_data()

num_labels = len(np.unique(y_train))

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

image_size = x_train.shape[1]
x_train = np.reshape(x_train, [-1, image_size, image_size, 1])
x_test = np.reshape(x_test, [-1, image_size, image_size, 1])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

input_shape = (image_size, image_size, 1)
batch_size = 128
kernel_size = 3
pool_size = 2
filters = 64
dropout = 0.2

batch_size1 = 128
kernel_size1 = 3
pool_size1 = 2
filters1 = 64
dropout1 = 0.2


inputs = Input(shape=input_shape)

x = Conv2D(filters=filters,
           kernel_size=kernel_size,
           activation='relu')(inputs)
x = MaxPooling2D(pool_size)(x)
x = Conv2D(filters=filters,
           kernel_size=kernel_size,
           activation='relu')(x)
x = MaxPooling2D(pool_size)(x)
x = Conv2D(filters=filters,
           kernel_size=kernel_size,
           activation='relu')(x)
x = Flatten()(x)
x = Dropout(dropout)(x)
outputs = Dense(num_labels, activation='softmax')(x)
model = keras.Model(inputs=inputs, outputs=outputs, name='mnist_model')

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, batch_size=batch_size)

_, acc = model.evaluate(x_test,
                        y_test,
                        batch_size=batch_size,
                        verbose=0)

print("\nTest accuracy: %.1f%%" % (100.0 * acc))
