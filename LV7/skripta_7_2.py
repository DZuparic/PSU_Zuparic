from keras.models import load_model
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np
from tensorflow import keras
from keras.utils import img_to_array

filename = 'osam.png'

img = mpimg.imread(filename)
img = color.rgb2gray(img)
img = resize(img, (28, 28))


plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')


# TODO: ucitaj model

model = keras.models.load_model('my_model')


# TODO: napravi predikciju 



# TODO: ispis rezultat
print("------------------------")
print("Slika sadrzi znamenku: ", np.argmax(model.predict(img)))



