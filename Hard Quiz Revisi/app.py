import time

anggaran = 25000000
pengeluaran = [
    ("Tiket Pesawat Iberia", 7151000),
    ("Hotel Barcelo Sants", 2782000),
    ("Taksi", 2000000),
    ("Tur Camp Nou", 1000000),
    ("Jajan di Coffee Shop", 1000000),
    ("Pemandangan di The W Hotel", 500000),
    ("Makan Siang & Malam (2 hari)", 4000000),
    ("Belanja & Suvenir", 2000000),
    ("Aktivitas Tambahan", 1500000),
    ("Tur Sagrada Familia", 1500000),
    ("Mengunjungi Park Güell", 1200000),
    ("Tur La Rambla & Gothic Quarter", 1300000),
    ("Tur ke Montjuïc", 800000),
    ("Masuk ke Casa Batlló", 700000),
    ("Tiket Museum Picasso", 600000),
    ("Tambahan Kuliner & Oleh-oleh", 500000),
    ("Alternatif Tur Gaudi Architecture (Macet)", 500000),
    ("Transportasi Alternatif ke Gaudi Architecture", 300000),
    ("Minuman & Camilan di Camp Nou", 37000),
    ("Saat Di Coffee Shop saya jajan tumbler lucu" , 30000)
]

solusi = []

def cari_kombinasi(sisa_anggaran, indeks, kombinasi_sekarang):
    if sisa_anggaran == 0:
        global solusi
        solusi = kombinasi_sekarang[:]
        return True
    if sisa_anggaran < 0 or indeks >= len(pengeluaran):
        return False
    
    # Coba memasukkan item saat ini
    nama_item, biaya = pengeluaran[indeks]
    
    # Jika macet, ganti dengan alternatif
    if nama_item == "Tur Gaudi Architecture":
        nama_item = "Alternatif Tur Gaudi Architecture (Macet)"
    
    kombinasi_sekarang.append((nama_item, biaya))
    if cari_kombinasi(sisa_anggaran - biaya, indeks + 1, kombinasi_sekarang):
        return True
    
    # Jika gagal, coba tanpa item ini
    kombinasi_sekarang.pop()
    return cari_kombinasi(sisa_anggaran, indeks + 1, kombinasi_sekarang)

# Mulai timer
start_time = time.time()

# Jalankan algoritma pencarian kombinasi
cari_kombinasi(anggaran, 0, [])

# Hitung sisa uang
sisa_uang = anggaran - sum(item[1] for item in solusi)

# Jika masih ada sisa uang, gunakan kategori kecil hingga habis
for item in pengeluaran:
    if sisa_uang >= item[1] and item not in solusi:
        solusi.append(item)
        sisa_uang -= item[1]
    if sisa_uang == 0:
        break

# Stop timer
end_time = time.time()

# Cetak hasil
if solusi:
    print("Pengeluaran untuk menghabiskan 25 juta:")
    for item in solusi:
        print(f"- {item[0]}: Rp{item[1]:,}")
    print(f"Total: Rp{sum(item[1] for item in solusi):,}")
    print(f"Sisa uang: Rp{sisa_uang:,}")
    print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")
else:
    print("Tidak ada kombinasi yang tepat untuk menghabiskan seluruh uang.")

 # Jika macet, ganti dengan alternatif
    #if nama_item == "Tur Gaudi Architecture":
        #nama_item = "Alternatif Tur Gaudi Architecture (Macet)"



#Fungsi cari_kombinasi , fungsi yang mencoba menyusun kombinasi pengeluaran dengan mencoba membatalkan
#pilihan jika tidak sesuai. 
#Basis Rekursi
#if sisa_anggaran == 0:
    #global solusi
    #solusi = kombinasi_sekarang[:]
    #return True
    #Jika sisa anggaran 0 makan di tambahkan ke solusi

#Kondisi Penghentian Rekursi
#if sisa_anggaran < 0 or indeks >= len(pengeluaran):
    #return False
#Jika sisa_anggaran menjadi negatif atau kita sudah mencoba semua pengeluaran (indeks >= len(pengeluaran)), maka kita hentikan pencarian karena kombinasi ini tidak valid.

#Mencoba Memasukkan Pengeluaran
#nama_item, biaya = pengeluaran[indeks]
#kombinasi_sekarang.append((nama_item, biaya))
#if cari_kombinasi(sisa_anggaran - biaya, indeks + 1, kombinasi_sekarang):
    #return True
    #Kita mengambil satu item pengeluaran dan mengurangkan biayanya dari sisa_anggaran. Jika dengan #memasukkan item ini kita berhasil menghabiskan anggaran, maka kita langsung kembali (return True).

#Backtracking: Membatalkan Pilihan jika Gagal
#kombinasi_sekarang.pop()
#return cari_kombinasi(sisa_anggaran, indeks + 1, kombinasi_sekarang)
#Jika ternyata menambahkan item sebelumnya tidak menghasilkan kombinasi yang tepat, kita membatalkan #
#pilihan (pop) dan mencoba opsi tanpa item tersebut.


#2. Pemilihan Kombinasi Terbaik
#Fungsi cari_kombinasi akan mencari kombinasi yang pertama kali ditemukan. Setelah itu, program menyesuaikan dengan menambahkan kategori kecil agar tidak ada sisa uang.

#for item in pengeluaran:
    #if sisa_uang >= item[1] and item not in solusi:
        #solusi.append(item)
        #sisa_uang -= item[1]
    #if sisa_uang == 0:
        #break

    #Jika setelah backtracking masih ada sisa uang, program akan menambahkan item kecil hingga anggaran habis tepat.  
#Kelebihan:
#Menemukan Solusi yang Tepat

#Backtracking memastikan bahwa kombinasi pengeluaran yang dihasilkan tepat mencapai 25 juta tanpa kelebihan atau kekurangan.
#Pendekatan Sistematis

#Algoritma mencoba semua kemungkinan kombinasi secara terstruktur dan terorganisir, sehingga tidak ada kombinasi yang terlewat.
#Tidak Perlu Sorting atau Preprocessing

#Pendekatan ini langsung bekerja pada daftar pengeluaran tanpa perlu mengurutkan atau melakukan perhitungan awal yang kompleks.
#Mudah Dimodifikasi

#Jika ada penyesuaian, seperti menambah kategori pengeluaran atau mengubah total anggaran, algoritma dapat langsung digunakan tanpa banyak perubahan.
#❌ Kekurangan:
#Kompleksitas Waktu Tinggi

#Pendekatan backtracking memiliki kompleksitas O(2ⁿ) dalam kasus terburuk, karena mencoba semua kombinasi kemungkinan. Jika jumlah item pengeluaran bertambah banyak, algoritma bisa menjadi lambat.
#Tidak Selalu Optimal

#Backtracking hanya mencari kombinasi pertama yang cocok, bukan yang paling optimal. Bisa jadi ada kombinasi lain yang lebih baik dalam hal pengalaman wisata, tetapi algoritma tidak mempertimbangkannya.
#Tidak Efisien untuk Anggaran Fleksibel

#Jika pengguna ingin solusi dengan margin toleransi (misal, maksimal sisa 100 ribu), backtracking tidak fleksibel karena hanya mencari solusi yang persis 25 juta.
#Tidak Mempertimbangkan Prioritas

#Semua pengeluaran dianggap setara, padahal mungkin ada kategori yang lebih diutamakan (misalnya, tiket pesawat lebih penting dibandingkan oleh-oleh). Algoritma tidak memiliki mekanisme prioritas.  