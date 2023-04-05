import matplotlib.pyplot as plt
import numpy as np

def build_checkerboard(v, a, b):
    x = np.zeros((v,v))
    y = np.ones((v,v))
    r1 = (np.hstack((x,y)))
    r1 = r1.copy()*(b/50)
    r2 = (np.hstack((y,x)))*b
    r2 = r2.copy()*(b/50)
    check=(np.vstack((r1,r2)))*a
    return check

ploca = build_checkerboard(50,200,300)

plt.imshow(ploca, cmap='gray', vmin=0, vmax=255)
plt.show()
