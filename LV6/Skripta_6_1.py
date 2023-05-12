import numpy as np
from sklearn.datasets import fetch_openml
from matplotlib import pyplot as plt
import joblib
import pickle
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix


X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)


# TODO: prikazi nekoliko ulaznih slika
for i in range(9): 
    plt.subplot(330 + 1 + i)
    plt.imshow(X[i].reshape((28,28)), cmap='gray')
plt.show()

# skaliraj podatke, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

# TODO: izgradite vlastitu mrezu pomocu sckitlearn MPLClassifier 
mlp_mnist = MLPClassifier(hidden_layer_sizes=(300,), max_iter=15, alpha=1e-4,solver='sgd', verbose=10, random_state=1, learning_rate_init=.1)
mlp_mnist.fit(X_train, y_train)

# TODO: evaluirajte izgradenu mrezu
print("Training set score: %f" % mlp_mnist.score(X_train, y_train))
print("Test set score: %f" % mlp_mnist.score(X_test, y_test))


cm = confusion_matrix(y_test, mlp_mnist.predict(X_test))
print(cm)

# spremi mrezu na disk
filename = "NN_model.sav"
joblib.dump(mlp_mnist, filename)


