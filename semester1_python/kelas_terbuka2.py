"""
nama=input("nama anda adalah: ")
print("hallo ", nama, "apa kabar? ")
print("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")

#biodata ktp, nama, bulan lahir, tanggal, usia, output pak bu siapa adalah lahir dibulan sekitan tgl sekian
nama=input("Masukkan nama Anda: ")
bulan=input("Masukkan bulan lahir Anda: ")
tanggal=int(input("Masukkan tanggal lahir Anda: "))
usia=int(input("Masukkan usia Anda: "))
print("nama anda adalah", nama, "yang lahir pada bulan", bulan, "dengan tanggal", tanggal, "dan usia anda adalah", usia)
"""
"""
tampan=input("apakah dia ganteng?")
if tampan=="banget":
    print("setuju")
else:
    print("dih org dia ganteng")
"""
"""
umur=int(input("umur? "))
if umur>=21:
    print("ayo pesta")
else:
    print("ke gereja aja yuk")
"""
"""
umur=int(input("umur? "))
if umur <=7:
    print("kamu masih kecill")
elif umur >=7:
    print("kamu juga masih kecill")
else:
    print("berarti udh apa ya")
"""
"""
#1 nasgor, 2 bakmie goreng, 3 usus sapi, 4 otak udang, 5 akong

menu=int(input("pesan menu no berapa? (pilih 1-5) "))
if menu==1:
    print("oke, nasgor ya")
elif menu==2:
    print("oke, bakmie goreng")
elif menu==3:
    print("oke, usus sapi")
elif menu==4:
    print("otak udang ya")
elif menu==5:
    print("akong apaan")
else:
    print("waduhh gada di menu itu")
print("terimakasih sudah memesan")
"""
"""
alas=int(input("masukkan alas segitiga: "))
tinggi=int(input("masukkan tinggi segitiga: "))
luas= alas*tinggi*0.5
print("jadi luas segitiga adalah: ", luas)
"""

"""
#1 persegi, 2 persegi panjang, 3 segitiga

bentuk=int(input("mau luas bentuk no berapa? "))
if bentuk==1:
    print("persegi")
    sisi=int(input("masukkan sisi persegi: "))
    luas= sisi*sisi
    print("jadi luas persegi panjang adalah: ", luas)
elif bentuk==2:
    print("persegi panjang")
    panjang=int(input("masukkan panjang persegi panjang: "))
    lebar=int(input("masukkan lebar persegi panjang: "))
    luas= panjang*lebar
    print("jadi luas persegi panjang adalah: ", luas)
elif bentuk==3:
    print("segitiga")
    alas=int(input("masukkan alas segitiga: "))
    tinggi=int(input("masukkan tinggi segitiga: "))
    luas= alas*tinggi*0.5
    print("jadi luas segitiga adalah: ", luas)
else:
    print("no anda salah, masukkan no 1 sampai 3")
print("terimakasih telah menggunakan program inii")
"""

#ini lagi coba coba doang
m=[1,2,3,4,5,6,7,8,9]
for i in range(0,9):
    print(m[i], end='')

