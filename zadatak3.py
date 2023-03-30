import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")

img = img[:,:,0].copy()
for i in range(len(img)):
    img[i]+=40
    if (img[i]>255).any():
        img[i]=255

#rotirana slika
rot=np.rot90(img,3)
#zrcaljena slika
zrc=np.fliplr(img)
#smanjena rezolucija
rez = img[::10,::10]

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()