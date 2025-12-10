# Describe what input nodes is connected to what output node
# Our model uses 3 vision nodes and 1 bias node to connect to 1 output node
class Connection:
    
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight