import numpy as np

data = [[1,2,3,2.5],
        [2.0,5.0,-1.0,2.0],
        [-1.5,2.7,3.3,-0.8]
        ]
class Layer_Dense:
    def __init__(self,n_inputs,n_nuran):
        self.weights = np.random.rand(n_inputs,n_nuran)
        self.biases = np.zeros((1,n_nuran))
    def forword(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases
    

layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

print("Layer 1")
layer1.forword(data)
print(layer1.output)

print("Layer 2")
layer2.forword(layer1.output)
print(layer2.output)