from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

boston = load_boston()

df = pd.DataFrame(boston.data)

df.columns = boston.feature_names
df['MEDV'] = pd.DataFrame(boston.target)
df.shape

df.replace(0, np.nan , inplace = True)
print(df.isnull().sum()/len(df))

df = df.drop('ZN', axis=1)
df = df.drop('CHAS', axis = 1)

mask = np.zeros_like(df.corr())
mask[np.triu_indices_from(mask)] = True


sns.set(rc={'figure.figsize':(8.5,8.5)})
sns.heatmap(df.corr().round(2),square= True ,cmap='YlGnBu', annot= True , mask=mask)

columns = ['TAX', 'RAD' , 'NOX','INDUS','DIS']
df= df.drop(columns= columns)

features = df.drop('MEDV',1).columns
target = df['MEDV']
plt.figure(figsize=(20,20))
for index,feature_name in enumerate(features):
    plt.subplot(4,len(features)/2,index+1)
    plt.scatter(df[feature_name],target)
    plt.title(feature_name,fontsize = 15)
    plt.xlabel(feature_name, fontsize=8)
    plt.ylabel('MEDV',fontsize=15)


df["LOGSTAT"] = df["LSTAT"].apply(np.log)
plt.figure(figsize=(20,10))

plt.subplot(1,2,1)
plt.scatter(df['LSTAT'],df['MEDV'], color= 'green')
plt.title('Original',fontsize=20)
plt.xlabel('LSTAT',fontsize=20)
plt.ylabel('MEDV',fontsize=20)
plt.plot([0,40], [30,0])

plt.subplot(1,2,2)
plt.scatter(df['LOGSTAT'],df['MEDV'],color='red')
plt.title('Log',fontsize=20)
plt.xlabel('Transformed LSTAT',fontsize = 20)
plt.ylabel('Transformed MEDV',fontsize = 20)
plt.plot([0,4],[50,0])

X = df[['LOGSTAT','RM']]
Y = df.MEDV


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size= 0.30,random_state=10)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

lrn=LinearRegression()

lrn.fit(X_train,Y_train)
y_predicted= lrn.predict(X_test)


r2 = lrn.score(X_test,Y_test)
rmse= (np.sqrt(mean_squared_error(Y_test,y_predicted)))
print('r-squared : {}'.format(r2))
print('--------------------------------------------------')
print('root mean squared error: {}'.format(rmse))

plt.figure(figsize=(10,8))
plt.scatter(y_predicted,Y_test,color='green')
plt.plot([0,50],[0,50],'--k')
plt.axis('tight')
plt.ylabel('The True Prices',  fontsize=20)

plt.xlabel('Moj Prediction',fontsize=20)
plt.title("Predicted vs Actual",fontsize=20)


plt.show()