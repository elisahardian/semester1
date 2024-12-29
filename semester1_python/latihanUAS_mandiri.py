"""
#while. bikin password. minta input pass
jawab=str(input("masukkan password awal anda: "))
while True:
    a=str(input("masukkan password: "))
    if a==jawab:
        print("password benar. selamat datang")
        break
    else:
        print("password salah. coba lagi")

#menghitung momentum p=m.v. m=100. v=dari 0 sampai 100, kanaikan v 10
for v in range(0,110, 10):
    momentum=100*v
    print("saat v=",v,", momentumnya=", momentum)
    
#membuat segitiga menggunakan for
for i in range(0,5):
    print("*"*i)
    i+=1

for i in range(5,0,-1):
    print("*"*i)
    i-=1

n=int(input("mau berapa baris? "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()


n=int(input("mau berapa baris? "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()


n=int(input("mau berapa baris? "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
"""
"""
#BILANGAN GENAP, GANJIL
print("GANJIL")
for i in range(1,11,2):
    print(i)
print()
i=1
while i<11:
    print(i)
    i+=2

print()
print("GENAP")
for i in range(0,11,2):
    print(i)
print()
i=0
while i<11:
    print(i)
    i+=2
"""
"""
#FAKTORIAL
n=int(input("masukkan n= "))
hit=1
for i in range(1,n+1):
    hit=hit*i
    i+=1
print(f"faktorial dari {n}!= {hit}")
"""
"""
nama=['gord', 'nana', 'jhonson']
for i in nama:
    print(i)
for i in range(0,len(nama)):
    print(nama[i])
nama="elisa"
for i in nama:
    print(i)
"""   

"""
#CONTINUE, BREAK, PASS
print('BREAK')
for i in range(0,5,1):
    if i==3:
        break
    print(i)
print()
i=0
while i<=5:
    if i==3: break
    print(i)
    i+=1
print()

print('CONTINUE')
for i in range(0,5,1):
    if i==3:
        continue
    print(i)

print()
print('PASS')
for i in range(0,6,1):
    if i==3:
        pass
    print(i)
print()  
i=0
while i<=5:
    if i==3: pass
    print(i)
    i+=1
"""
"""
nama=[]
nama.append("aling")
nama.append("elisa")
nama.append("hardian")
for i in range(0,len(nama)):
    print("nama: ")
    for j in range(0, len(nama[i])):
        print(nama[i][j], end="")
    print()
print()
a=[2,3,4,5,6,7]
for i in range(0,3):
    print(a[i])
print()
for i in a:
    print(i)
print()
for i in a:
    hit=i*2
    print(hit)
print()
a=[2,3,4,5,6,7]
for i in a[1:3]:
    hit=i **2
    print(hit)
print()
n=int(input("masukkan n= "))
for i in range(0,n+1):
    print(f"{i}x{i}={i*i}")
for i in range(0,n+1):
    print(f"{i}pangkat 2={i**2}")
"""
"""
#SEGITIGA
for i in range(0,4):
    print("*"*i)
print()
n=int(input("masukkan n= "))
for i in range(0,n+1):
    print("*"*i)
print()
n=int(input("masukkan n= "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="")
    print()
print()
n=int(input("masukkan n= "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
print()
n=int(input("masukkan n= "))
for i in range(n+1,-1,-1):
    for j in range(i+1,0, -1):
        print(j, end="")
    print()
"""
