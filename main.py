"""Python class to handle Vectors"""
from typing import List, Tuple


class Vector:
    def __init__(self, v=None, w=None):
        pass

    def add(self, v, w):
        assert len(v) == len(w), 'Ooops vectors not of same length'
        self.vector = [v_i + w_i for v_i, w_i in zip(v, w)]
        return self.vector

    def subtract(self, v, w):
        assert len(v) == len(w), 'Ooops the vectors not of same length'
        self.vector = [v_i - w_i for v_i, w_i in zip(v, w)]
        return self.vector

    def __repr__(self):
        return f"Vector--> {self.vector}"


new_vector = Vector()

print(new_vector.add([1, 2, 3], [4, 3, 2]))
