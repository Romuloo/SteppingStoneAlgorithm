
matriz = [[(False, 0), (True, 1), (False, 1)],
          [(True, 0), (True, 1), (True, 2)]]

rows = len(matriz)
columns = len(matriz[0])
print(str(rows) + ', ' + str(columns))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(str(i) + ', ' + str(j))
