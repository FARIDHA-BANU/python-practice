m1 = [[1, 2], [3, 4]]
m2 = [[1, 2], [3, 4]]
r = [[0, 0], [0, 0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        r[i][j] = m1[i][j] + m2[i][j]

print("Addition of two matrices:")
for item in r:
    print(item)
