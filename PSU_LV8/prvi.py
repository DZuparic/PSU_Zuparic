import os
import shutil
import keras

testCSV = "archive/Test.csv"
Test_Dir = "archive/Test_Dir"

# kreiraj direktorij gdje ce se spremiti testne slike
os.makedirs(Test_Dir, exist_ok=True)

# otvori CVS sa labelama i putanjama
rows = open(testCSV).read().strip().split("\n")[1:]


# prolazak kroz sve unose u CSV-u; kopiraj sliku u poddirektorij
for r in rows:

    (label, imagePath) = r.strip().split(",")[-2:]
    os.makedirs(os.path.join(Test_Dir,label), exist_ok=True)
    shutil.copy(os.path.join("archive", imagePath), os.path.join(Test_Dir,label))

