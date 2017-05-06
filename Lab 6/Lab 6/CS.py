import numpy as np
from keras.layers import Dense
from keras.models import Sequential


np.random.seed(0)
dataset = np.genfromtxt("cs-training.csv", delimiter=",")
x=dataset[:10000,2:10]
y=dataset[:100000,1]
tx=dataset[10000:150000,2:10]
ty=dataset[10000:150000,1]
model = Sequential()
model.add(Dense(30,input_dim=8,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=150, batch_size=10)
scores = model.evaluate(tx, ty)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

predictions = model.predict(x)
rounded = [round(z[0]) for z in predictions]
print(rounded)
