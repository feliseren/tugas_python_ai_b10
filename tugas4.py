# Tugas 4
# Felis Eren Cristi Milala

# LIST: AKSES & MANIPULASI
print("LIST (ARRAY)")
data_list = ["A1", "A2", "B1", "B2", "C1", 1, 2, 3, 4, 5]
print(f"List Awal: {data_list}")
print(f"Elemen Pertama: {data_list[0]}  dan Terakhir: {data_list[-1]}")
print(f"Slicing [1:6:2]: {data_list[1:6:2]}")

# Manipulasi
print(f"List Sebelum Manipulasi: {data_list}\n")
data_list.append("YOLOv8") 
data_list.insert(2, "Semarang") 
data_list.extend([100, 200]) 
data_list.pop()
data_list.remove(3) 
print(f"List Sesudah Manipulasi: {data_list}\n")


# TUPLE: IMMUTABILITY & UNPACKING 
print("TUPLE (IMMUTABLE)")
data_tuple = ("Felis", 24060122130197, "Informatika", "Semarang", 2022, "Aktif")
print(f"Panjang Tuple: {len(data_tuple)}")
print(f"Akses Indeks 2: {data_tuple[2]}")

# Unpacking
nama, nim, prodi, *sisanya = data_tuple
print(f"Unpacked - Nama: {nama}, NIM: {nim}, Prodi: {prodi}")
print(f"Rest (*sisanya): {sisanya}\n")


# SET: KEUNIKAN & HIMPUNAN 
print("SET (HIMPUNAN)")
set_a = {1, 2, 3, 4, 5, 5, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

print(f"Union : {set_a | set_b}")
print(f"Intersection : {set_a & set_b}")
print(f"Difference : {set_a - set_b}")
print(f"Symm. Diff : {set_a ^ set_b}\n")


# DICTIONARY: KEY/VALUE 
print("DICTIONARY")
mhs = {
    "nama": "Felis Eren",
    "nim": "24060122130197",
    "angkatan": 2023,
    "kota": "Semarang"
}

mhs["hobi"] = "Masak" 
mhs["angkatan"] = 2022
del mhs["kota"]
        
print(f"Keys   : {list(mhs.keys())}")
print(f"Values : {list(mhs.values())}")
print("Iterasi Item:")
for key, value in mhs.items():
    print(f"- {key}: {value}\n")


# NESTED STRUCTURES
print("NESTED (LIST OF DICTS)")
perpustakaan = [
    {"judul": "Python Crash Course", "penulis": "Eric Matthes", "tahun": 2019},
    {"judul": "Deep Learning", "penulis": "Ian Goodfellow", "tahun": 2016},
    {"judul": "Clean Code", "penulis": "Robert C. Martin", "tahun": 2008},
    {"judul": "Hands-On Machine Learning", "penulis": "Aurelien Geron", "tahun": 2022}
]

print("Daftar Judul Buku:")
for buku in perpustakaan:
    print(f" {buku['judul']} ")

# Filter buku terbit >= 2018 menggunakan List Comprehension
buku_baru = [b['judul'] for b in perpustakaan if b['tahun'] >= 2018]
print(f"Buku Terbit >= 2018: {buku_baru}\n")


# COMPREHENSION & UTILITAS 
print("COMPREHENSION")
angka = range(1, 21)
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka[:5]]
print(f"List Genap: {genap}")
print(f"List Kuadrat (1-5): {kuadrat}")

# Dict Comprehension
status_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print(f"Dict Status: {status_angka}")

# Set Comprehension
kalimat = "Halo Semuanya"
huruf_unik = {char.lower() for char in kalimat if char.isalpha()}
print(f"Huruf Unik: {sorted(list(huruf_unik))}\n")


# KEANGGOTAAN & PENCARIAN
print("PENCARIAN & KEANGGOTAAN")
daftar_lab = ["A1", "A2", "B1", "B2", "C1"]
target = "B1"

if target in daftar_lab:
    posisi = daftar_lab.index(target)
    print(f"'{target}' ditemukan pada posisi indeks: {posisi}")
else:
    print(f"'{target}' tidak ditemukan.")

# Cek di Set
print(f"Apakah 6 ada di Set B? {6 in set_b}")