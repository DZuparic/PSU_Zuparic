import urllib.request as ur
import xml.etree.ElementTree as ET
import ssl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=5&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

airQualityHR = ur.urlopen(url)
print('Retrieving: ', url)
root = ET.fromstring(airQualityHR.read())

vrijednost=[]
vrijeme=[]
for child in root:
    vrijednost.append(child[0].text)
    vrijeme.append(child[2].text)

data = {"vrijednost":vrijednost,
        "vrijeme":vrijeme}

df=pd.DataFrame(data, columns=['vrijednost','vrijeme'])

#Dohvaćanje mjerenja dnevne koncentracije lebdećih čestica PM10 za 2017. godinu za grad Osijek.
print(df.to_string())

#Ispis tri datuma u godini kada je koncentracija PM10 bila najveća.
print("Datumi kada je koncentracija bila najveca:")
print(df.sort_values(by=['vrijednost']).tail(3))


#Pomoću barplot prikažite ukupni broj izostalih vrijednosti tijekom svakog mjeseca.
df['datum']=pd.to_datetime(df['vrijeme'], utc=True)
df['mjesec'] = df['datum'].dt.month
df['dan'] = df['datum'].dt.dayofweek
df['mjesec'].count()

mjeseci ={'Siječanj':31-df[df.mjesec == 1]['mjesec'].count(),
          'Veljača':28-df[df.mjesec == 2]['mjesec'].count(),
          'Ožujak':31-df[df.mjesec == 3]['mjesec'].count(),
          'Travanj':30-df[df.mjesec == 4]['mjesec'].count(),
          'Svibanj':31-df[df.mjesec == 5]['mjesec'].count(),
          'Lipanj':30-df[df.mjesec == 6]['mjesec'].count(),
          'Srpanj':31-df[df.mjesec == 7]['mjesec'].count(),
          'Kolovoz':31-df[df.mjesec == 8]['mjesec'].count(),
          'Rujan':30-df[df.mjesec == 9]['mjesec'].count(),
          'Listopad':31-df[df.mjesec == 10]['mjesec'].count(),
          'Studeni':30-df[df.mjesec == 11]['mjesec'].count(),
          'Prosinac':31-df[df.mjesec == 12]['mjesec'].count()}

x = list(mjeseci.keys())
y= list(mjeseci.values())

fig = plt.figure(figsize=(10,5))

plt.bar(x,y,width=0.4)
plt.xlabel("Mjesec")
plt.ylabel("Broj izostalih vrijednosti")
plt.title("Broj izdostalih vrijednosti po mjesecima")
plt.show()