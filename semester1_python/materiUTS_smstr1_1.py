"""
print("hello world")
print("parameter1", "parameter2", 100, 899)
#ini comentar tidak tereksekusi

#======PROGRAM LUAS LINGKARAN======
phi=22/7
r=7
print("luas lingkaran: ", phi*r*r)
jari_jari=int(input("masukkan jari-jari: "))
phi=22/7
print("luas lingkaran: ", phi*jari_jari*jari_jari)

#======PROGRAM LUAS PERMUKAAN BALOK======
panjang=int(input("masukkan panjang balok: "))
lebar=int(input("masukkan lebar balok: "))
tinggi=int(input("masukkan tinggi balok: "))
print("panjang: ", panjang, "; lebar: ", lebar, "; tinggi: ", tinggi)
print("luas permukaan balokk adalah: ", 2*((panjang*lebar)+(panjang*tinggi)+(lebar*tinggi)))

#======PROGRAM LUAS TRAPESIUM======
alasatas=float(input("masukkan alas atas: "))
alasbawah=float(input("masukkan alas bawah: "))
tinggi=float(input("masukkan tinggi: "))
luas=0.5*(alasatas + alasbawah)*tinggi
print("luas trapesium adalah: ", luas)

#======TIPE DATA======
a=int(input("masukkan angka pertama: "))
b=int(input("masukkan angka kedua: "))
print("hasil penjumlahannya adalah: ", a+b) #hasil akan integer, hasil akan dijumlahkan
p=input("masukkan apapun 1: ")
q=input("masukkan apapun 2: ")
print("hasil penjumlahannya: ", p+q) #hasil akan string, hasil akan digabungkan

nama=input("namanya siapa? ")
print("oh halloo ", nama)
umur=int(input("umur berapa? "))
print("ohh umur", umur, "tahun")

x="hello world"
print(x, ", tipe datanya: ", type(x))
x=20
print(x, ", tipe datanya: ", type(x))
x=67.98
print(x, ", tipe datanya: ", type(x))
x=1j
print(x, ", tipe datanya: ", type(x))
x=["apel", "pisang", "nanas", "semangka"]
print(x, ", tipe datanya: ", type(x))
x=("apel", "pisang", "nanas", "semangka")
print(x, ", tipe datanya: ", type(x))
x={"apel", "pisang", "nanas", "semangka"}
print(x, ", tipe datanya: ", type(x))
x=frozenset({"apel", "pisang", "nanas", "semangka"})
print(x, ", tipe datanya: ", type(x))
x=range(6)
print(x, ", tipe datanya: ", type(x))
x=True
print(x, ", tipe datanya: ", type(x))
x=b"hello"
print(x, ", tipe datanya: ", type(x))
x=bytearray(5)
print(x, ", tipe datanya: ", type(x))
x=memoryview(bytes(5))
print(x, ", tipe datanya: ", type(x))
x=None
print(x, ", tipe datanya: ", type(x))

#======CASTING======
x=int(8.33)
y=int("71")
z=int(2)
print(x, y, z, type(x), type(y), type(z))
p=float(98)
q=float(23.81)
r=float("877")
print(p, q, r, type(p), type(q), type(r))
a=str(87)
b=str(54.38)
c=str("helllo")
print(a, b, c, type(a), type(b), type(c))

#======LIST, TUPLE, SET======
tinggi=[170, 165, 172]
berat=[70, 71, 65]
datalist=["z", 2, 0.5]
print("tipe data tinggi: ", type(tinggi), ",tipe data berat: ", type(berat), ",tipe data data list: ", type(datalist))
print(tinggi+berat)
a=datalist[0]
print(a)
print(datalist[0], ",type data list index ke 0:", type(datalist[0]))
jumlahlist=[berat[0]+tinggi[0], berat[1]+tinggi[1], berat[2]+tinggi[2]]
print(jumlahlist, ", type datanya ", type(jumlahlist))
jumlahtuple=(berat[0]+tinggi[0], berat[1]+tinggi[1], berat[2]+tinggi[2])
print(jumlahtuple, ", type datanya ", type(jumlahtuple))
jumlahset={berat[0]+tinggi[0], berat[1]+tinggi[1], berat[2]+tinggi[2]}
print(jumlahset, ", type datanya ", type(jumlahset))

tinggi[0]=172
tinggi[2]=170
print("data tinggi setelah diubah: ", tinggi)
berat[1]=98
print("data berat setelah diubah: ", berat)

#======PERTAMBAHAN, PENGURANGAN DAN PERKALIAN MATRIKS======
a=[[1,2],
   [2,1]]
b=[[-1,1],
   [0,1]]
tambah=[[a[0][0]+b[0][0], a[0][1]+b[0][1]],
        [a[1][0]+b[1][0], a[1][1]+b[1][1]]]
kurang=[[a[0][0]-b[0][0], a[0][1]-b[0][1]],
        [a[1][0]-b[1][0], a[1][1]-b[1][1]]]
print("hasil kedua matriks ditambah adalah: ", tambah, ", hasil kedua matriks dikurang adalah: ", kurang)

a=[[1,2],
   [4,3]]
b=[[0,-2],
   [-1,5]]
perkalian=[[(a[0][0]*b[0][0])+(a[0][1]*b[1][0]),(a[0][0]*b[0][1])+(a[0][1]*b[1][1])],
           [(a[1][0]*b[0][0])+(a[1][1]*b[1][0]),(a[1][0]*b[0][1])+(a[1][1]*b[1][1])]]
print("perkalian 2 matriks: ", perkalian)

#======FUNGSI======
#fungsi tanpa parameter
alas=8
tinggi=2
def luas_segitiga():
    luas=0.5*alas*tinggi
    print("luas segitiga adalah: ", luas)
    return luas
luas_segitiga()
#fungsi dengan parameter
alas1=8
tinggi1=10
alas2=3
tinggi2=5
def luas_segitiga(alas, tinggi):
    luas=0.5*alas*tinggi
    print("luas segitiga adalah: ", luas)
    return luas
luas_segitiga(5,2)
luas_segitiga(alas1, tinggi2)
luas_segitiga(alas2, tinggi2)

#======LOOPING======
for i in range(10):
    print(i, end=" ")
print()    

x=8
y=5
for fi in range(y):
    print(x)
    x+=2

a=int(input("masukkan batas awal: "))
b=int(input("masukkan batas akhir: "))
for i in range(a,b):
    print(i)

#======LIST DAN TUPLE======
dtlist1=[4,9,15,12]
dtlist2=[1,2,3,4,5,6,7,8]
print("panjang list 1: ", len(dtlist1), "; panjang list 2: ", len(dtlist2))
print("nilai maks dari dtlist 1: ", max(dtlist1), "; nilai min dari dtlist 2: ", min(dtlist2))
print(1 in dtlist1)
print(8 in dtlist2)
print(sum(dtlist2))
dtlist1.append(67)
print(dtlist1)
dtlist2.insert(3,888)
print(dtlist2)
print(dtlist1[0:2])
print(dtlist2[4:8])
print(dtlist1[:])

tuple_buah=('pisang', 'nanas', 'melon', 'durian')
print(tuple_buah[0:2])
print(tuple_buah[1:3])

#======SELECTION======
a=int(input("tebak sebuah angka: "))
if a==9:
    print("betull angka 9 jawabannya")
elif a<9:
    print("coba angka yang lebih besar lagi")
else:
    print("coba angka yang lebih kecil")
"""