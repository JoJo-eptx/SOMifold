import os
import pickle

class GraphLoader:
    """Loads graphs from .gpickle files in a directory."""

    def __init__(self, directory='.'):
        self.directory = directory
        self.filenames = []

    def load_graphs(self):
        files = [f for f in os.listdir(self.directory) if f.endswith('.gpickle')]
        graphs = []
        for f in files:
            with open(os.path.join(self.directory, f), 'rb') as file:
                graph = pickle.load(file)
                graphs.append(graph)
        self.filenames = files
        return graphs
