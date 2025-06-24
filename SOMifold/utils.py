import pickle

def save_graph(graph, filename):
    with open(filename, "wb") as f:
        pickle.dump(graph, f)

def load_graph(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
