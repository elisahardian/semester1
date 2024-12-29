"""
data="ini adalah string" #bisa menggunakan petik 1 atau 2, ' "
print(data)
print(type(data))
print(' "hallooo ini pake kutip 2 kali" ')
print(" 'hallooo ini pake kutip 2 kali juga' ")
print("ini hari jum'at")
print("ini hari jum\'at")
print("ucup \tbunga, ini menjadi jauhan")
print("ucup \bbunga, ini menjadi deketan")
print("baris pertama, \r\nbaris kedua") # \r buat apa sihh ?
print("baris pertama, \rbaris kedua") #alg ga ngerti ini buat apa
"""

print("""
    ini keren sih, jadi dia multiline
    nama: ini alg
    tgl: 11 okt 2023
      """)

"""
#OPERASI DAN MANIPULASI STRING
#menyambung strinng
nama_pertama= "Elisa"
nama_tengah= "Hardian"
nama_akhir= "."
nama_lengkap= nama_pertama+nama_tengah+nama_akhir
print(nama_lengkap)
nama_lengkap=nama_pertama+" "+nama_tengah+nama_akhir
print(nama_lengkap)

#menghitung panjang string
panjang=len(nama_lengkap) 
print(panjang) #hasilnya akan 14 karena spasi dan titik diitung

#mengecek apakah ada komponen char atau string di string
d="d"
status=d in nama_lengkap
print(d+ " ada di " + nama_lengkap + "=" + str(status))
status=d not in nama_lengkap
print(d+ " tidak ada di " + nama_lengkap + "=" + str(status))

#mengulang string
print("wkw"*10)
print(8*"kwk")

#indexing
print("index ke-0: " + nama_lengkap[0])
print("index ke-5: " + nama_lengkap[5]) #index ke 5 itu spasi
print("index ke-[0:3]: " + nama_lengkap[0:3]) #yg di index ke 3 nya tidak termasuk
print("index ke-[0:8:2]: " + nama_lengkap[0:8:2]) #dari index 0 sampai index ke 8 tapi index ke 8 nya ga termasuk, trus dijarakin 2 angka.

#item paling kecil dan paling besar
print("paling kecil: " + min(nama_lengkap)) #yg paling kecil yaitu spasi
print("paling besar: " + max(nama_lengkap)) #yg paling besar yaitu huruf s, bedasarkan urutan abjad

# ASCII adalah American Standard Code For Information Interchange, kode yang digunakan untuk mewakili karakter dalam komputer
ascii_code=ord(" ")
print("ASCII code untuk spasi adalah: ", str(ascii_code))
data= 117
print("char untuk ASCII 117 adalah: ", chr(data)) #jadi karakter yg memiliki no ascii 117 adalah u

#operator dalam bentuk method
data="ilmu matematika"
jumlah=data.count("m")
print("jumlah m pada ", data, "=", str(jumlah))

#MERUBAH CASE DARI STRING
#merubah semua ke uppercase
salam="broooo!"
print("normal= ", salam)
salam= salam.upper()
print("upper= ", salam)
#merubah smua ke lowercase
ganormal="seMAngaT yA paSTi BiSa"
print(ganormal)
ganormal=ganormal.lower()
print(ganormal)

salam="SISTTT"
apakah_upper=salam.isupper()
print(salam, " is upper? ", str(apakah_upper))
apakah_lower=salam.islower()
print(salam, " is lower? ", str(apakah_lower))

#isalpha() , untuk mengecek semuanya huruf bukan
#isalnum() , huruf dan angka
#isspace() , spasi, tab, newline
#istitle() , semua kata dimulai dengan huruf besar

judul="It Is Okay To Not To Be Okay" #jika ada 1 saja huruf besar judul jadi kecil, maka akan false
cek_judul=judul.istitle()
print(judul, " is title? ", str(cek_judul))

#mengecek komponen startswith() dan endswith()
cek_start="ini apa ya".startswith("ini")
print("starts: ", str(cek_start))
cek_end="ini apa yaaa".endswith("yaa") #yg ini hasil akan salah, karena yaaa sama yaa berbeda
print("ends: ", str(cek_end))

#penggabungan komponen join() , split()
pisah=["aku", "keren", "banget"]
gabung= " ".join(pisah)
print(pisah)
print(gabung)
gabung= "ehem".join(pisah)
print(gabung)
gabung="akuehemkerenehembanget"
print(gabung.split("ehem"))

#alokasi karakter rjust() , ljust() , center()
kanan="kanan".rjust(10)
print("'", kanan, "'")
kiri="kiri".ljust(10)
print("'", kiri, "'")
tengah="tengah".center(10)
print("'", tengah, "'")
"""