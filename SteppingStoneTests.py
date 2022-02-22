import pytest
from SteppingStoneAlgortihm import SteppingStone as ss


class TestSteppingStone:

    def test_water(self):
        matrix_1 = [[(False, 0), (True, 1)],
                    [(True, 0), (True, 1)]]
        assert 1 == len(ss.water(matrix_1))

