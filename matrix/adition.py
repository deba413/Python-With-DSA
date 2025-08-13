
a = [[1, 5, 3],
     [4, 4, 2],
     [6, 7, 3]]
b = [[1, 5, 9],
     [1, 7, 9],
     [5, 4, 6]]
c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j]+b[i][j]
for r in c:
    print(r)
