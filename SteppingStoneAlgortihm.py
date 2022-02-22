class SteppingStone:

    # This method searches for the position of all the waters in the matrix.
    @staticmethod
    def water(matrix):
        waters = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j][0]:
                    waters.append((i, j))
        return waters

    # This method searches for the position of all the stones in the matrix.
    @staticmethod
    def stone(matrix):
        stones = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j][0]:
                    stones.append((i, j))
        return stones

