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

    # This method searches for the position of all the stones in the matrix.
    # Returns a list of tuples containing the position of all the stones.
    # O(i^j)
    @staticmethod
    def stone(matrix):
        stones = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j][0]:
                    stones.append((i, j))
        return stones

    # This method return the relation between an element, and it's children
    # key: the key value. Initially it's the water.
    # stones: a list of possible nodes.
    # memory: a list where the parent node is stored, just to avoid going backwards.
    # O(n)
    @staticmethod
    def get_arcs(key, stones, memory):
        water_path = defaultdict(list)
        for i in range(len(stones)):
            if (stones[i][0] == key[0] or stones[i][1] == key[1]) and not stones[i] == key and not stones[i] in memory:
                water_path[key].append(stones[i])
        return water_path

    # This method returns all the possible nodes where I can move following the rules
    # O(n^i)
    @staticmethod
    def form_graph(key, stones):
        aux_stones = copy.copy(stones)
        memory = []
        run = True
        graph = defaultdict(list)
        graph[key] = SteppingStone.get_arcs(key, stones, memory).get(key)
        while run:
            new_key = aux_stones.pop()
            graph[new_key] = SteppingStone.get_arcs(new_key, stones, memory).get(new_key)
            if len(aux_stones) == 0:
                run = False
        return graph
