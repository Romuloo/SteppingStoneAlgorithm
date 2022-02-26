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
            if matrix[v[0]][i][0]:
                counter += 1
        return counter != 0

    # This method checks if there is any stone in the ordinate axis.
    # Returns True if there is at least 1 stone.
    # O(n)
    @staticmethod
    def check_ordinate(v, matrix):
        counter = 0
        for i in range(len(matrix)):
            if matrix[i][v[1]][0]:
                counter += 1
        return counter != 0

