a=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]
b=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]

print("enter matrix a: ")
for i in range(5):
    for j in range(5):
        a[i][j]=int(input(f"enter a[{i}][{j}]: "))

print("enter matrix b: ")
for i in range(5):
    for j in range(5):
        b[i][j]=int(input(f"enter b[{i}][{j}]: "))
        
result=[[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j]=+ a[i][k] * b[k][j]

for r in result:
    print(r)
    