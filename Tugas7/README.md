# Praktikum 7

## Latihan 1

* Buat program sederhada dengan input 2 buah bilangan, kemudian
tentukan bilangan terbesar dari kedua bilangan tersebut
menggunakan statement if.

``````
bilangan1 = float(input("Masukan bilangan pertama : "))
bilangan2 = float(input("Masukan bilangan kedua : "))


if bilangan1 > bilangan2:
   bilangan_terbesar = bilangan1
else:
   bilangan_terbesar = bilangan2

   print("Bilangan terbesar adalah :", bilangan_terbesar )
``````

 ### Maka outputnya
 ![Alt text](ol1.png)


## Latihan 2

* Buat program untuk mengurutkan data berdasarkan input sejumlah
data (minimal 3 variable input atau lebih), kemudian tampilkan
hasilnya secara berurutan mulai dari data terkecil.

``````
# Meminta pengguna memasukkan 3 bilangan
print("Program mengurutkan data")
bil1 = int(input("Bilangan ke-1: "))
bil2 = int(input("Bilangan ke-2: "))
bil3 = int(input("Bilangan ke-3: "))

data = (bil2, bil3, bil1)

print("Urutan bilangan :", data)
``````

### Maka outputnya
![Alt text](ol2.png)

# Lab 3: Perulangan

## Latihan 1

* Buat program dengan perulangan bertingkat (nested) for yang
menghasilkan output sebagai berikut:

![Alt text](img.png)

## kode programnya
``````
baris = 10
kolom = baris

for bar in range(baris):
    for col in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab), end='')
    print()
``````

## maka outputnya

![Alt text](olp1.png)


## Latihan 2

* Tampilkan n bilangan acak yang lebih kecil dari 0.5.
* nilai n diisi pada saat runtime
* anda bisa menggunakan kombinasi while dan for untuk
menyelesaikannya

## kode programnya

``````
import random

n = int(input("Masukkan jumlah n: "))

count = 0

while count < n:
    bilangan = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
    if bilangan < 0.5:
        print(bilangan)
        count += 1

``````

## maka outputnya
![Alt text](olp2.png)
