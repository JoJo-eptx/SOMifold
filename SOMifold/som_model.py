import numpy as np
import networkx as nx
from HexSOM import HexagonalGraph
from HexSOM import SelfOrganizingMap

def create_hexagonal_grid(grid_size: int):
    grid_generator = HexagonalGraph(
        N_X=grid_size, N_Y=grid_size,
        x_range=(0, grid_size+9),
        y_range=(0, grid_size)
    )
    lattice = grid_generator.create_graph()
    return lattice

def train_som(lattice: nx.Graph, data: np.ndarray, epochs: int):
    som = SelfOrganizingMap(lattice)
    som.fit(data=data, epochs=epochs, min_distance=0.5, neighborhood_radius=1.5)
    return som

def create_graph_from_weights(original_graph, weights):
    new_graph = nx.Graph()
    node_mapping = {}
    for node, weight in zip(original_graph.nodes, weights):
        node_pos = tuple(weight) if hasattr(weight, '__iter__') and not isinstance(weight, str) else (weight,)
        new_graph.add_node(node_pos)
        node_mapping[node] = node_pos

    for edge in original_graph.edges:
        new_graph.add_edge(node_mapping[edge[0]], node_mapping[edge[1]])

    return new_graph
