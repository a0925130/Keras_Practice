import numpy as np
import xlrd
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense


def excel_read():
    wb = xlrd.open_workbook('iris_plants_data.xls')
    sheet = wb.sheet_by_name('Sheet1')
    data = []
    for i in range(sheet.nrows):
        cell = sheet.row_values(i)
        for j in range(sheet.ncols):
            data1 = cell[j]
            data.append(data1)
    return data


a = excel_read()
data_iris = [a[i:i + 5] for i in range(0, len(a), 5)]
np.random.shuffle(data_iris)

for subarray in data_iris:
    for i, label in enumerate(subarray):
        if label == 'setosa':
            subarray[i] = 0
        elif label == 'versicolor':
            subarray[i] = 1
        elif label == 'virginica':
            subarray[i] = 2

print(data_iris)
x_data, y_data = np.hsplit(np.array(data_iris), (4,))
y_data = y_data.reshape(150, )
y_data = keras.utils.to_categorical(y_data, 3)
examples = np.array(x_data).reshape(150, 4)
x_data = x_data.T

for feature in x_data:
    min_val = feature.min()
    scalar = feature.max() - min_val
    for i, val in enumerate(feature):
        feature[i] = (val - min_val) / scalar
x_data = x_data.T
(x_train, x_test), (y_train, y_test) = np.split(x_data, [int(len(x_data) * 0.8)]), \
                                       np.split(y_data, [int(len(y_data) * 0.8)])

input_shape = (4,)
batch_size = 10

model = Sequential()
model.add(Dense(256, input_shape=input_shape))
model.add(Dropout(0.5))
model.add(Dense(256))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))

model.summary()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=batch_size, epochs=30)

score = model.evaluate(x_test, y_test, batch_size=batch_size, verbose=0)
print("loss:", score[0])
print("acc:", score[1])
