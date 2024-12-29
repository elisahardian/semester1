"""
## PREDICTED LOOP
for i in range(5):
    print(i)
print()
for index in range(2,7):
    print(index)
print()

jajan=["getuk", "baso", "kentang", "gorengan"]
n=len(jajan)
for i in range(0,n):
    print(jajan[i])
print()
teks="elisa"
for i in teks:
    print(i)
print()
for i in range(2,6):
    print(i)
else:
    print("selesaii loopnya")
print()

for i in range(6,11):
    if i==9: break
    print(i)
else:
    print("selesai") #yg ini juga ga tercetak. karena ada break
print()
for i in range(6,11):
    if i==9: continue #jika ketemu angka 9, maka terskip, kembali keawal, perintah dibawah ini ga keeksekusi
    print(i)
else:
    print("selesai")
print()
for i in range(-3,4):
    print(i)
print()
for i in range(2,8,2):
    print(i)
print()
for i in range(10, 0, -1):
    print(i)

#nested loop
m=[]
m.append([[1,2,3],[4,5,6],[7,8,9]])
m.append([[10,11,12],[13,14,15],[16,17,18]])
m.append([[19,20,21],[22,23,24],[25,26,27]])
m.append([[28,29,30],[31,32,33],[34,35,36]])
for i in range(0, len(m)):
    print("matriks ke-", i)
    for j in range(0, len(m[i])):
        print(m[i][j])
        if j>= len(m[i])-1:
            print()

for i in range(0,5,1):
    hitung=i**2
    print(hitung)
print()
for i in range(5,0,-1):
    hitung=i**2
    print(hitung)
print()
#PROGRAM MENGHITUNG NxN SAMPAI 9
for i in range(1,10):
    hitung=i*i
    print(i, "x", i, "=", hitung)
print()


#PROGRAM MENGHITUNG FAKTORIAL
n=int(input("masukkan nilai  n= "))
hitung=1
for i in range(1,n+1):
    hitung=hitung*i
print(f"{n}! = ", hitung)

#kalo faktorial pake while
n=int(input("masukkan nilai  n= "))
hitung=1
i=1
while i<(n+1): #atau sama juga kalo i<=n
    hitung=hitung*i
    i+=1
print(f"{n}!={hitung}")

print()
#bikin segitiga angka
n=3
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()

n=3
for i in range(n+1, -1, -1):
    for j in range(i+1, 0,-1):
        print(j, end=" ")
    print()

print()
n=5
for i in range(n-1, -1, -1):
    for j in range(i+1, 0, -1):
        print(j, end=" ")
    print()
print("--"*5)
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print()

##UNPREDICTED LOOP
#WHILE

jawab=0
while jawab != 25:
    jawab= int(input("5 x 5 = "))
    if jawab != 25:
        print("jawaban anda salah, 5x5 bukan ", jawab)
print("benar, 5x5 adalah ", jawab)

print()
i=1
while i<10:
    print(i)
    i+=1

print()
i=1
while i<10:
    i+=1
    print(i)

print()
#DO WHILE
while True:
    jawab=int(input("berapa 5x5= "))
    if jawab != 25:
        print("salah, 5x5 bukan ", jawab)
    else:
        print("benar, 5x5= ", jawab)
        break

while True:
    jawab=int(input("5x5= "))
    if jawab==25:
        print("benar");
        break
    else:
        print("coba lagi")

print()
angka=0
while angka<5:
    angka+=1
    print("aling keren-- pengulangan ke", angka)

print()
angka=0
while angka<5:
    angka+=1
    print(angka)

print()
angka=0
while angka<5:
    angka+=1
    if angka==3:
        print("hallo")
    print(angka)

angka=0
while angka < 5:
    angka+=1
    if angka==3:
        pass #tidak akan diproses, tidak pengaruh
    print(angka)

angka=0
print(f"angka sekarang: {angka}")
while angka<5:
    angka+=1
    print(f"angka sekarang: {angka}")
    if angka==3:
        print("nicee")
    print("whatsupp")
print("finish!")
print()

angka=0
print(f"angka sekarang: {angka}")
while angka<5:
    angka+=1
    print(f"angka sekarang: {angka}")
    if angka==3:
        print("nicee")
        continue
    print("whatsupp")
print("finish!")
print()

angka=0
print(f"angka sekarang: {angka}")
while angka<5:
    angka+=1
    print(f"angka sekarang: {angka}")
    if angka==3:
        print("nicee")
        break
    print("whatsupp")
print("finish!")
"""