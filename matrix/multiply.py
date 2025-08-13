#Multiply by two matrix: 

a = [[4, 5, 6],
     [8, 5, 4],
     [3, 5, 8]]
b = [[4, 6],
     [6, 3],
     [8, 9]]
c = [[0, 0],
     [0, 0],
     [0, 0]]
for i in range(0, len(c)):
    for j in range(0, len(c[0])):
        for k in range(0, len(b)):
            c[i][j] += a[i][k]*b[k][j]
for r in c:
    print(r)
# print(c)