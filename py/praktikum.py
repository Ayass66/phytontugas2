# Daftar barang beserta harganya
daftar_barang = {
    "baju": 50000,
    "celana": 95000,
    "sarung": 100000,
    "jilbab": 25000,
    "gamis": 250000,
}

# Menampilkan daftar barang
print("Daftar Barang:")
for barang, harga in daftar_barang.items():
    print(f"{barang}: Rp {harga}")

#Input jumlah barang yang dibeli
total_belanja = 0
jumlah_barang = int(input("\n Masukkan jumlah barang yang dibeli: "))

#Menghitung total belanjaan 
for i in range(jumlah_barang):
    barang = input(f"Masukkan nama barang ke-{i+1}: ")
    if barang in daftar_barang: 
        total_belanja += daftar_barang[barang]
    else:
        print(f"{barang} tidak ada dalam daftar barang.")

#Menampilkan total belanjaan 
print(f"\n Total belanjaan Anda: Rp {total_belanja}")