import plotly.express as px
import numpy as np

class Plotter:
    """Handles visualization of node data arrays on hexagonal lattice nodes using Plotly."""

    def __init__(self, lattice_nodes):
        self.lattice_nodes = lattice_nodes
        self.figures = []

    def plot_node_arrays(self, node_arrays, titles):
        for i, arr in enumerate(node_arrays):
            fig = px.scatter(
                x=self.lattice_nodes[:, 0],
                y=self.lattice_nodes[:, 1],
                color=-arr[:, 2],
                color_continuous_scale='Jet',
                width=800,
                height=800,
                labels={'x': 'X Coordinate', 'y': 'Y Coordinate', 'color': 'Curvature'},
                title=titles[i]
            )
            self.figures.append(fig)

    def plot_weighted_sum(self, summed_array):
        fig = px.scatter(
            x=self.lattice_nodes[:, 0],
            y=self.lattice_nodes[:, 1],
            color=-summed_array[:, 2],
            color_continuous_scale='Jet',
            width=800,
            height=800,
            labels={'x': 'X Coordinate', 'y': 'Y Coordinate', 'color': 'Curvature'},
            title='Weighted Sum: Curvature'
        )
        self.figures.append(fig)

    def show_all(self):
        for fig in self.figures:
            fig.show()
