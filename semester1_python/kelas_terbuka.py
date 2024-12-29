#prosedur= langkah langkah untuk melakukan sesuatu. contoh= luas=panjang*lebar
#fungsi adalah tempat untuk menaruh prosedurnya
#fungsi dengan parameter dan fungsi tanpa parameter. parameter untuk membatasi mana yang akan digunakan (biasanya menggunakan (variable)). fungsi tanpa variable akan ()
#return= hasil akhir yang akan dikeluarkan dalam fungsi. jika tidak pakai return akan tidak ada hasil (walaupun fungsinya bisa jalan)

#FUNGSI TANPA PARAMETER
"""
alas=8
tinggi=10
def luas_segitiga():       #fungsi
    luas=0.5*alas*tinggi         #prosedur
    print("luasnya adalah: ", luas)
    return luas_segitiga
luas_segitiga()          #pemanggilan fungsi
"""

"""
#FUNGSI DENGAN PARAMETER

alas1=8
tinggi1=10
alas2=5
tinggi2=6
def luas_segitiga(alas, tinggi):       #fungsi dengan parameter
    luas=0.5*alas*tinggi         #prosedur
    print("luasnya adalah: ", luas)
    return luas_segitiga
luas_segitiga(alas1, tinggi1)          #pemanggilan fungsi dengan parameter
luas_segitiga(alas2, tinggi2)
"""

"""
#LATIHAN FUNGSI TANPA PARAMETER

r=7
def luas_lingkaran():
    luas=22/7*r*r
    print("luas lingkaran adalah: ", luas)
    return luas_lingkaran
luas_lingkaran()
"""

"""
#LATIHAN FUNGSI DENGAN PARAMETER DAN MEMINTA INPUT DARI USER
#input dan print tidak bisa satu baris.. karena input membutuhkan tempat penyimpanan dahulu yaitu variabel. baru kita bisa memprint nilai variable tersebut

alas1= float(input("masukkan alas pertama: "))        #meminta input dari user
print("alas pertama: ", alas1)
tinggi1= float(input("masukkan tinggi pertama: "))
print("tinggi pertama: ", tinggi1)
alas2= float(input("masukkan alas kedua: "))
print("alas kedua: ", alas2)
tinggi2= float(input("masukkan tinggi kedua: "))
print("tinggi kedua: ", tinggi2)

def luas_segitiga(alas, tinggi):       #fungsi dengan parameter
    luas=0.5*alas*tinggi         #prosedur
    print("luasnya adalah: ", luas)
    return luas_segitiga
luas_segitiga(alas1, tinggi1)          #pemanggilan fungsi dengan parameter
luas_segitiga(alas2, tinggi2)
"""

#LOOPING (pengulangan)
#ada for loop samam while loop. for loop akan terus berjalan sampai suatu kondisi terpenuhi. while loop akan terus berjalan ?
"""
for i in  range (10):       #print akan diulang 10 kali
    print(i)
"""
"""
x=8
y=5

for i in  range (y):       #print akan diulang y kali. bisa juga langsung ditulis dengan angka
    print(x)
    x=x*2           #setiap x akan dikali 2
"""
"""
x=int(input("mau dimulai dari angka berapa? "))
y=int(input("mau diulang berapa kali? "))

for i in  range (y):       #print akan diulang y kali. bisa juga langsung ditulis dengan angka
    print(x)
    x=x+5
"""

"""
#bikin fungsi trus bikin fungsi volume kubus ditambah limas. minta input dar user

#volume kubus, sisi**3
sisi=float(input("masukkan sisi kubus: "))
print(sisi)

def volume_kubus(sisi):
    volume_kubus= sisi**3
    return volume_kubus

#volume limas 1/3*alas*tinggi
alas=float(input("masukkan alas limas: "))
print(alas)
tinggi=float(input("masukkan tinggi limas: "))
print(tinggi)

def volume_limas(alas, tinggi):
    volume_limas= 1/3*alas*tinggi
    return volume_limas

z= volume_kubus(sisi) + volume_limas(alas, tinggi)
print("jadi jumlah volume kubus dan volume limas adalah ", z)
"""
