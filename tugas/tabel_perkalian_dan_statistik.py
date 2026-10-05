# Tugas 3: Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

# Validasi n
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Inisialisasi
total_semua = 0
count_genap = 0

# Nested loop
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j

        # Menampilkan tabel perkalian
        print(f"{hasil:4}", end="")

        # Menghitung jumlah per baris
        total_baris += hasil

        # Menghitung jumlah keseluruhan
        total_semua += hasil

        # Menghitung banyak hasil genap
        if hasil % 2 == 0:
            count_genap += 1

    print(f" | jumlah baris = {total_baris}")

# Hasil akhir
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")