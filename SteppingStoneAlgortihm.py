import copy
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

    @staticmethod
    def form_path(v, matrix):
        found = False
        vx = v
        stones = [vx]

        while not found:
            if len(stones) > 0:
                vx = stones.pop()

            if SteppingStone.check_abscissa(vx, matrix):
                for i in range(len(matrix[0])):
                    if matrix[vx[0]][i][0] and i != vx[1]:
                        stones.append((vx[0], i))   # todas las piedras de la horizontal
                for stone in stones:
                    if stone == v:
                        found = True
                    if not SteppingStone.check_ordinate(stone, matrix):  # por cada piedra de la horizontal, si no tiene vertical, la anulo.
                        stones.remove(stone)
            found = True




        return stones

