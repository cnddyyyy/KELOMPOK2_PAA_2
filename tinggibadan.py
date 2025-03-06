# KELOMPOK 2 (ALGORITMA QUICKSORT : TINGGI BADAN)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Data tinggi badan sudah diberikan
tinggi_badan = [160, 165, 170, 155, 180, 175, 168, 172, 158, 182,
                159, 177, 166, 169, 174, 167, 178, 161, 163, 171]

# Menampilkan data sebelum diurutkan
print("\nData tinggi badan sebelum diurutkan:", tinggi_badan)

# Mengurutkan tinggi badan
hasil_sorting = quick_sort(tinggi_badan)

# Menampilkan hasil setelah diurutkan
print("Tinggi badan setelah diurutkan:", hasil_sorting)
