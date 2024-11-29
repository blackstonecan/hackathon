import numpy as np

def create_2d_array(rows, cols, prob=0.0005):
    # Generate a 2D array of random floats between 0 and 1
    random_values = np.random.random((rows, cols))
    # Use NumPy's vectorized operations to create the array with 0s and 1s
    arr = np.where(random_values < prob, 0, 1)
    return arr