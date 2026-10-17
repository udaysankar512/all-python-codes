import numpy as np

data = [[1,2,3,2.5],
        [2.0,5.0,-1.0,2.0],
        [-1.5,2.7,3.3,-0.8],
        [1.5,2.5,-2.8,3.76]
        ]

class Layers_implimant:
    def __init__(self,n_input,n_nuran):
        self.watage = np.random.rand(n_input,n_nuran)
        self.bieas = np.zeros((1,n_nuran))
    def forword(self,inputs): # the inputs are the data imput from the test or train the model
        self.output = np.dot(inputs,self.watage) + self.bieas
        

layer1 = Layers_implimant(4,10)
layer2 = Layers_implimant(10,8)
layer3 = Layers_implimant(8,4)
layer_output = Layers_implimant(4,2)

print("layer 1:")
layer1.forword(data)
print(layer1.output)

print("layer 2:")
layer2.forword(layer1.output)
print(layer2.output)

print("layer 3:")
layer3.forword(layer2.output)
print(layer3.output)

print("output layer :")
layer_output.forword(layer3.output)
print(layer_output.output)

print("="*100)