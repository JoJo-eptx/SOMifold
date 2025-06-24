from data_processing import load_and_clean_data
from preprocessing import compute_grid_size, scale_coordinates, compute_severity_weights
from som_model import create_hexagonal_grid, train_som, create_graph_from_weights
from visualization import plot_data_and_lattice, visualize_graph
from utils import save_graph
import numpy as np

def main():
    file_path = 'data/2020_2025_CRIS.csv'
    df = load_and_clean_data(file_path)
    
    grid_size = compute_grid_size(len(df))
    df = compute_severity_weights(df)
    
    scaled_xy, scaler = scale_coordinates(df, grid_size)
    
    lattice = create_hexagonal_grid(grid_size)
    plot_data_and_lattice(scaled_xy, np.array(lattice.nodes()))
    
    som = train_som(lattice, scaled_xy, epochs=grid_size)
    
    topology = create_graph_from_weights(som.som_graph, som.weights)
    visualize_graph(topology)
    
    # save_graph(topology, "B - SUSPECTED MINOR INJURY.gpickle")

if __name__ == "__main__":
    main()
