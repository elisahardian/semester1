"""
a=int(input("masukkan angka: "))
match a:
    case 9:
        print("sembilan")
    case 8:
        print("delapan")
    case _:
        print("tak dikenal")
print()
def cetak(nama_depan, nama_tengah, nama_belakang):
    print("nama depan: ", nama_depan)
    print("nama tengah: ", nama_tengah)
    print("nama belakang: ", nama_belakang)
    print("nama anda: ", nama_depan ," ", nama_tengah, " ",nama_belakang)
cetak("takezi", "kenxo", "musashi")
print()
def operasi(a,b):
    hasil=a+b
    print(hasil)
operasi(10,2)
print()
def fungsi(buah):
    for x in buah:
        print(x)
buah=['apel', 'jeruk', 'mangga']
fungsi(buah)

def fungsi(anak1, anak2, anak3):
    print("anak1= ", anak1)
    print("anak2= ", anak2)
    print("anak3= ", anak3)
fungsi('takezi', 'linus', 'tobias')
print()

def fungsi(anak):
    for x in anak:
        print(x)
anak=['tobias', 'linus', 'kenzo']
fungsi(anak)
print()

def fungsi(anak1, anak2, anak3):
    print("anak1= ", anak1)
    print("anak2= ", anak2)
    print("anak3= ", anak3)
fungsi(anak3='takezi', anak1='linus', anak2='tobias')

def fungsi(*anak):
    for x in anak:
        print(x)
fungsi("anak1", 'anak2', 'anak3', 'anak4', 'anak5')

def fungsi(**mobil):
    print("mobil merek: ", mobil['merek'])
    print("mobil tipe: ", mobil['tipe'])
fungsi(merek='toyota', tipe='s')

def contoh():
    return 100
a=contoh()
print(a)

def contoh(b):
    if b%2==0:
        return "genap"
    return "ganjil"
b=int(input("b= "))
x=contoh(b)
print(x)

def contoh(b):
    if b%2==0:
        return "genap"
    return "ganjil"
a=contoh(101)
print(a)
b=contoh(100)
print(b)

def operasi(a,b):
    return a+b
a=operasi(2,9)
print(a)
print(a+1)

def nilai(a,b,c):
    total=(0.3*a)+(0.3*b)+(0.4*c)
    if 80<=total<=100:
        return "A"
    elif 65<=total<80:
        return "B"
    elif 50<=total<65:
        return "C"
    else:
        return "D"
a=int(input("masukkan nilai tugas: "))
b=int(input("masukkan nilai uts: "))
c=int(input("masukkan nilai uas: "))
x=nilai(a,b,c)
print(x)

#deret 2a+1. a=2. hasilnya [5,7,9]
a=int(input("masukkan a= "))
def fungsi(a):
    lt=[]
    for x in range(a, a+3):
        hit=2*a+1
        lt.append(hit)
        a+=1
    return lt
print(fungsi(a))

a=int(input("masukkan total pembayaran anda: "))
def bayar(a):
    if a>=50000:
        return "bayar pakai qris"
    else:
        return "pakai cash ya"
print(bayar(a))

#penyelesaian akar
a=int(input("masukkan angka utama: "))
m=int(input("masukkan pangkat dari angka utama: "))
n=int(input("masukkan akar dari pangkat: "))
def akar(a,m,n):
    hasil=a**(m/n)
    return hasil
print(akar(a,m,n))

#[1,2,3,4,5]. genap output 2,4, ganjil output 1,3,5
def fungsi():
    lt=[1,2,3,4,5]
    if a=="genap":
        return lt[1],lt[3]
    elif a=="ganjil":
        return lt[0], lt[2], lt[4]
    else:
        return "sepertinya anda salah"
a=str(input("masukkan ganjil/genap? "))
print(fungsi())
"""

#luas segitiga atau luas lingkaran
def luas(a):
    if minta=="lingkaran":
        jari=int(input("jari jari lingkaran: "))
        luas=jari*jari*3.14
        return "luas=jari x jari x 3.14 =", luas
    elif minta=="segitiga":
        alas=int(input("masukkan alas segitiga: "))
        tinggi=int(input("masukkan tinggi segitiga: "))
        luas=0.5*alas*tinggi
        return "luas=0.5 x alas x tinggi =", luas
    else:
        return "sepertinya anda salah"
minta=str(input("segitiga/lingkaran? "))
print(luas(minta))
