from SteppingStoneAlgortihm import SteppingStone as ss

matrix = [[(True, 0), (True, 1), (True, 1)],
          [(True, 0), (False, 1), (True, 2)]]

matrix_2 = [[(True, 1), (False, 1), (False, 1), (True, 1)],
            [(False, 1), (False, 1), (True, 1), (True, 1)],
            [(False, 1), (False, 1), (False, 1), (False, 1)],
            [(True, 1), (False, 1), (True, 1), (False, 1)]]

matrix_3 = [[(False, 1), (False, 1), (False, 1), (True, 1)],
            [(False, 1), (True, 1), (False, 1), (True, 1)],
            [(True, 1), (True, 1), (False, 1), (False, 1)],
            [(True, 1), (False, 1), (False, 1), (True, 1)]]



print(ss.form_path((1, 2), matrix))


print(ss.form_path((0, 3), matrix_2))


