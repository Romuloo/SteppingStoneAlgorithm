import copy
import random
from collections import defaultdict

__author__ = "Javier Linares Castrillón"


class SteppingStone:

    # This method searches for the position of all the waters in the matrix.
    # Returns a list of tuples containing the position of all the waters
    # O(i^j)
    @staticmethod
    def water(matrix):
        waters = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j][0]:
                    waters.append((i, j))
        return waters

    # This method checks if there is any stone in the abscissa axis.
    # Returns True if there is at least 1 stone.
    # O(n)
    @staticmethod
    def check_abscissa(v, matrix):
        counter = 0
        for i in range(len(matrix[0])):
            if matrix[v[0]][i][0] and i != v[1]:
                counter += 1
        return counter != 0

    # This method checks if there is any stone in the ordinate axis.
    # Returns True if there is at least 1 stone.
    # O(n)
    @staticmethod
    def check_ordinate(v, matrix):
        counter = 0
        for i in range(len(matrix)):
            if matrix[i][v[1]][0] and i != v[0]:
                counter += 1
        return counter != 0

    # This method forms the path for 1 water cell
    @staticmethod
    def form_path(v, matrix):
        matrix[v[0]][v[1]] = (True, matrix[v[0]][v[1]][1])
        found = False
        vx = v
        so = []
        sa = []
        while not found:
            if len(so) > 0:
                vx = so.pop()
            if SteppingStone.check_abscissa(vx, matrix):
                for i in range(len(matrix[0])):
                    if matrix[vx[0]][i][0] and i != vx[1]:
                        sa.append((vx[0], i))
                for stone in sa:
                    if not SteppingStone.check_ordinate(stone, matrix):
                        sa.remove(stone)
                    if stone == v:
                        found = True
            for stone in sa:
                for j in range(len(matrix)):
                    if matrix[j][stone[1]][0] and j != stone[0]:
                        so.append((j, stone[1]))
                for stone_2 in so:
                    if not SteppingStone.check_abscissa(stone_2, matrix):
                        so.remove(stone_2)
                    if stone_2 == v:
                        found = True
        if found:
            matrix[v[0]][v[1]] = (False, matrix[v[0]][v[1]][1])
        print([sa, so])
        return [sa, so]

    @staticmethod
    def stepping_stones(matrix):
        paths = []
        results = {}
        for water in SteppingStone.water(matrix):
            paths.append(SteppingStone.form_path(water, matrix))
        for path in paths:
            suma = 0
            aux_i = 0
            for i in range(len(path[1])):
                try:
                    suma += matrix[path[0][i][0]][path[0][i][1]][1] * -1
                except IndexError:
                    print('list index out of range')
                try:
                    suma += matrix[path[1][i][0]][path[1][i][1]][1]
                except IndexError:
                    print('list index out of range')
                aux_i = i
            results[matrix[path[1][aux_i][0]][path[1][aux_i][1]]] = suma

        for t in results:
            if results[t] < 0:
                return (t, results[t])
        return True

