"""
#FORMAT STRING
#string
nama="marlene"
format_str=f"hello {nama}"
print(format_str)
#angka
angka=2005.8
format_str=f"angka= {angka}"
print(format_str)
angka=15
format_str=f"bilangan bulat= {angka}"
print(format_str)
"""

"""
#menampilkan tanda + atau -
angka_min=-10
angka_plus=+10
format_min=f"minus= {angka_min:-d}"
format_plus=f"plus= {angka_plus:+d}"
print(format_min)
print(format_plus)
#memformat persen
persentase=0.045
format_persen=f"persen= {persentase:.2%}"
print(format_persen)
#melakukan operasi aritmatika
harga=10000
jumlah=5
format_string=f"harga total Rp {harga*jumlah:,}"
print(format_string)
#format angka lain
angka=4
format_binary=f"binary= {bin(angka)}"
print(format_binary)
format_octal=f"octal= {oct(angka)}"
print(format_octal)
format_hex=f"hex= {hex(angka)}"
print(format_hex)
"""

#WIDTH DAN MULTILINE
data_nama= "Elisa Hardian"
data_umur= 18
data_tinggi= 166.3
data_nomor_sepatu= 40
#string standard
data_string=f"nama= {data_nama}, umur= {data_umur}, tinggi= {data_tinggi}, data nomor sepatu= {data_nomor_sepatu}"
print(data_string)
#string multiline dengan \n
data_string=f"nama= {data_nama}, \numur= {data_umur}, \ntinggi= {data_tinggi}, \ndata nomor sepatu= {data_nomor_sepatu}"
print(data_string)
#string multiline dengan kutip triplets """
data_string=f"""
nama= {data_nama}
umur= {data_umur}
tinggi= {data_tinggi}
data nomor sepatu= {data_nomor_sepatu}
"""
print(data_string)


#DATE AND TIME
import datetime as dt
hari_ini=dt.date.today()
print(hari_ini)
tanggal=dt.date(2023,6,12)
print(tanggal)

print("silahkan masukkan tanggal, bulan, dan tahun lahir")
tanggal=int(input("tanggal: "))
bulan=int(input("bulan: "))
tahun=int(input("tahun: "))
tanggal_lahir=dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah {tanggal_lahir}")
print(f"harinya adalah {tanggal_lahir:%A}")

""" hari_ini=dt.date.today
print(f"hari ini tanggal: {hari_ini}")
umur=hari_ini - tanggal_lahir
print(f"umur anda adalah {umur}") """ #gatau knp yg ini gamau