import numpy as np
from keras.layers import Dense
from keras.models import Sequential

np.random.seed(0)
dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")
x=dataset[0:538,0:8]
y=dataset[0:538,8]
tx=dataset[538:,0:8]
ty=dataset[538:,8]

model = Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(20,activation='relu'))
model.add(Dense(100,activation='sigmoid'))
model.add(Dense(50,activation='relu'))
model.add(Dense(60,activation='sigmoid'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=150, batch_size=10)
scores = model.evaluate(tx, ty)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

predictions = model.predict(x)
rounded = [round(z[0]) for z in predictions]
print(rounded)
