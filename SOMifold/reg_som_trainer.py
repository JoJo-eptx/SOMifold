import pickle
from HexSOM import RegSOM  # Adjust import as needed

class RegSOMTrainer:
    """Initializes, optionally trains, and saves a RegSOM object."""

    def __init__(self, lattice_graph, learning_rate=0.01):
        self.lattice_graph = lattice_graph
        self.learning_rate = learning_rate
        self.regsom = RegSOM(lattice_graph, learning_rate=learning_rate)

    def set_weights(self, weight_vector):
        if len(weight_vector) != len(self.lattice_graph.nodes()):
            raise ValueError("Weight vector length does not match number of lattice nodes.")
        self.regsom.weights = weight_vector.reshape(-1, 1) if weight_vector.ndim == 1 else weight_vector

    def train(self, input_data, epochs=100):
        self.regsom.train(input_data, epochs=epochs)

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.regsom, f)
        print(f"RegSOM saved to {filename}")

    def get_regsom(self):
        return self.regsom
