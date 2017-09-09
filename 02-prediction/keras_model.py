from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils.np_utils import to_categorical
import numpy as np
import pandas as pd
import sklearn.metrics

model = Sequential()

model.add(Dense(units=32, input_dim=5))
model.add(Activation('relu'))
model.add(Dense(units=32))
model.add(Activation('relu'))
model.add(Dense(units=2))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

df = pd.read_csv('format_two.tsv', delimiter='\t')
data = df[['r0', 'r1', 'r2', 'r3', 'r4', 'r5']].as_matrix()

X_train, y_train = data[:,:-1], data[:,-1]
print(X_train, y_train)

model.fit(X_train, to_categorical(y_train), epochs=100, batch_size=5)
preds = model.predict(X_train)
binary_preds = np.argmax(preds, axis=1)

print('Training acc.:', sklearn.metrics.accuracy_score(binary_preds, y_train))
