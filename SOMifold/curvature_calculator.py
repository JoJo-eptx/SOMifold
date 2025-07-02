import numpy as np

class CurvatureCalculator:
    """Computes tangent vectors and curvature for hexagonal graphs."""

    @staticmethod
    def compute_tangent_vectors(graph):
        summed_tangent_vectors = {}
        for node in graph.nodes:
            node_pos = np.array(node)
            sum_vec = np.zeros_like(node_pos, dtype=float)
            for neighbor in graph.neighbors(node):
                neighbor_pos = np.array(neighbor)
                sum_vec += neighbor_pos - node_pos
            summed_tangent_vectors[node] = sum_vec
        return summed_tangent_vectors

    @staticmethod
    def compute_laplacian_matrix(graph):
        num_nodes = len(graph.nodes)
        laplacian_matrix = np.zeros((num_nodes, num_nodes))
        nodes = list(graph.nodes)
        for i, node in enumerate(nodes):
            neighbors = list(graph.neighbors(node))
            laplacian_matrix[i, i] = len(neighbors)
            for neighbor in neighbors:
                j = nodes.index(neighbor)
                laplacian_matrix[i, j] = -1
        return laplacian_matrix

    @staticmethod
    def compute_curvature(graph, tangent_vectors):
        laplacian = CurvatureCalculator.compute_laplacian_matrix(graph)
        nodes = list(graph.nodes)
        tangents = np.array([tangent_vectors[node] for node in nodes])
        laplacian_tangents = laplacian.dot(tangents)
        curvatures = {node: np.linalg.norm(laplacian_tangents[i]) for i, node in enumerate(nodes)}
        return curvatures
