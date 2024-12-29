"""
bitwise= operasi masing masing bit
int 2= 0 0 0 0 0 0 1 0
       7 6 5 4 3 2 1 0 (pangkatnya)
       maka 2 pangkat 1 adalah 2. maka betul itu angka binernya
int 5= 0 0 0 0 0 1 0 1
       7 6 5 4 3 2 1 0 (pangkatnya)
       maka 2 pangkat 2 ditambah 2 pangkat 0 adalah 4 ditambah 1 jadi 5. maka betul itu angka binernya
int 9= 0 0 0 0 1 0 0 1
       7 6 5 4 3 2 1 0 (pangkatnya)
       maka 2 pangkat 3 ditambah 2 pangkat 0 adalah 8 ditambah 1 jadii 9. maka betul itu angka binernya
"""

"""
#OPERASI BITWISE, OPERASI BINER, BINARY

a=9
b=5
# bitwise OR (|)
c= a | b
print("\n======bitwise OR======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))
print("---------------------(|)")
print("nilai: ", c, ", binary: ", format(c, "08b"))
# bitwise AND (&)
c= a & b
print("\n======bitwise AND======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))
print("---------------------(&)")
print("nilai: ", c, ", binary: ", format(c, "08b"))
# bitwise XOR (^)
c= a ^ b
print("\n======bitwise XOR======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))
print("---------------------(^)")
print("nilai: ", c, ", binary: ", format(c, "08b"))
# bitwise NOT (~)
c= ~a
print("\n======bitwise NOT======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("---------------------(~)")
print("nilai: ", c, ", binary: ", format(c, "08b"))
"""

"""
# SHIFTING
a=9
b=5
#shift right (>>)
c= a >> 2
print("\n=======>>=======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("---------------------(>>)")
print("nilai: ", c, ", binary: ", format(c, "08b"))
#shift left (<<)
c= a << 2
print("\n=======<<=======")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("---------------------(<<)")
print("nilai: ", c, ", binary: ", format(c, "08b"))
"""

"""
#OPERASI ASSIGNMENT DENGAN PENYINGKATAN
a=5 #ini adalah assignment
print("nilai a: ", a)
a+=1 #artinya a=a+1
print("nilai a+=1, nilai a menjadi: ", a)
a-=2 #artinya a=a-2
print("nilai a-=2, nilai a menjadi: ", a)
a*=5 #artinya a=a*5
print("nilai a*=5, nilai a menjadi: ", a)
a/=2 #artinya a=a/2
print("nilai a/=2, nilai a menjadi: ", a)
b=10
print("\nnilai b: ", b)
b%=3
print("nilai b%=3, nilai b menjadi: ", b)
b=10
b//=3
print("nilai b//=3, nilai b menjadi: ", b)
b=5
b**=3
print("nilai b**=3, nilai b menjadi: ", b)
"""


#OPERASI BITWISE
# OR
c=True
print("nilai c: ", c)
c|=True
print("nilai c|=True, nilai c menjadi: ", c)
c=True
print("nilai c: ", c)
c|=False
print("nilai c|=False, nilai c menjadi: ", c)
c=False
print("nilai c: ", c)
c|=True
print("nilai c|=True, nilai c menjadi: ", c)
c=False
print("nilai c: ", c)
c|=False
print("nilai c|=False, nilai c menjadi: ", c)

# AND
c=True
print("nilai c: ", c)
c&=True
print("nilai c&=True, nilai c menjadi: ", c)
c=True
print("nilai c: ", c)
c&=False
print("nilai c&=False, nilai c menjadi: ", c)
c=False
print("nilai c: ", c)
c&=True
print("nilai c&=True, nilai c menjadi: ", c)
c=False
print("nilai c: ", c)
c&=False
print("nilai c&=False, nilai c menjadi: ", c)

# XOR
c=True
print("nilai c: ", c)
c^=True
print("nilai c^=True, nilai c menjadi: ", c)
c=True
print("nilai c: ", c)
c^=False
print("nilai c^=False, nilai c menjadi: ", c)
c=False
print("nilai c: ", c)
c^=True
print("nilai c^=True, nilai c menjadi: ", c)
c=False
print("nilai c: ", c)
c^=False
print("nilai c^=False, nilai c menjadi: ", c)

# SHIFT (menggeser)
d=0b0100
print("nilai d= ", format(d, "04b"))
d>>=2
print("nilai d>>=2, nilai d menjadi: ", format(d, "04b"))
d<<=1
print("nilai d>>1, nilai d menjadi: ", format(d, "04b"))
