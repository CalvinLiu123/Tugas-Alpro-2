from scipy.spatial import KDTree
import numpy as np

# Data lokasi restoran (latitude, longitude)
restoran = {
    "Restoran A": (1.2921, 103.7768),
    "Restoran B": (1.3000, 103.8000),
    "Restoran C": (1.3100, 103.8200),
    "Restoran D": (1.2850, 103.7800),
    "Restoran E": (1.2950, 103.7900)
}

# Konversi lokasi ke array untuk KDTree
lokasi_restoran = np.array(list(restoran.values()))
nama_restoran = list(restoran.keys())

# Membuat KDTree
kd_tree = KDTree(lokasi_restoran)

# Lokasi pengguna (latitude, longitude)
lokasi_pengguna = (1.2980, 103.7900)

# Mencari restoran terdekat
jarak, indeks = kd_tree.query(lokasi_pengguna)
restoran_terdekat = nama_restoran[indeks]

# Output hasil
print(f"Restoran terdekat: {restoran_terdekat}")
print(f"Jarak ke restoran: {jarak:.4f} satuan koordinat")
