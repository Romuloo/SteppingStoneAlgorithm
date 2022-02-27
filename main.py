import random

from SteppingStoneAlgortihm import SteppingStone as ss

matrix = [[(False, 2), (False, 8), (False, 1)],
          [(True, 1), (True, 3), (True, 1)]]

matrix_2 = [[(False, 1), (True, 100), (False, 1), (False, 1)],
            [(True, 1), (True, 1), (True, 1), (True, 1)],
            [(False, 1), (False, 1), (False, 1), (False, 1)],
            [(True, 1), (False, 1), (True, 1), (True, 1)]]

matrix_3 = [[(False, 1), (False, 1), (False, 1), (True, 1)],
            [(False, 1), (True, 1), (False, 1), (True, 1)],
            [(True, 1), (True, 1), (False, 1), (False, 1)],
            [(True, 1), (False, 1), (False, 1), (True, 1)]]

matrix_5 = [[(True, 5), (False, 3), (False, 2)],
            [(False, 2), (True, 6), (True, 4)],
            [(True, 4), (True, 8), (False, 3)]]

# print(ss.form_path((1, 2), matrix))
print(ss.form_path((2, 2), matrix_5))

print(ss.stepping_stones(matrix_5))
