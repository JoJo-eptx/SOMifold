import numpy as np
from sklearn.preprocessing import MinMaxScaler

def compute_grid_size(n_points: int) -> int:
    # Optional: parameterize or compute dynamically
    return 60

def scale_coordinates(df, grid_size: int):
    scaler = MinMaxScaler(feature_range=(0, grid_size))
    xy = np.vstack((df.Longitude, df.Latitude)).T
    scaled_xy = scaler.fit_transform(xy)
    return scaled_xy, scaler

def compute_severity_weights(df):
    monetized_values = np.array([5300, 118000, 246900, 1254700, 132000000, 229000])
    severity_labels = ['N - NOT INJURED', 'C - POSSIBLE INJURY', 
                       'B - SUSPECTED MINOR INJURY', 'A - SUSPECTED SERIOUS INJURY',
                       'K - FATAL INJURY', '99 - UNKNOWN']

    log_vals = np.log(monetized_values + 1).reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0.8, 1.8))
    scaled_log_vals = scaler.fit_transform(log_vals).flatten()

    severity_to_logval = dict(zip(severity_labels, scaled_log_vals))
    df['log_monetized_value'] = df['Crash Severity'].map(severity_to_logval)
    return df
