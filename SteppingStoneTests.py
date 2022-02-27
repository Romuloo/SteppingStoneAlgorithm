import pytest
from SteppingStoneAlgortihm import SteppingStone as ss

__author__ = "Javier Linares Castrillón"


class TestSteppingStone:
    matrix_1 = [[(False, 0), (True, 1), (False, 1)],
                [(True, 0), (True, 1), (True, 2)]]
    matrix_2 = [[(True, 0), (True, 1)],
                [(True, 0), (False, 1)]]

    matrix_3 = [[(True, 0), (True, 1)],
                [(True, 0), (True, 1)]]

    matrix_4 = [[(False, 1), (False, 1), (False, 1), (True, 1)],
                [(False, 1), (True, 1), (False, 1), (True, 1)],
                [(True, 1), (True, 1), (False, 1), (False, 1)],
                [(True, 1), (False, 1), (False, 1), (True, 1)]]

    matrix_5 = [[(True, 5), (False, 3), (False, 2)],
                [(False, 2), (True, 6), (True, 4)],
                [(False, 4), (True, 8), (False, 3)]]

    def test_water(self):
        assert 1 == len(ss.water(self.matrix_2))

    def test_check_abscissa(self):
        assert True == ss.check_abscissa((0, 0), self.matrix_1)

    def test_check_ordinate(self):
        assert False == ss.check_ordinate((0, 1), self.matrix_2)

    def test_check_2x2_matrix(self):
        assert [[(0, 1), (1, 0)], [(1, 1), (0, 0)]] == ss.form_path((0, 0), self.matrix_3)

    def test_medium_position(self):
        assert [[(1, 3), (3, 0), (2, 1)], [(3, 3), (3, 3), (2, 0), (1, 1)]] == ss.form_path((1, 1), self.matrix_4)


