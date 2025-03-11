
import time
import random

def sum_n(prices):
    total = 0
    for price in prices:
        total += price
    return total

# Membuat daftar harga dengan 1000 elemen secara acak antara 1000 hingga 50000
prices = [random.randint(1000, 50000) for _ in range(1000000)]

# Mengukur waktu eksekusi
start_time = time.time()
total = sum_n(prices)
end_time = time.time()

# Output hasil perhitungan dan waktu eksekusi
print(f"Total belanja: {total}")
print(f"Waktu eksekusi: {end_time - start_time:.10f} detik")

# Menurut Saya , Setelah saya buat dengan uji coba range data 1juta maka O(log n) lebih lambat
# dibandingkan
# Dengan O(n) ,  begitu juga dengan O(n^2) Lebih lambat lagi dibandingkan dengan O(Log  n)


