"""
print(10>8)
print(19<7)
print(77==77)
x=5
print(x>3 and x<10)
print(x>3 or x<5)
print(not(x>3 or x<5))


x=["apel", "pisang", "anggur"]
y=["apel", "pisang", "anggur"]
z=x
print("x is z", x is z)
print(x is y)
print(x==y)
print(x==z)
print(y==z)
print(y is not z)
print("x is not z", x is not z)
print(x is not y)
print("pisang" in x)
print("apel" not in z)
print(abs(-122))
print(pow(2,4))
print(max(22,3,5,77))
print(min(22,3,5,77))


binary_number=0b1010
print(binary_number)
result=~binary_number
print(result)

a=10
b=12
print("nilai a: ", a, ", nilai b: ", b)
print("nilai bit dari a: ", format(a, "04b"))
print("nilai bit dari b: ", format(b, "04b"))
print("nilai bit dari not a: ", format(~a, "04b"))
print("hasil dari a and b: ", format(a&b, "04b"))
print("hasil dari a or b: ", format(a|b, "04b"))
print("hasil dari a xor b: ", format(a^b, "04b"))
print("hasil dari right shift a: ", format(a>>1, "04b"))
print("hasil dari left shift a: ", format(a<<1, "04b"))


#======DICTIONARY======
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(car)
a=car.copy()
print(a)
b=car.items()
print(b)
c=car.keys()
print(c)
d=car.values()
print(d)
e=car.get("year")
print(e)
f=car["year"]
print(f)
print(car)
car["year"]=1777
print(car)
car["color"]="red"
print(car)
car.update({"color":"blue"})
print(car)
car.pop("year")
print(car)
car.popitem()
print(car)
car.popitem()
print(car)
car.popitem()
print(car)


#dictionary yang dimasukkan kedalam list
listfam=[]
template={
    "name":"elisa",
    "year":2005
}
listfam.append(template)
template={
    "name":"tobias",
    "year":2002
}
listfam.append(template)
template={
    "name":"linus",
    "year":2001
}
listfam.append(template)
template={
    "name":"anna",
    "year":2011
}
listfam.append(template)
print(listfam)
print(len(listfam))
for i in range(0,4):
    print(i, listfam[i])
for i in range(0,4):
    print(i, listfam[i].get("name"), listfam[i].get("year"))
for i in range(0,4):
    template=listfam[i]
    print(i, template["name"], template["year"])
for i in range(0,4):
    print(i, listfam[i]["name"], listfam[i]["year"])


ukuran={
    "tb":[136,123,153,129],
    "bb":[29,31,34,40]
}
print(ukuran)
print(ukuran["tb"])


m=[1,2,3,4,5,6,7,8,9]
print(m)
print(m[0])
print(m[2])
print("panjang m: ", len(m))
for i in m:
    print(i, end=" ")
print()
for m in range(0,10):
    print(m, end=" ")
print()
m=[1,2,3,4,5,6,7,8,9]
print(m)
m.append(10)
print(m)

for i in m:
    print(i, end=" ")
print()
print("panjang m: ", len(m))
print(m)
m.pop(9)
print(m)
for i in range(0, len(m)):
    print(m[i], end=" ") 


m=[1,2,3,4,5,6,7,8,9]
print(m)
m.append(10)
print(m)
m.insert(2,100)
print(m)
m[4]=999
print(m)
m.sort()
print(m)
m.reverse()
print(m)
m.pop(5)
print(m)
m.remove(100)
print(m)
n=[199,233,211]
m.extend(n)
print(m)
m.clear()
print(m)
"""