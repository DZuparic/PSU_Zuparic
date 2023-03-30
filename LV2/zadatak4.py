import numpy as np
import matplotlib.pyplot as plt
check = np.zeros((5, 5))
check[::2, 1::2] = 1
check[1::2, ::2] = 1
plt.matshow(check, cmap='gray')
plt.show()