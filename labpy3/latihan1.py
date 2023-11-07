import random

n = int(input("Masukkan jumlah n: "))

count = 0

while count < n:
    bilangan = random.random()
    if bilangan < 0.5:
        print(bilangan)
        count += 1

print("Selesai")