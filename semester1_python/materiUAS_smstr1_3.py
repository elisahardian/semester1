"""
## BUATLAH PROGRAM PYTHON YANG MENGGUNAKAN WHILE LOOP UNTUK MENCETAK SEMUA BIL GANJIL ANTARA 1 HINGGA 10
for i in range(1,11,2):
    print(i)
print()
i=1
while i <= 10:
    print(i)
    i += 2
print()
#jika bil ganjil tersebut dalam susunan terbalik
for i in range(9,0,-2):
    print(i)
print()
i=9
while i >=0:
    print(i)
    i -= 2
print()

## BUATLAH SEGITIGA PADA PYTHON
n=4
for i in range(1, n+1):
    print("* " *i)
print()
i=1
while i < 5:
    print("* " *i)
    i += 1
print()

#pada for
for i in range(0,4):
    print("* " *i)
for i in range(4,0,-1):
    print("* " *i)
print()
#pada while
i=1
while i <=3:
    print("* " *i)
    i+=1
i=4
while i >=1:
    print("* " *i)
    i-=1


## BUATLAH PROGRAM PYTHON YANG MEMINTA PENGGUNA UNTUK MEMASUKKAN SEBUAH ANGKA 
## ROGRAM TERSEBUT KEMUDIAN MENGGUNAKAN WHILE LOOP UNTUK MENCETAK TABEL PERKALIAN DARI ANGKA TERSEBUT HINGGA 10.

angka=int(input("masukkan angka untuk dikali 1 sampai 10: "))
i=1
while i <= 10:
    print(i, "x", angka, "=", i*angka)
    i+=1
print()
angka=int(input("masukkan angka untuk dikali 1 sampai 10: "))
for i in range(1, 11):
    hasil=i*angka
    print(f"{i} x {angka} = {hasil}")
print()

## TEBAKAN ANGKA: BUATLAH PROGRAM PYTHON YANG MENGHASILKAN SEBUAH ANGKA ACAK ANTARA 1 HINGGA 15. PROGRAM TERSEBUT KEMUDIAN MEMINTA PENGGUNA MENEBAK ANGKA TERSEBUT.
##GUNAKAN WHILE LOOP UNTUK MEMBERIKAN PETUNJUK DAN KESEMPATAN MENEBAK YANG TAK TERBATAS HINGGA PENGGUNA MENEBAK DENGAN BENAR.

percobaan=0
jawaban=8
while True:
    tebakan=int(input("masukkan angka tebakan anda: "))
    if jawaban == tebakan:
        print("tebakan anda benar! ")
        break
    elif tebakan < jawaban:
        print("tebakan anda terlalu kecil, coba lagi")
    else:
        print("tebakan anda terlalu besar, coba lagi") 
    percobaan+=1
print("anda berhasil menebak angka dalam", percobaan+1, "kali percobaan")

print()

## FAKTORIAL: BUATLAH PROGRAM PYTHON YG MEMINTA PENGGUNA UNTUK MEMASUKKAN SEBUAH ANGKA. PROGRAM TERSEBUT KEMUDIAN 
## MENGGUNAKAN WHILE LOOP UNTUK MENGHITUNG FAKTORIAL ANGKA TERSEBUT.

inputdata=int(input("masukkan data= "))
hasilfaktorial=1
for i in range(1, inputdata+1):
    hasilfaktorial*=i
print(f"faktorial dari {inputdata} adalah {hasilfaktorial}")
print()

n=int(input("masukkan angka: "))          
x=1
i=1
while i <= n:
    x=x*i
    i+=1
print(f"{n}! = {x}")
print()

## DERET FIBONANCCI: BUATLAH PROGRAM PYTHON YANG MENGGUNAKAN WHILE LOOP UNTUK MENCETAK DERET FIBONANCCI HINGGA SUKU KE 10. 
## DERET FIONANCCI DIMULAI DARI 0 DAN 1,DENGAN SETIAP SUKU BERJUMLAHKAN 2 SUKU SEBELUMNYA

max_range=10   #sampe 11 angka aja, (index ke 10)  
nilai1, nilai2 = 0,1 #kita define nilai awal fibonanci 0 , 1
print("hitung deret fibonancci")
print(nilai1, nilai2, end=" ")
i=2 #kita mulai dari index ke 2, pengulangan.. karena index ke 0 dan 1 udh didefine
while i <= max_range:
    nilai3=nilai2 + nilai1
    print(nilai3, end=" ")
    nilai1, nilai2 = nilai2, nilai3 #nilai 2 dan 3 akan dianggap sebagai nilai 1, 2,  dst.
    i += 1

print()

#cara lain dengan for loop
nilai1=0
nilai2=1
n=int(input("masukkan mau berapa panjang datanya? "))
lt=[0,1]
for i in range(0,n):
    nilai3=nilai1+nilai2
    nilai1,nilai2=nilai2,nilai3
    lt.append(nilai3)
print(lt)
print()

#cara lain dengan while loop
nilai1=0
nilai2=1
i=1
lt=[0,1]
n=int(input("masukkan mau berapa panjang datanya? "))
while i<=n:
    nilai3=nilai1+nilai2
    nilai1,nilai2=nilai2,nilai3
    lt.append(nilai3)
    i+=1
print(lt)
"""
