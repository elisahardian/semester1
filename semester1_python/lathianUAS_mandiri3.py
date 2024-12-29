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
"""
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
