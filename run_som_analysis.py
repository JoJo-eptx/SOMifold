from SOMifold.data_processing import load_and_clean_data
from SOMifold.preprocessing import compute_grid_size, scale_coordinates, compute_severity_weights
from SOMifold.som_model import create_hexagonal_grid, train_som, create_graph_from_weights
from SOMifold.visualization import plot_data_and_lattice, visualize_graph
from SOMifold.utils import save_graph
from SOMifold.graph_loader import GraphLoader
from SOMifold.curvature_calculator import CurvatureCalculator
from SOMifold.difference_graph_builder import DifferenceGraphBuilder
from SOMifold.node_data_processor import NodeDataProcessor
from SOMifold.plotter import Plotter
from SOMifold.reg_som_trainer import RegSOMTrainer
from scipy.special import softmax
import numpy as np
import os

import pdb

def main():
    severities = [
        'K - FATAL INJURY',
        'A - SUSPECTED SERIOUS INJURY',
        'B - SUSPECTED MINOR INJURY'
    ]
    
    file_path = 'data/2020_2025_CRIS.csv'
    df = load_and_clean_data(file_path)

    scaler = None  # Initialize scaler for coordinate scaling

    for severity in severities:
        print(f"\nProcessing severity: {severity}")

        # Construct filename and check if it already exists
        output_filename = severity.replace(' ', '_') + ".gpickle"
        if os.path.exists(output_filename):
            print(f"✔ File already exists: {output_filename}, skipping.")
            continue

        # Filter data
        df_filtered = df.query("`Person Type` not in ['4 - PEDESTRIAN', '3 - PEDALCYCLIST'] and `On System Flag` == 'No'")
        df_filtered = df_filtered.query("`Crash Severity` == @severity")

        if df_filtered.empty:
            print(f"⚠ No data for severity: {severity}")
            continue

        # Continue with processing
        grid_size = compute_grid_size(len(df_filtered))
        df_filtered = compute_severity_weights(df_filtered)

        scaled_xy, scaler = scale_coordinates(df_filtered, grid_size)

        lattice = create_hexagonal_grid(grid_size)
        plot_data_and_lattice(scaled_xy, np.array(lattice.nodes()))

        som = train_som(lattice, scaled_xy, epochs=grid_size)

        topology = create_graph_from_weights(som.som_graph, som.weights)
        visualize_graph(topology)

        save_graph(topology, output_filename)
        print(f"✅ Saved graph: {output_filename}")

    # Load graphs using GraphLoader
    loader = GraphLoader()
    graphs = loader.load_graphs()

    # Compute curvature for each graph
    curvature_calc = CurvatureCalculator()
    all_curvatures = []
    for graph in graphs:
        tangent_vectors = curvature_calc.compute_tangent_vectors(graph)
        curvatures = curvature_calc.compute_curvature(graph, tangent_vectors)
        all_curvatures.append(curvatures)

    # Create difference graphs
    diff_builder = DifferenceGraphBuilder()
    difference_graphs = [diff_builder.create_difference_graph(g) for g in graphs]

    # Process node data from difference graphs
    processor = NodeDataProcessor()
    node_arrays = [processor.get_node_data_as_array(g) for g in difference_graphs]
    processed_arrays = [processor.process_node_array(arr) for arr in node_arrays]

    # Monetize and apply weights
    monetize_vals = np.array([246900, 1254700, 132000000])
    log_weights = np.log(monetize_vals)
    log_weights = log_weights/np.max(log_weights)  # Normalize log weights
    weights = softmax(log_weights)

    # Apply weights and stack arrays
    weighted_arrays = processor.apply_weights(processed_arrays, weights)
    summed_array = processor.stack_and_sum(weighted_arrays)

    # Create a new hexagonal grid for visualization
    grid_size = 60
    lattice = create_hexagonal_grid(grid_size)
    lattice_nodes = np.array(lattice.nodes())

    # Plot the results
    plotter = Plotter(lattice_nodes)
    titles = [f.replace('.gpickle', '') for f in loader.filenames]
    plotter.plot_node_arrays(weighted_arrays, titles)
    plotter.plot_weighted_sum(summed_array)
    plotter.show_all()

    # Save the summed array as a new graph
    som_trainer = RegSOMTrainer(lattice, learning_rate=0.01)
    som_trainer.set_weights(summed_array)
    som_trainer.save("ABK - WEIGHTED SUM CURVATURE.gpickle")

if __name__ == "__main__":
    main()

