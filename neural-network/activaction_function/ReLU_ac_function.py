import numpy as np

data = np.array([
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8],
    [1.5, 2.5, -2.8, 3.76]
])

class Layers:
    def __init__(self,n_input,n_nuran):
        self.watage = np.random.rand()