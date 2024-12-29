"""
#PASSWORD
password=str(input("setting password anda: "))
while True:
    tebakan=str(input("masukkan password anda: "))
    if password==tebakan:
        print("selamat datang! ")
        break
    else:
        print("password anda salah, coba lagi! ")
"""
"""
n=int(input("masukkan n= "))
i=0
while i<=10:
    print(f"{i}x{n}= {i*n}")
    i+=1

n=int(input("masukkan n= "))
for i in range(0,11):
    print(f"{i}x{n}= {i*n}")
"""
"""
jawaban=2
percobaan=0
while True:
    tebakan=int(input("masukkan angka tebakan anda (1-15): "))
    if jawaban==tebakan:
        print("TEBAKAN BENAR")
        break
    elif tebakan < jawaban:
        print("tebakan anda terlalu kecil. coba lagi! ")
        percobaan+=1
    else:
        print("tebakan anda terlalu besar. coba lagi! ")
        percobaan +=1
print("anda berhasil menebak dalam", percobaan+1, "kali percobaan")
"""
"""
#faktorial
n=int(input("masukkan n= "))
hit=1
i=1
while i<=n:
    hit=hit*i
    i+=1
print("faktorial dari", n, "adalah", hit)
"""
"""
#deret fbonanci 0 1 1 2 3 5 8 13 21 34 55 while loop
i=0
nilai1=0
nilai2=1
lt=[0,1]
while i<=10:
    nilai3=nilai1+nilai2
    nilai1, nilai2= nilai2, nilai3
    lt.append(nilai3)
    i+=1
print(lt)
"""
"""
a=int(input("masukkan bilangan a: "))
if a%2==0:
    print(a,"merupakan bilangan genap")
else:
    print(a,"merupakan bilangan ganjil")
"""
"""
#paket belanja murah 2 barang
#smj=200.000
#motoraki=1.000.000
#bola=20.000
#tamia=30.000
print("daftar mainan
      -smj
      -bola
      -tamia
      -motor aki")
hari=str(input("sekarang hari apa? "))
for i in range(10):
    if hari=="minggu":
        print("HARI INI KAMI TUTUP")
        break

    a=str(input("masukkan nama belanjaan pertama anda: "))
    b=str(input("masukkan nama belanjaan kedua anda: "))

    total_belanja=0
    if a=="smj" and b=="motor aki":
        print("total belanja anda adalah 1.200.000")
        total_belanja=1200000
    elif a=="motor aki" and b=="smj":
        print("total belanja anda adalah 1.200.000")
        total_belanja=1200000
    elif a=="smj" and b=="bola":
        print("total belanja anda adalah 220.000")
        total_belanja=220000
    elif a=="bola" and b=="smj":
        print("total belanja anda adalah 220.000")
        total_belanja=220000
    elif a=="smj" and b=="tamia":
        print("total belanja anda adalah 230.000")
        total_belanja=230000
    elif a=="tamia" and b=="smj":
        print("total belanja anda adalah 230.000")
        total_belanja=230000
    elif a=="motor aki" and b=="bola":
        print("total belanja anda adalah 1.020.000")
        total_belanja=1020000
    elif a=="bola" and b=="motor aki":
        print("total belanja anda adalah 1.020.000")
        total_belanja=1020000
    else:
        print("pesanan anda tidak ada didaftar")
    print()

    if hari=="senin":
        diskon=0.1*total_belanja
        total=total_belanja-diskon
        print("dengan diskon sebesar", diskon, "total belanjaan menjadi", total)
    elif hari=="selasa":
        diskon=0.2*total_belanja
        total=total_belanja-diskon
        print("dengan diskon sebesar", diskon, "total belanjaan menjadi", total)
    elif hari=="rabu":
        diskon=0.1*total_belanja
        total=total_belanja-diskon
        print("dengan diskon sebesar", diskon, "total belanjaan menjadi", total)
    elif hari=="kamis":
        diskon=0.2*total_belanja
        total=total_belanja-diskon
        print("dengan diskon sebesar", diskon, "total belanjaan menjadi", total)
    elif hari=="jumat":
        diskon=0.1*total_belanja
        total=total_belanja-diskon
        print("dengan diskon sebesar", diskon, "total belanjaan menjadi", total)
    elif hari=="sabtu":
        diskon=0.3*total_belanja
        total=total_belanja-diskon
        print("dengan diskon sebesar", diskon, "total belanjaan menjadi", total)
    else:
        print("HARI INI KAMI TUTUP")
print("terimakasih sudah berbelanja")
"""

#soal
print("UJIAN AKHIR SEMESTER")
nama=str(input("masukkan nama anda: "))
skor=0
print(f"""1. Ada berapa macam pengulangan pada Unpredicted Loop? 
      a.1
      b.2
      c.3""")
jawab1=str(input("a/b/c? "))
if jawab1=="b":
    print("BENAR")
    skor+=1
else:
    print("SALAH")
print(f"""2. Perbedaan function dan Procedure? 
      a.function ada return
      b.procedure ada return
      c.keduanya sama tidak ada bedanya""")
jawab2=str(input("a/b/c? "))
if jawab2=="a":
    print("BENAR")
    skor+=1
else:
    print("SALAH")
print(f"""3. Apa itu Switch Case?
      a.matriks
      b.pengulangan
      c.seleksi""")
jawab3=str(input("a/b/c? "))
if jawab3=="c":
    print("BENAR")
    skor+=1
else:
    print("SALAH")
print(f"""4. Hasilnya masih bisa dioperasikan lagi? 
      a.procedure
      b.function
      c.one way selection""")
jawab4=str(input("a/b/c? "))
if jawab4=="b":
    print("BENAR")
    skor+=1
else:
    print("SALAH")

nilai=25*skor
print(f"""skor {nama}: {skor} ,nilai {nama}: {nilai}""")
if 80<=nilai<=100:
    print("grade: A")
elif 60<=nilai<80:
    print("grade: B")
elif 40<=nilai<60:
    print("grade: C")
else:
    print("grade: D")
