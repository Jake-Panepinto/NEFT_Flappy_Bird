import math

class Node:
    
    def __init__(self, id_number):
        # Characterizes node type: 0-2 vision, 3 bias
        self.id = id_number
        # Layer 0 denotes input and 1 denotes output
        self.layer = 0
        self.input_value = 0
        self.output_value = 0
        self.connections = []
    
    # Activation function: a(i0 * w0 + i1 * w1 + i2 * w2 + i3 *w3)
    # Adds the product of inputs and weights to output nodes and sigmoids the output
    def activate(self):
        # Scales from 0 to 1
        def sigmoid(x):
            return 1 / (1 + math.exp(-x))
        
        # Output layer
        if self.layer == 1:
            self.output_value = sigmoid(self.input_value)
        
        for i in range(0, len(self.connections)):
            # Adds the result of the product of this nodes weight and output value to the output node
            self.connections[i].to_node.input_value += self.connections[i].weight * self.output_value
