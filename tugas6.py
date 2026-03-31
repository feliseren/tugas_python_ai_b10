# Tugas 6
# Nama: Felis Eren Cristi Milala
import numpy as np
import pandas as pd
import os

np.random.seed(42)

# NUMPY: DATA & STATISTIK 
# Membuat 10 nilai ujian acak antara 50 sampai 100
nilai_ujian = np.random.randint(50, 101, size=10)

def hitung_statistik_numpy(arr):
    stats = {
        "Rata-rata": np.mean(arr),
        "Median": np.median(arr),
        "Standar Deviasi": np.std(arr),
        "Nilai Min": np.min(arr),
        "Nilai Max": np.max(arr)
    }
    return stats

# PANDAS: DATAFRAME
data = {
    "nama": ["Felis", "Budi", "Citra", "Dandi", "Eka", "Fani", "Gani", "Hana", "Iwan", "Joko"],
    "nim": [f"240601231300{i}" for i in range(10)],
    "nilai": nilai_ujian
}

df_mhs = pd.DataFrame(data)

# Tambahkan kolom status
df_mhs['status'] = df_mhs['nilai'].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

# OOP
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self):
        # Menghitung rata-rata kolom nilai
        return round(self.df['nilai'].mean(), 2)

    def pass_rate(self, threshold: float = 70.0):
        # Menghitung persentase kelulusan
        lulus = len(self.df[self.df['nilai'] >= threshold])
        total = len(self.df)
        return (lulus / total) * 100

    def save_summary(self, path: str):
        # Menulis ringkasan statistik dan DataFrame ke file .txt.
        stats = hitung_statistik_numpy(self.df['nilai'].values)
        jml_lulus = len(self.df[self.df['status'] == "LULUS"])
        jml_tidak = len(self.df) - jml_lulus

        with open(path, 'w') as f:
            f.write("RINGKASAN TUGAS 6\n")
            f.write(f"File: {path}\n")
            f.write("-" * 25 + "\n")
            f.write("STATISTIK NUMPY:\n")
            for k, v in stats.items():
                f.write(f"{k}: {v:.2f}\n")
            
            f.write("\nRINGKASAN DATAFRAME:\n")
            f.write(f"Total Baris Data : {len(self.df)}\n")
            f.write(f"Jumlah Lulus     : {jml_lulus}\n")
            f.write(f"Jumlah Tidak Lulus: {jml_tidak}\n")
            f.write(f"Persentase Lulus : {self.pass_rate():.1f}%\n")
            f.write("-" * 25 + "\n")
        
        print(f"Ringkasan berhasil disimpan ke: {path}")

    def __str__(self):
        return f"GradeBook(Jumlah Data={len(self.df)}, Rata-rata={self.average()})"

# DEMO
if __name__ == "__main__":
    print("NUMPY")
    stats_np = hitung_statistik_numpy(nilai_ujian)
    for k, v in stats_np.items():
        print(f"{k}: {v:.2f}")
    print("\n")

    print("PANDAS")
    print("5 Baris Pertama DataFrame:")
    print(df_mhs.head())
    print("\n")

    print("OOP")
    my_gradebook = GradeBook(df_mhs)
    print(my_gradebook)
    print(f"Rata-rata Kelas    : {my_gradebook.average()}")
    print(f"Persentase Lulus   : {my_gradebook.pass_rate()}%")
    # Simpan ke file
    my_gradebook.save_summary("ringkasan_tugas6.txt")