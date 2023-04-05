import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")

bright = img[:,:,0].copy()
img2 = img[:,:,0].copy()
img3 = img[:,:,0].copy()

#posvijetljena slika - imshow(bright,..)
for i in range(len(bright)):
    bright[i]=bright[i]+0.2
    if(bright[i]>1).any():
        bright[i]=1

#prikazana druga cetvrtina slike po sirini - imshow(img3,..)
for i in range(640):
    for j in range(960):
        if(j>=960/4 and j<2*960/4):
            img3[i][j]=img3[i][j]
        else:
            img3[i][j]=0

#rotirana slika - imshow(rot,..)
rot=np.rot90(img2,3)

#zrcaljena slika - imshow(zrc,..)
zrc=np.fliplr(img2)

#smanjena rezolucija - imshow(rez,..)
rez = img2[::10,::10]

plt.figure()
plt.imshow(rez, cmap="gray", vmin=0, vmax=1)
plt.show()
