baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

i = 0
while i < baris:
    j = 0
    while j < kolom:
        print("X" if (i + j) % 2 == 0 else "O", end=" ")
        j += 1
    print()
    i += 1