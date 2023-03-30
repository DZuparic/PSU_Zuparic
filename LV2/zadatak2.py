import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
print(data)

plt.scatter(data[:,0],data[:,3],c='b',s=data[:,5]*15)

print("Minimalna potrošnja: ", +min(data[:,0]))
print("Maksimalna potrošnja: ", +max(data[:,0]))
print("Srednja vrijednost potrošnji: ", +sum(data[:,0])/len(data[:,0]))
arr=[]

for i,item in enumerate(data[:,1]):
    if item >=6:
        arr.append(data[i,0])
        
print("Minimalna potrošnja: ", +min(arr))
print("Maksimalna potrošnja: ", +max(arr))
print("Srednja vrijednost potrošnji: ", +sum(arr)/len(arr))

plt.xlabel("potrošnja automobila")
plt.ylabel("konjske snage")
plt.show()