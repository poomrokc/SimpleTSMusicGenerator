import tensorflow as tf
import process
from tensorflow.keras import layers
from tensorflow.keras import optimizers
import numpy as np

np.set_printoptions(threshold=np.nan)

print(tf.VERSION)
print(tf.keras.__version__)

data,labelType,labelNote,labelTime=process.getNumpyAllData(['rock1.mid','rock2.mid','rock3.mid','rock4.mid','rock5.mid','rock6.mid','rock7.mid','rock8.mid','rock9.mid'])
print(data.shape)
print(labelType.shape)

#Model Type

model = tf.keras.Sequential()

model.add(layers.Dense(30,input_dim=30,activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data, labelType, epochs=200, batch_size=100,validation_split=0.1, verbose=1)
model.save('rock44Type.h5')

#Model Note

model = tf.keras.Sequential()

model.add(layers.Dense(30,input_dim=30,activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(128, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data, labelNote, epochs=200, batch_size=100,validation_split=0.1, verbose=1)
model.save('rock44Note.h5')

#Model Time

model = tf.keras.Sequential()

model.add(layers.Dense(30,input_dim=30,activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(600, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data, labelTime, epochs=200, batch_size=100,validation_split=0.1, verbose=1)
model.save('rock44Time.h5')
