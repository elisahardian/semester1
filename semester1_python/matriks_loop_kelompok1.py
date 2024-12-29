## FOR LOOP PERKALIAN MATRIKS (matriks n kali matriks n)
# #Input matriks pertama
# n=int(input("masukan matriks berapa kali berapa: "))
# matriks1 = []
# print("input kolom-kolom matriks1:")
# for i in range(n):
#     baris = []
#     for j in range(n):
#         kolom = int(input(f"input kolom matriks1 pada baris {i+1} kolom {j+1}: "))
#         baris.append(kolom)
#     matriks1.append(baris)

# #Input matriks kedua
# matriks2 = []
# print("input kolom-kolom matriks2:")
# for i in range(n):
#     baris = []
#     for j in range(n):
#         kolom = int(input(f"input kolom matriks2 pada baris {i+1} kolom {j+1}: "))
#         baris.append(kolom)
#     matriks2.append(baris)

# #Inisialisasi matriks hasil perkalian
# hasil = [[0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0]]

# #Perkalian matriks
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             hasil[i][j] += matriks1[i][k] * matriks2[k][j]

# #Menampilkan hasil perkalian
# print("Hasil perkalian matriks:")
# for i in range(n):
#     for j in range(n):
#         print(hasil[i][j], end=" ")
#     print()


# print()

# ## WHILE LOOP PERKALIAN MATRIKS (matriks n kali matriks n)
n=int(input("masukkan matriks berapa kali berapa: "))
print("masukkan elemen matriks pertama: ")
matriks1 = []
i = 0 
while i < n : 
    baris1 = []
    j = 0
    while j < n : 
        kolom1 = int(input(f'baris {i+1}, kolom {j+1}= '))
        j+= 1 
        baris1.append(kolom1)
    i += 1 
    matriks1.append(baris1)
print("masukkan elemen matriks kedua: ")
matriks2 = []
i = 0 
while i < n : 
    baris2 = []
    j = 0
    while j < n : 
        kolom2 = int(input(f'baris {i+1}, kolom {j+1}= '))
        j+= 1
        baris2.append(kolom2) 
    i += 1 
    matriks2.append(baris2)
hasil = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
i = 0
while i < n :
    j = 0  
    while j < n :
        k = 0 
        while k < n : 
            hasil[i][j] += matriks1[i][k] * matriks2[k][j]
            k += 1 
        j += 1
    i += 1 
print("hasil perkalian matriks: ")
i = 0
while i < n : 
    j = 0 
    while j < n : 
        print(hasil[i][j], end= ' ') 
        j += 1 
    print('')
    i += 1 
