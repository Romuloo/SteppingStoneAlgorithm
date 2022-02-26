import pytest
from SteppingStoneAlgortihm import SteppingStone as ss

__author__ = "Javier Linares Castrillón"


class TestSteppingStone:
    matrix_1 = [[(False, 0), (True, 1), (False, 1)],
                [(True, 0), (True, 1), (True, 2)]]
    matrix_2 = [[(False, 0), (True, 1)],
                [(True, 0), (False, 1)]]

    def test_water(self):
        assert 2 == len(ss.water(self.matrix_2))

    def test_check_abscissa(self):
        assert True == ss.check_abscissa((0, 0), self.matrix_1)

    def test_check_ordinate(self):
        assert False == ss.check_ordinate((0, 1), self.matrix_2)
