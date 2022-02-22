import pytest
from SteppingStoneAlgortihm import SteppingStone as ss


class TestSteppingStone:

    def test_water(self):
        matrix_1 = [[(False, 0), (True, 1)],
                    [(True, 0), (True, 1)]]
        assert 1 == len(ss.water(matrix_1))

    def test_form_graph_1(self):
        matrix = [[(False, 0), (True, 1), (False, 1)],
                  [(True, 0), (True, 1), (True, 2)]]
        assert [(0, 1), (1, 0)] == ss.form_graph((0, 0), ss.stone(matrix)).get((0, 0))
