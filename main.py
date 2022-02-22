from SteppingStoneAlgortihm import SteppingStone as ss

matriz = [[(False, 0), (True, 1), (False, 1)],
          [(True, 0), (True, 1), (True, 2)]]

# rows = len(matriz)
# columns = len(matriz[0])
# print(str(rows) + ', ' + str(columns))

# for i in range(len(matriz)):
#   for j in range(len(matriz[i])):
#       print(str(i) + ', ' + str(j))

print('waters: ' + str(ss.water(matriz)))
print('stones: ' + str(ss.stone(matriz)))

print('path_1: ' + str(ss.form_graph((0, 0), ss.stone(matriz)).get((0, 0))))
