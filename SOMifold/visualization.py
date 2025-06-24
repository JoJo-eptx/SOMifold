import matplotlib.pyplot as plt
import plotly.express as px
import networkx as nx

def plot_data_and_lattice(data_xy, lattice_nodes):
    fig = px.scatter(x=data_xy[:, 0], y=data_xy[:, 1], width=800, height=800)
    fig.update_traces(marker=dict(color='blue'))
    fig.add_trace(px.scatter(x=lattice_nodes[:, 0], y=lattice_nodes[:, 1]).data[0])
    fig.data[1].update(marker=dict(color='red'))
    fig.show()

def visualize_graph(G):
    pos = {node: node for node in G.nodes()}
    nx.draw(G, pos, with_labels=False, node_size=18, node_color="skyblue", edge_color="gray", linewidths=0.5)
    plt.show()
