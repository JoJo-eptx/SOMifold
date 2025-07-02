import networkx as nx
from scipy.spatial.distance import euclidean

class DifferenceGraphBuilder:
    """Builds difference graphs from original graphs and computes node-wise avg difference."""

    def __init__(self, reference_value=1.0061177485142743):
        self.reference_value = reference_value

    def create_difference_graph(self, original_graph):
        diff_graph = nx.Graph()
        for node in original_graph.nodes():
            neighbors = list(original_graph.neighbors(node))
            if neighbors:
                distances = [euclidean(node, neighbor) - self.reference_value for neighbor in neighbors]
                avg_diff = sum(distances) / len(distances)
            else:
                avg_diff = 0.0
            diff_graph.add_node(node, avg_difference=avg_diff)
        return diff_graph
