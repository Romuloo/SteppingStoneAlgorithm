import pytest
from SteppingStoneAlgortihm import SteppingStone as ss

__author__ = "Javier Linares Castrillón"


class TestSteppingStone:
    matrix_1 = [[(False, 0), (True, 1), (False, 1)], [(True, 0), (True, 1), (True, 2)]]
    matrix_2 = [[(False, 0), (True, 1)], [(True, 0), (True, 1)]]

    def test_water(self):
        assert 1 == len(ss.water(self.matrix_2))

    def test_form_graph_1(self):
        memory = [(0, 0)]
        assert [(0, 1), (1, 0)] == ss.get_arcs((0, 0), ss.stone(self.matrix_1), memory).get((0, 0))

    # If the result of get() with one of the given keys is empty, the test fails assuming that
    # the given list of elements is not completed.
    def test_form_graph(self):
        keys = [(0, 0), (1, 2), (1, 1), (1, 0), (0, 1)]
        check = True
        while keys:
            empty = ss.form_graph((0, 0), ss.stone(self.matrix_1)).get(keys.pop())
            if not empty:
                check = False
                break
        assert check

