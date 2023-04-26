import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')

#5 automobila s najvecom potrosnjom
print(mtcars.sort_values(by=['mpg']).tail(5))

#3 automobila s 8 cilindara koji imaju najmanju potrošnju
print(mtcars[mtcars.cyl == 8].sort_values(by=['mpg']).head(3))

print("Srednja potrošnja automobila sa 6 cilindara:", mtcars[mtcars.cyl == 8].mpg.mean())

print("Srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs:",mtcars[(mtcars.cyl == 4) & (mtcars.wt >2) & (mtcars.wt < 2.2)]['mpg'].mean())

print("Broj automobila s autmatskim mjenjačem:",mtcars[mtcars.am == 0]['am'].count())

print("Broj automobila s ručnim mjenjačem:",mtcars[mtcars.am == 1]['am'].count())

print("Broj automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga:",mtcars[(mtcars.am == 0) & (mtcars.hp > 100)]['am'].count())

#masa automobila u kilogramima
mtcars['kg'] = mtcars['wt']*1000*0.45
print(mtcars[['car', 'wt', 'kg']])