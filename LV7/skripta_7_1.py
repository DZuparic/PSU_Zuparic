import numpy as np
from tensorflow import keras
from keras import layers
from keras.layers import Dense
from keras.layers import Dropout
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa

for i in range(9): 
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i].reshape((28,28)), cmap='gray')
plt.show()


# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu

model = keras.Sequential([
  layers.Flatten(input_shape=(28, 28)),
  layers.Dense(128, activation='relu'),
  layers.Dense(10)
])

model.summary()



# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

# TODO: provedi ucenje mreze

model.fit(x_train_s, y_train_s, epochs=7, batch_size=32)


# TODO: Prikazi test accuracy i matricu zabune

loss_and_metrics = model.evaluate(x_test_s, y_test_s, batch_size=128)
print(loss_and_metrics)


# TODO: spremi model

model.save('my_model')


