from SteppingStoneAlgortihm import SteppingStone as ss

matrix = [[(False, 0), (True, 1), (True, 1)],
          [(True, 0), (True, 1), (True, 2)]]

matrix_2 = [[(False, 1), (False, 1), (False, 1), (True, 1)],
            [(False, 1), (False, 1), (False, 1), (False, 1)],
            [(False, 1), (False, 1), (False, 1), (False, 1)],
            [(True, 1), (False, 1), (False, 1), (True, 1)]]

print(ss.form_path((0, 0), matrix))


