ocjena = -1
while ocjena<0 or ocjena>1:
    ocjena = float(input("Unesite ocjenu iz intervala 0.0 do 1.0: "))

if ocjena < 0.6:
    print("F")
elif 0.6 <= ocjena < 0.7:
    print("D")
elif 0.7 <= ocjena < 0.8:
    print("C")
elif 0.8 <= ocjena < 0.9:
    print("B")
elif ocjena >= 0.9:
    print("A")
else:
    print("Unesena vrijednost nije unutar intervala!")