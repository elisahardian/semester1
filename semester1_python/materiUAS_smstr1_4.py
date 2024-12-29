## SELEKSI 
"""
#ONE WAY SELECTION
a=int(input("masukkan bilangan a: "))
if a%2==0:
   print("bilangan", a, "adalah bil genap")

b=int(input("masukkan bilangan  b: "))
if b%2 !=0: print("bilangan", b, "adalah bil ganjil")

pasw = str(input("masukkan password: "))
if pasw=="aling":
   print("selamat datang aling")

#TWO WAY SELECTION 
a=int(input("masukkan bilangan a: "))
if a%2==0:
   print("bilangan", a, "adalah bil genap")
else:
   print("bilangan", a, "bukan genap")

b=int(input("masukkan bilangan  b: "))
print("bilangan", b, "adalah bil ganjil") if b%2 !=0 else print("bilangan", a,"adalah bil genap")

#TRY-EXCEPTION
print("sebelum terjadinya kesalahan")
print(x)
print("baris ini tidak dieksekusi jika terjadi kesalahan diatasnya")

try:
    print("baris sebelum terjadinya kesalahan")
    print(x)
    print("bar ini tidak dieksekusi karena terjadi kesalahan diatasnya")
except:
    print("except terjadi karema x belum ada")

x=100
try:
    print("baris sebelum terjadinya kesalahan")
    print(x)
    print("baris ini dieksekusi karena tidak terjadi kesalahan diatasnya")
except:
    print("except terjadi karena x belum ada")
else:
    print("semua perintah pada try berhasil dieksekusi karena tidak ada kesalahan")

x=100
try:
    print("baris sebelum terjadinya kesalahan")
    print(x)
    print("baris ini dieksekusi karena tidak terjadi kesalahan diatasnya")
finally:
    print("baris finally dicetak tanpa kondisi apapun")

a=str(input("masukkan nilai string:(lapar/tidak)? "))
b=int(input("masukkan berapa siswa: "))
if a=="lapar" and b>=10:
    print("boleh istirahat kekantin")
else:
    print("ayo lanjut belajar lagi")

## SELESKSI BERSARANG
#IF BERSARANG PADA THEN
print("program mencari bilangan yang paling besar")
a=int(input("masukkan bilangan a: "))
b=int(input("masukkan bilangan b: "))
c=int(input("masukkan bilangan c: "))
if (a>b):
    if (a>c):
        print(f"maka nilai {a} adalah yang paling besar")
if (b>c):
    if (b>a):
        print(f"maka nilai {b} adalah yang paling besar")
else:
    print(f"maka nilai {c} adalah yang paling besar")

#IF BERSARANG PADA THEN DAN ELSE
print("rencana setelah lulus sekolah? \n1.kuliah\n2.kerja")
jawaban= int(input("masukkan jawaban anda: "))
if (jawaban == 1):
    print("kuliah jurusan apa?\n1.teknik informatika\n2.sistem informasi")
    jurusan= int(input("masukkan nomor jurusan anda: "))
    if (jurusan == 1):
        print("ohh kuliah teknik informatika")
    else:
        print("ohhh sistem informasi toh")
else:
    print("kerja diindustri apa?\n1.tambang\n2.interspace")
    kerja= int(input("masukkan nomor pekerjaan anda: "))
    if (kerja == 1):
        print("ohhh di pertambangan")
    else:
        print("wahh keren banget luar angkasa gitu")

## SWITCH CASE
a=int(input("input bilangan a: "))
match a:
    case 1:
        print("satu")
    case 2:
        print("dua")
    case 3:
        print("tiga")
    case _: # _ untuk opsi default
        print("tidak kenal") 


## IF- ELIF
a=int(input("input bilangan a: "))
if a==1:
    print("satu")
elif a==2:
    print("dua")
elif a==3:
    print("tiga")
else:
    print("tidak dikenal") 
"""