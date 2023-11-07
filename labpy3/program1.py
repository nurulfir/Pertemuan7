modal_awal = 100_000_000  # Modal awal sebesar 100 juta
labas = []  # Daftar laba bulanan

# Perulangan dari bulan ke 1 hingga bulan ke 8
for bulan in range(1, 9):
    if bulan <= 2:
        laba = 0  # Bulan pertama dan kedua belum mendapatkan laba
    elif bulan == 3:
        laba = modal_awal * 0.1  # Bulan ketiga mendapatkan laba sebesar 1%
    elif bulan == 5:
        laba = modal_awal * 0.5  # Bulan kelima mendapatkan laba sebesar 5%
    elif bulan == 8:
        laba = modal_awal * 0.5 * 0.4  # Bulan kedelapan mengalami penurunan 2%
    else:
        laba = labas[bulan - 2]  # Laba bulan sebelumnya

    labas.append(laba)

#Print hasil laba bulanan
for bulan, laba in enumerate(labas, start=1):
    print(f"Laba Bulan Ke- {bulan} Sebesar: {laba:.2f}")

total_laba = 0

for laba in labas:
    total_laba += laba

print(f"Total Laba Adalah: {total_laba:.2f}")
