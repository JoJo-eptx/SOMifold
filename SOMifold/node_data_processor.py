import numpy as np

class NodeDataProcessor:
    """Processes node attribute arrays and monetizes curvature-related values."""

    @staticmethod
    def get_node_data_as_array(graph):
        data = []
        for node, attr in graph.nodes(data=True):
            x, y = node
            avg_diff = attr.get('avg_difference', 0)
            data.append([x, y, avg_diff])
        return np.array(data)

    @staticmethod
    def process_node_array(node_array):
        arr = node_array.copy()
        negative_vals = arr[:, 2][arr[:, 2] < 0]
        closest_to_zero = negative_vals.max() if negative_vals.size > 0 else None
        max_val = arr.max()

        if closest_to_zero is not None:
            scaled_value = max(closest_to_zero * 1.1, max_val + 1e-5)
            arr[arr < 0] *= scaled_value
            arr = np.abs(arr)

        arr[:, 2] = np.log(arr[:, 2] + 1e-12)
        return arr

    @staticmethod
    def monetize_log_values(log_column, monetized_values=np.array([246900, 1254700, 132000000])):
        log_col = np.array(log_column)
        log_min, log_max = np.min(log_col), np.max(log_col)
        scaled = (log_col - log_min) / (log_max - log_min + 1e-12)
        return scaled * (monetized_values[-1] - monetized_values[0]) + monetized_values[0]

    @staticmethod
    def apply_weights(processed_arrays, weights):
        for i, arr in enumerate(processed_arrays):
            arr[:, 2] = arr[:, 2] * weights[i]
        return processed_arrays

    @staticmethod
    def stack_and_sum(arrays):
        stacked = np.stack(arrays, axis=2)
        summed = stacked.sum(axis=2)
        return summed
