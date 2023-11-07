bilangan_terbesar = None

while True:
    angka = float(input("Masukkan bilangan : "))

    # Pengguna ingin menyelesaikan program
    if angka == 0:
        break

    # Memeriksa apakah angka yang dimasukkan lebih besar dari yang sebelumnya
    if bilangan_terbesar is None or angka > bilangan_terbesar:
        bilangan_terbesar = angka

if bilangan_terbesar is not None:
    print(f"Bilangan terbesar adalah: {bilangan_terbesar}")
else:
    print("Tidak ada bilangan yang dimasukkan.")