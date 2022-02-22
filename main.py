from SteppingStoneAlgortihm import SteppingStone as ss

matrix = [[(False, 0), (True, 1), (False, 1)],
          [(True, 0), (True, 1), (True, 2)]]

# rows = len(matriz)
# columns = len(matriz[0])
# print(str(rows) + ', ' + str(columns))

# for i in range(len(matriz)):
#   for j in range(len(matriz[i])):
#       print(str(i) + ', ' + str(j))

print('waters: ' + str(ss.water(matrix)))
print('stones: ' + str(ss.stone(matrix)))
m = [(0, 1)]

print('path_1: ' + str(ss.get_arcs((1, 1), ss.stone(matrix), m).get((1, 1))))

print(ss.form_graph((0, 0), ss.stone(matrix)).keys())
