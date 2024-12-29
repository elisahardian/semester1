"""
## HARUS INSTALL MODUL PANDAS DULU KALO DI VSC

import pandas as pd
nama=['Nisa', 'Fira', 'Fadlur', 'Yahya', 'Vano']
upah=[1000, 2000, 1000, 3000, 4000]
jam_kerja=[8, 8, 8, 8, 8]
hari_kerja=[19, 20, 22, 18, 21]
dataframe={'Nama':nama, 'Upah':upah, 'Jam Kerja':jam_kerja, 'Hari Kerja':hari_kerja}
dataframe=pd.DataFrame(dataframe) #pd disini untuk mengubah data list menjadi data tabular seperti tabel
print(dataframe)
dataframe['Gaji']=0 #ini untuk membuat kolom gaji
for i in range(len(dataframe)):
    dataframe.at[i, 'Gaji']=dataframe.at[i, 'Upah']*dataframe.at[i, 'Jam Kerja']*dataframe.at[i, 'Hari Kerja']
    #perhitungan gaji hasil perkalian antara upah, jam kerja dan hari kerja
    #at sama seperti append, untuk menambah. at khusus di pandas
print(dataframe)

print()

import pandas as pd
matakuliah=['Kalkulus', 'Mtk Diskrit', 'Stat Prob', 'Algo Pemro', 'Agama', 'Inggris']
tugas=[97, 90, 95, 89, 85, 93]
uts=[90, 100, 97, 91, 76, 94]
uas=[95, 92, 95, 90, 89, 95]
dataframe={'Mata Kuliah':matakuliah, 'Tugas'=tugas, 'UTS':uts, 'UAS':uas}
dataframe=pd.DataFrame(dataframe)
print(dataframe)
dataframe['Nilai']=0
for i in range(len(dataframe)):
    dataframe.at[i, 'Nilai']=((0,3 * dataframe.at[i, 'Tugas'])+(0,3 * dataframe.at[i, 'UTS'])+(0,4 * dataframe.at[i, 'UAS']))
print(dataframe)
dataframe['Grade']=0
for i in range(len(dataframe)):
    if 80<= dataframe.at[i, 'Nilai'] <=100:
        dataframe[i, 'Grade']='A'
    elif 65<= dataframe.at[i, 'Nilai'] <=79:
        dataframe[i, 'Grade']='B'
    elif 40<= dataframe.at[i, 'Nilai'] <=64:
        dataframe[i, 'Grade']='C'
    else:
        dataframe[i, 'Grade']='D'
print(dataframe)
"""
"""
## PROCEDUR
def cetak(namadepan, namatengah, namabelakang):
    print("Nama Depan: ", namadepan)
    print("Nama Tengah: ", namatengah)
    print("Nama Belakang: ", namabelakang)
cetak("Takezo", "Kenzei", "Musashi")

def operasi(a,b):
    print(a+b)
operasi(18,2)

def my_function(food):
    for x in food:
        print(x)
food=['apple', 'banana', 'cherry']
my_function(food)

def my_function(food):
    for x in food:
        print(x)
fruits=['apple', 'banana', 'cherry']
my_function(fruits)

def my_functions(child3, child1, child2):
    print("isi parameter child1: ", child1)
    print("isi parameter child2: ", child2)
    print("isi parameter child3: ", child3)
my_functions('linus', 'emil', 'tobias')

def my_functions(child3, child1, child2):
    print("isi parameter child1: ", child1)
    print("isi parameter child2: ", child2)
    print("isi parameter child3: ", child3)
my_functions(child1='emil', child2='tobias', child3='linus')

def fungsi(*child): # ARBITRARY ARGUMENTS. tanda * digunakan untuk parameter yang tidak diketahui dengan pasti jumlahnya
    for x in child:
        print("nama anak:", x)
print("3 arguments/parameter")
fungsi("emil", "tobias", "linus")
print("5 arguments/parameter")
fungsi("emil", "tobias", "linus", "nobita", "naruto")

def my_function(**mobil): # ARBITRARY KEYWORDS ARGUMENTS. tanda ** digunakan jika parameter tidak diketahui jumlahnya dan ada sangkutpautnya dengan nama key
    print("merek mobil: ", mobil["merek"])
    print("jenis mobil: ", mobil["tipe"])
    print("harga mobil: ", mobil["harga"])
print("2 arguments")
my_function(merek="nissan", tipe="matic", harga="300000000")
 
def my_function(merek, tipe, harga): #bisa juga seperti ini tanpa arbitrary keywords arguments
    print("merek mobil: ", merek)
    print("jenis mobil: ", tipe)
    print("harga mobil: ", harga)
print("2 arguments")
my_function("nissan", "matic","300000000")

def my_functions(**mobil):
    i=0
    for z in mobil.keys():
        i+=1
        print("data mobil [",i,"]-",z,":", mobil[z])
print("2 arguments")
my_functions(merek="nissan", tipe="sedan")
print("4 arguments")
my_functions(merek="nissan", tipe="hatchback", cc=1200, transmisi="matic")


## FUNCTION

def contoh():
    return 100
a=contoh()
print(a)

def contoh(b):
    if b%2==0:
        return "genap"
    return "ganjil"
a=contoh(101)
print(a)

def contoh(b):
    if b%2==0:
        return "genap"
a=contoh(101)
print(a) #yg ini hasilnya akan "none" karena tidak ada yg "else"nya,tidak ada return nya lagi

def contoh(b):
    if b%2==0:
        return "genap"
    else:
        return "ganjil"
a=contoh(101)
print(a)
c=contoh(100)
print(c)

def f_hitung():
    hasil =5+7
    return hasil
f_hitung() #ini pemanggilan fungsi yg sudah dibikin diatasnya. hasil yg ini akan bisa dioperasikan dengan yg lain karena ada return
a=f_hitung() #hasil fungsi tersebut kita misalkan dulu dengan variable
print(a*2)

def operasi(a, b):
    return (a+b)
hasil=operasi(2,18)
print(hasil)
print(hasil+5) #hasilnya bisa dioperasikan lagi karena merupakan function

def operasiarray(a): #variable disini "a"
    return a[0]+a[3]+a[4]
a=[0,20,30,40,50] #sama variabel disini "a", bisa sama bisa ngga. TAPI YG DISINI
print(operasiarray(a)) #sama variabel disini "a" bisa sama bisa ngga. SAMA YG DISINI HARUS SAMA

def contoh(b):
    if 80<b<=100:
        return "A"
    elif 65<b<=80:
        return "B"
    elif 40<=b<=65:
        return "C"
    else:
        return "D"
a=int(input("masukkan nilai anda: "))
print(contoh(a))

def contoh(b):
    if b%2==0:
        return "genap"
    else:
        return "ganjil"
a=int(input("masukkan angka: "))
print(contoh(a))

def nilai(a,b,c):
    hit=((0.3*a)+(0.3*b)+(0.4*c))
    if 80<=hit<=100:
        return "A"
    elif 65<=hit<80:
        return "B"
    elif 40<=hit<65:
        return "C"
    else:
        return "D"
a=int(input("masukkan nilai tugas anda: "))
b=int(input("masukkan nilai UTS anda: "))
c=int(input("masukkan nilai UAS anda: "))
print(nilai(a,b,c))

#PROGRAM UNTUK MENGHITUNG DERET 2A+1
#jika diminta masukkan a=2, dan output nya [5,7,9]
def contoh(a):
    lt= [] # lt berupa list kosong
    for i in range(a, a+3): # sampe a+3 karena hasilnya diminta ada 3 yaitu 5,7,9
        hitung=2 * a + 1
        lt.append(hitung) #hasil perhitungan akan ditambah ke lt
        a += 1
    return lt
a=int(input("masukkan nilai a: "))
print(contoh(a))

#PROGRAM JIKA OUTPUTNYA BAYAR LEBIH DARI RP 50.000 GUNAKAN QRIS. SELAIN ITU CASH
def bayar():
    if a>=50000:
        return "gunakan QRIS"
    else: 
        return "gunkan cash"
a=int(input("masukkan total pembayaran anda: "))
print(bayar())

#PROGRAM PENYELESAIAN AKAR
def akar():
    hitung=a**(m/n)
    return hitung
a=int(input("masukkan angka utamanya: "))
m=int(input("masukkan pangkat angka utamanya: "))
n=int(input("masukkan pangkat akarnya: "))
print(akar())

#PROGRAM LIST ARRAY: [1,2,3,4,5].. JIKA INPUT "GENAP", OUTPUT 2,4. JIKA "GANJIL", OUTPUT 1,3,5 

def fungsi2(a):
    lt=[1,2,3,4,5]
    if a== "Genap":
        return [2,4]
    elif a== "genap":
        return [2,4]
    elif a== "Ganjil":
        return [1,3,5]
    elif a== "ganjil":
        return [1,3,5]
    else:
        return "invalid syntax"
b=str(input("genap/ganjil? "))
print(fungsi2(b))

def fungsi2():
    lt=[1,2,3,4,5]
    if a== "genap":
        return lt[1], lt[3]
    elif a== "ganjil":
        return lt[0], lt[2], lt[4]
    else:
        return "invalid syntax"
a=str(input("genap/ganjil? "))
print(fungsi2())


#PROGRAM MENGHITUNG LUAS SEGITIGA DAN LINGKARAN. JIKA PILIH "SEGITIGA", LUAS SEGITIGA SEBAGAI OUTPUT
def luas(a):
    if a=="segitiga":
        return "luas=alas*tinggi/2"
    elif a=="lingkaran":
        return "luas=3.14*r*r"
    else:
        return "invalid syntax"
a=str(input("segitiga atau lingkaran? "))
print(luas(a))

def luas(a):
    if a=="segitiga":
        alas=int(input("masukkan alas: "))
        tinggi=int(input("masukkan tinggi: "))
        hitung=alas*tinggi/2
        return hitung
    elif a=="lingkaran":
        r=int(input("masukkan jari-jari: "))
        hitung=3.14*r*r
        return hitung
    else:
        return "invalid syntax"
a=str(input("segitiga atau lingkaran? "))
print(luas(a))

"""
