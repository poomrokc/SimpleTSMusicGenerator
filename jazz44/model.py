import tensorflow as tf
import process
from tensorflow.keras import layers
from tensorflow.keras import optimizers
import numpy as np

np.set_printoptions(threshold=np.nan)

print(tf.VERSION)
print(tf.keras.__version__)

data,labelType,labelNote,labelTime=process.getNumpyAllData(['almonds.mid','alljarr.mid','4bros.mid','israel.mid','chipblue.mid'])
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
model.fit(data, labelType, epochs=300, batch_size=100,validation_split=0.1, verbose=1)
model.save('jazz44Type.h5')

#Model Note

model = tf.keras.Sequential()

model.add(layers.Dense(30,input_dim=30,activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(128, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data, labelNote, epochs=300, batch_size=100,validation_split=0.1, verbose=1)
model.save('jazz44Note.h5')

#Model Time

model = tf.keras.Sequential()

model.add(layers.Dense(30,input_dim=30,activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(600, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data, labelTime, epochs=300, batch_size=100,validation_split=0.1, verbose=1)
model.save('jazz44Time.h5')
