#buat program untuk menghitung aritmatika fungsional

def tambah(x, y):
    i = x + y
    return print(f"hasil penjumlahan x dan y adalah = {i}" )
def pengurangan(x, y):
    i = x - y
    return print(f"hasil pengurangan x dan y adalah = {i}" )
def pembagian(x, y):
    i = x / y
    return print(f"hasil pembagian x dan y adalah = {i}" ) 
def perkalian(x, y):
    i = x * y
    return print(f"hasil perkalian x dan y adalah = {i}" )

x=int(input("masukkan nilai x = "))
y=int(input("masukkan nilai y = ")) 

tambah (x, y)
pengurangan (x, y)
pembagian (x, y)
perkalian (x, y)