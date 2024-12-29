"""
##STRING
teks="kata \" biemers\" ini ada di dalam tanda kutip dua"
print(teks)
teks="kata \' biemers\' ini ada di dalam tanda kutip satu"
print(teks)
teks="kata 'biemers' ini ada di dalam tanda kutip satu, wlaupun gapake garis \\"
print(teks)
teks="backslash ini \\"
print(teks)
teks="ini karakter \\t tab\tjadi dia kesamping, spasi panjang"
print(teks)
teks="ini karakter \\n newline- \n-jadi dia kebawah"
print(teks)
#OCTAL DAN HEXADECIMAL
teks="contoh octal value \"\110\145\154\154\157 \" "
print(teks)
print("(110) octal adalah karakter \'H\'")
print("(145) octal adalah karakter \'e\'")
print("(154) octal adalah karakter \'l\'")
print("(154) octal adalah karakter \'l\'")
print("(157) octal adalah karakter \'o\'")
print("escape character \\110\\145\\154\\154\\157 menghasilkan tulisan \"\110\145\154\154\157\"")
teks="contoh hexadecimal value \"\x48\x65\x6c\x6c\x6f\""
print(teks)
print("(x48) hexadecimal adalah karakter \'H\'")
print("(x65) hexadecimal adalah karakter \'e\'")
print("(x6c) hexadecimal adalah karakter \'l\'")
print("(x6c) hexadecimal adalah karakter \'l\'")
print("(x6f) hexadecimal adalah karakter \'o\'")
print("escape character \\x48\\x65\\x6c\\x6c\\x6f menghasilkan tulisan \"\x48\x65\x6c\x6c\x6f\"")
angka=31
format_hex=f"hex= {hex(angka)}"
print(format_hex)
format_octal=f"octal= {oct(angka)}"
print(format_octal)


#OPERASI STRING
age=36
text="my name is john, i am {}"
print(text.format(age))

quantity=3
price=49.958
itemno=567
text="hello i want to buy {} pieces of item number {}, is it {} dollars? "
print(text.format(quantity, itemno, price))
text="hello i want to buy {0} pieces of item number {1}, is it {2} dollars?. here you go, {2} dollars, give me {0} pieces please"
print(text.format(quantity, itemno, price))

text="hello i want to buy {} pieces of item number {}, is it {:.2f} dollars? "
print(text.format(quantity, itemno, price))
angka=280.98892
print(f"mau dibulatin 3 angka diblkg koma= {angka:.3f}")
a="biemers"
b="is the best"
c=a+" "+b
print(c, "jumlah karakternya ada =", len(c))

ruler="0123456789"
teks="ini aling"
print(ruler)
print(teks)
print(ruler[:]) #ini nge cetak semuannya
print(teks[:3]) # ini nge cetak dari awal sampe index ke 3-1= 2
print(teks[2:6]) #ini nge cetak dari index ke 2 sampe index ke 6-1=5
kataacak="SEkarANg LagI ApA"
print(kataacak.lower())
print(kataacak.upper())
print(kataacak.capitalize())
print(kataacak.title())
nanya=kataacak.isupper()
print(nanya)
nanya=kataacak.istitle()
print(nanya)
kataacak="hallooo"
nanya=kataacak.islower()
print(nanya)
nama="Elisa Hardian"
cek_starts="Elisa Hardian".startswith("elisa")
cek_ends="Elisa Hardian ".endswith("an ")
print(cek_starts, cek_ends)

pisah=["aku", "dan", "kamu"]
gabungan=" ".join(pisah)
print("dari gini=", pisah, ", jadi gini=", gabungan)
gabungan="ekhem".join(pisah)
print("dari gini=", pisah, ", jadi gini=", gabungan)
gabungan="akuekhemdanekhemkamu"
print(gabungan.split("ekhem"))

kanan="kanan".rjust(20)
print(" "+ kanan +" ")
kiri="kiri".ljust(20)
print(" "+ kiri +" ")
tengah="tengah".center(20)
print(" "+ tengah +" ")

a="      hello world"
print(a.strip()) #menghapus space didepan itu

teks="hello guys ini aling, sekarang aling lagi belajar koding, udh jam 9:50 lhoo, tapi aling masih buka laptop. mantappp"
print(teks.replace("aling", "aku"))

field=["nama", "kota", "negara", "umur"]
rekord=" nobita; tokyo; jepang; 10"
hasil=rekord.split(";")
print(hasil)
for i in range(0, len(hasil)):
    print(field[i] + ":" + hasil[i])

kalimat="aling lagi belajar algoritma pemrograman, skrng tgl 20 november, bsk rencana aling mau belajar statistik sama mtk diskrit"
y=kalimat.find("lagi") #"lagi" ada di index keberapa
z=kalimat.count("aling") #ada berapa kata "aling"
print("ada di index ke: ", y, "; ada berapa banyak kata yg dicari: ", z)

#nama ASCII
c="p"
d="P"
print("ASCII dari p: ", ord(c))
print("ASCII dari P: ", ord(d))

"""
