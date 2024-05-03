uts=int(input("masukkan nilai uts ="))
uas=int(input("masukkan nilai uas ="))
praktikum=int(input("masukkan nilai praktikum ="))

nilai=(uts + uas + praktikum) / 3

if nilai >= 85 :
    print("lulus dgn predikat A. Dgn nilai rata-rata :", nilai)
elif nilai >= 80 < 85 :
    print("lulus dgn predikat A-. Dgn nilai rata-rata :", nilai)
else:
    print("tidak lulus", nilai)