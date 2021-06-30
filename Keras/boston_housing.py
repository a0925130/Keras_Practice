from math import sqrt

import numpy as np
import xlrd
import tensorflow.keras as keras
from matplotlib import pyplot
from numpy import concatenate
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense
from sklearn.preprocessing import StandardScaler
from tensorflow.python.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping


def excel_read():
    wb = xlrd.open_workbook('boston_housing_data.xls')
    sheet = wb.sheet_by_name('Sheet1')
    data = []
    for i in range(sheet.nrows):
        cell = sheet.row_values(i)
        for j in range(sheet.ncols):
            data1 = cell[j]
            data.append(data1)
    return data


a = excel_read()
data_housing = [a[i:i + 4] for i in range(0, len(a), 4)]
np.random.shuffle(data_housing)
print(data_housing)
x_data, y_data = np.hsplit(np.array(data_housing), (3,))
y_data = y_data/1000
(x_train, x_test), (y_train, y_test) = np.split(x_data, [int(len(x_data) * 0.8)], axis=0), \
                                       np.split(y_data, [int(len(y_data) * 0.8)], axis=0)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
print(x_train[0])
print(x_test[0])
mean = x_train.mean(axis=0)
std = x_train.std(axis=0)
x_train -= mean
x_train /= std
mean = x_test.mean(axis=0)
std = x_test.std(axis=0)
x_test -= mean
x_test /= std
print(x_train[0])
print(x_test[0])
input_shape = (3,)
batch_size = 10

model = Sequential()
model.add(Dense(16, activation='relu', input_shape=input_shape))
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))

model.summary()
model.compile(loss='mean_squared_error', optimizer='adam')


early_stopping = EarlyStopping(monitor='val_loss', patience=50, verbose=2)

history = model.fit(x_train, y_train, epochs=300, batch_size=20,
                    validation_data=(x_data, y_data), verbose=2,
                    shuffle=False, callbacks=[early_stopping])

pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

model.save("boston_housing.h5")
model = load_model("boston_housing.h5")
price = model.predict(x_test)
rmse = sqrt(mean_squared_error(y_test, price))
print('Test RMSE: %.3f' % rmse)
pyplot.plot(y_test, label='y_test')
pyplot.plot(price, label='price')
pyplot.legend()
pyplot.show()