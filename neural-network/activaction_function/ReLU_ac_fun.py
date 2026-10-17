import numpy as np

# Sample Data
data = np.array([
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8],
    [1.5, 2.5, -2.8, 3.76]
])

# Dense Layer
class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


# ReLU Activation
class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


# Layers
layer1 = Layer(4, 10)
relu1 = Activation_ReLU()

layer2 = Layer(10, 8)
relu2 = Activation_ReLU()

layer3 = Layer(8, 4)
relu3 = Activation_ReLU()

output_layer = Layer(4, 2)

# Forward Pass
layer1.forward(data)
relu1.forward(layer1.output)

layer2.forward(relu1.output)
relu2.forward(layer2.output)

layer3.forward(relu2.output)
relu3.forward(layer3.output)

output_layer.forward(relu3.output)

# Print Outputs
print("Layer 1 Output:")
print(relu1.output)

print("\nLayer 2 Output:")
print(relu2.output)

print("\nLayer 3 Output:")
print(relu3.output)

print("\nFinal Output:")
print(output_layer.output)