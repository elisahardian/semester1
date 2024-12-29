"""
#OPERASI ARITMATIKA
a=10
b=3
#operasi pertambahan +
hasil= a+b
print(a, "+", b, "=", hasil)
#operasi pengurangan -
hasil= a-b
print(a, "-", b, "=", hasil)
#operasi perkalian *
hasil= a*b
print(a, "*", b, "=", hasil)
#operasi pembagian /
hasil= a/b
print(a, "/", b, "=", hasil)
#operasi eksponen **
hasil= a**b
print(a, "**", b, "=", hasil)
#operasi modulus %
hasil= a%b
print(a, "%", b, "=", hasil)
#operasi floor division
hasil= a//b
print(a, "//", b, "=", hasil)
"""

"""
#OPERASI KOMPARASI
a=4
b=2
#lebih besar dari >
hasil= a > b
print(a, ">", b, "=", hasil)
#kurang dari <
hasil= a < b
print(a, "<", b, "=", hasil)
#lebih besar dari sama dengan >=
hasil= a >= b
print(a, ">=", b, "=", hasil)
#kurang dari sama dengan <=
hasil= a <= b
print(a, "<=", b, "=", hasil)
#sama dengan ==
hasil= a == b
print(a, "==", b, "=", hasil)
#tidak sama dengan !=
hasil= a != b
print(a, "!=", b, "=", hasil)

a=4
b=4
hasil= a is b
print(a, "is", b, "=", hasil)
"""


#OPERASI LOGIKA ATAU BOOLEAN 

# NOT (kebalikan dari data awal)
a= True
c= not a
print("data a= ", a)
print("----------NOT")
print("data c= ", c)
a= False
c= not a
print("data a= ", a)
print("----------NOT")
print("data c= ", c)
# OR (jika salah satu True, maka hasilnya True)
a= False
b= True
c= a or b
print(a, "or", b, "=", c)
a= True
b= False
c= a or b
print(a, "or", b, "=", c)
a= True
b= True
c= a or b
print(a, "or", b, "=", c)
a= False
b= False
c= a or b
print(a, "or", b, "=", c)
# AND (jika 2 buah nilai True, maka hasil True)
a= False
b= True
c= a and b
print(a, "and", b, "=", c)
a= True
b= False
c= a and b
print(a, "and", b, "=", c)
a= True
b= True
c= a and b
print(a, "and", b, "=", c)
a= False
b= False
c= a and b
print(a, "and", b, "=", c)
# XOR (jika 2 nilai berlaian, maka hasilnya True)
a= False
b= True
c= a ^ b
print(a, "XOR", b, "=", c)
a= True
b= False
c= a ^ b
print(a, "XOR", b, "=", c)
a= True
b= True
c= a ^ b
print(a, "XOR", b, "=", c)
a= False
b= False
c= a ^ b
print(a, "XOR", b, "=", c)
