# Tugas 3
# Felis Eren Cristi Milala

# Deklarasi Variabel dan Tipe Data
nama_lengkap = "Felis Eren Cristi Milala" # String
umur = 20 # Integer
ipk = 3.91 # Float
is_student = True # Boolean
mata_kuliah = ["Struktur Data", "AI"] # List

# Manipulasi String
teks = "Halo Semua"
print("Teks Asli:", teks)
print("Huruf Besar:", teks.upper())
print("Huruf Kecil:", teks.lower())
print("Panjang Karakter:", len(teks))
print("Gabungan String: " + teks + " oleh " + nama_lengkap)
print("\n")

# Operasi Matematika Sederhana
a = 15
b = 4

print("Penjumlahan (15 + 4) :", a + b)
print("Pengurangan (15 - 4) :", a - b)
print("Perkalian (15 * 4) :", a * b)
print("Pembagian (15 / 4) :", a / b)
print("Pembagian Bulat (15 // 4) :", a // b)
print("Sisa Bagi / Modulo (15 % 4) :", a % b)
print("\n")

# List dan Akses Elemen
daftar_lab = ["A1", "A2", "B1", "B2", "C1"]
print("Daftar Awal:", daftar_lab)
print("Elemen Kedua :", daftar_lab[1])

# Menambahkan item baru (append)
daftar_lab.append("C2")
print("Setelah Tambah (append):", daftar_lab)

# Menghapus item (remove)
daftar_lab.remove("B2")
print("Setelah Hapus :", daftar_lab)

# Menghapus item terakhir (pop)
item_dibuang = daftar_lab.pop()
print("Item yang di-pop:", item_dibuang)
print("List Akhir:", daftar_lab)
print("\n")

# Penggunaan Input dari User
user_nama = input("Masukkan nama Anda: ")
user_umur = input("Masukkan umur Anda: ")
print(f"Halo, nama saya {user_nama} dan umur saya {user_umur} tahun.")