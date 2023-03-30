import numpy as np
import matplotlib.pyplot as plt

a1=np.array([1,3,3,2,1])
a2=np.array([1,1,2,2,1])

plt.plot(a1,a2, 'b',linewidth=2, marker=".", markersize=10)
plt.axis([0,4,0,4])
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")
plt.show()