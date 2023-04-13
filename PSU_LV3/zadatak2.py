import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics

mtcars = pd.read_csv('mtcars.csv')

prvi = mtcars(mtcars.cyl == 4)
prvi = statistics.mean(prvi.mpg)
drugi = mtcars(mtcars.cyl == 6)
drugi = statistics.mean(drugi.mpg)
treci = mtcars(mtcars.cyl == 8)
treci = statistics.mean(treci.mpg)

df = pd.DataFrame({'cilindri': ['4', '6', '8'], 'avg_mpg':[prvi, drugi, treci]})
ax = df.plot.bar(x='cilindar', y='avg_mpg')
plt.show()