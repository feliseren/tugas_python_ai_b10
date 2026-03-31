# Tugas 5
# Nama: Felis Eren Cristi Milala

# FUNCTIONS
def greet(nama: str):
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0):
    #Mengembalikan hasil penjumlahan a + b.
    return a + b

def rata_rata(angka: list[float]):
    #Mengembalikan rata-rata dengan 2 angka di belakang koma.
    if not angka:
        return 0.0
    hasil = sum(angka) / len(angka)
    return round(hasil, 2)


# CLASS STUDENT
class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []

    def tambah_nilai(self, skor: float):
        # Menambah satu nilai ke dalam list nilai
        self.nilai.append(skor)

    def rata_nilai(self):
        # Menghitung rata-rata nilai menggunakan fungsi rata_rata()
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0):
        # Menentukan status kelulusan berdasarkan threshold
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self):
        # Representasi string ringkas dari objek Student
        return (f"Student(nama='{self.nama}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")


# DEMO

if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f"Tambah(5, 7) : {tambah(5, 7)}")
    print(f"Tambah(10)   : {tambah(10)}")
    print(f"Rata-rata [80, 90, 100]: {rata_rata([80, 90, 100])}")
    print(f"Rata-rata []           : {rata_rata([])}")
    print("\n")

    print("=== CLASS STUDENT ===")
    mhs1 = Student("Felis Eren", "24060123130098")
    mhs1.tambah_nilai(85.5)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(78.0)

    mhs2 = Student("Budi", "A123")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.5)
    print(mhs1)
    print(mhs2)

    print(f"\nDetail {mhs1.nama}:")
    print(f"- Rata-rata: {mhs1.rata_nilai()}")
    print(f"- Status   : {mhs1.status()}")

    print(f"\nDetail {mhs2.nama}:")
    print(f"- Rata-rata: {mhs2.rata_nilai()}")
    print(f"- Status   : {mhs2.status(threshold=75.0)}")