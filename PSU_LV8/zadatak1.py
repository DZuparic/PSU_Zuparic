import os
import numpy as np
import shutil
import keras
import tensorflow
from keras import layers
from keras.utils import image_dataset_from_directory
from keras import Sequential
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt

# ucitavanje podataka iz odredenog direktorija
train_ds = image_dataset_from_directory(
    directory='archive/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48))

num_classes = 43
input_shape = (48, 48, 3)

# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu
model = Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
    layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Dropout(0.2),
    layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Dropout(0.2),
    layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
    layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(43, activation='softmax')
])
model.summary()
# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss='categorical_crossentropy',
                optimizer='Nadam',
                metrics=['accuracy'])

# TODO: provedi ucenje mreze
model.fit(train_ds, epochs=10, batch_size=32)

test_ds = image_dataset_from_directory(
    directory='archive/Test_dir/',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48))

loss_and_metrics = model.evaluate(test_ds, batch_size=128)
print(loss_and_metrics)

cm = confusion_matrix(test_ds, train_ds)
cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[False,True])
cm_display.plot()
plt.show()

model.save('moj_model')