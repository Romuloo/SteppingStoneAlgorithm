from collections import defaultdict


class SteppingStone:

    # This method searches for the position of all the waters in the matrix.
    # Returns a list of tuples containing the position of all the waters
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
    @staticmethod
    def stone(matrix):
        stones = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j][0]:
                    stones.append((i, j))
        return stones

    # This method takes a tuple of coordinates for a water cell and a list of tuples with stone's coordinates.
    @staticmethod
    def form_graph(water, stones):
        water_path = defaultdict(list)
        for i in range(len(stones)):
            if stones[i][0] == water[0] or stones[i][1] == water[1]:
                water_path[water].append(stones[i])
        return water_path
