a=[[1,2],
   [4,3]]
b=[[0,-2],
   [-1,5]]
pertambahan=[[a[0][0]+b[0][0],a[0][1]+b[0][1]],
             [a[1][0]+b[1][0],a[1][1]+b[1][1]]]
print("pertambahan 2 matriks: ", pertambahan)

pengurangan=[[a[0][0]-b[0][0],a[0][1]-b[0][1]],
             [a[1][0]-b[1][0],a[1][1]-b[1][1]]]
print("pengurangan 2 matriks: ", pengurangan)

perkalian=[[(a[0][0]*b[0][0])+(a[0][1]*b[1][0]),(a[0][0]*b[0][1])+(a[0][1]*b[1][1])],
           [(a[1][0]*b[0][0])+(a[1][1]*b[1][0]),(a[1][0]*b[0][1])+(a[1][1]*b[1][1])]]
print("perkalian 2 matriks: ", perkalian)

