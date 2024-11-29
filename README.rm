
# Project Name: Custom BFS Algorithm Performance Comparison

## Overview
This project compares the performance of custom search algorithms against a standard Breadth-First Search (BFS) algorithm. The main goal is to evaluate the efficiency and accuracy of these algorithms in identifying paths or specific points in a grid-like matrix. The project simulates multiple scenarios with customizable inputs and visualizes the results for better analysis.

## Features
- Compare two approaches (`Custom Algorithm` and `BFS`) for:
  - Finding all reachable points in a grid.
  - Finding a single target point in a grid.
- Visualize grid configurations and results using `matplotlib`.
- Analyze performance metrics such as:
  - Execution time.
  - Memory usage.
  - Accuracy of results.
- Customizable grid configurations, including grid size and block probability.

## Project Structure
The project includes the following components:

### Main Scripts
- **`main.py`**:
  - Entry point for running the visualization and single-instance performance analysis.
- **`compare_find_all.py`**:
  - Compares the `find_all_custom` algorithm with `find_all_bfs` for locating all reachable points.
- **`compare_find_one.py`**:
  - Compares the `find_one_custom` algorithm with `find_one_bfs` for locating a single target point.

### Core Modules
- **`general.py`**:
  - Contains utility functions for generic algorithm application and result validation.
- **`matrix.py`**:
  - Provides a function to generate 2D matrices with customizable blocked-cell probabilities.

### Algorithms
- **`find_all_bfs.py`**:
  - Implements BFS for locating all reachable points in a grid.
- **`find_all_custom.py`**:
  - Custom algorithm for locating all reachable points with optimized operations.
- **`find_one_bfs.py`**:
  - Implements BFS for finding a single target point in a grid.
- **`find_one_custom.py`**:
  - Custom algorithm for finding a single target point with specialized logic.

## Usage

### Run the `main.py` Script:
Visualize grid configurations and evaluate a single instance.
```bash
python main.py
```

### Performance Comparison:
For comparing algorithms to find all reachable points:
```bash
python compare_find_all.py
```
For comparing algorithms to find a single target:
```bash
python compare_find_one.py
```

### Input Parameters:
- Grid size: Rows and columns.
- Start position: Starting coordinates in the grid.
- Blocked cell probability: Probability of a cell being blocked (default = 0.0005).
- Iterations: Number of test iterations for statistical analysis.

### Output:
- Performance metrics: Execution time, peak memory usage, and accuracy.
- Visualization of the grid and results (for `main.py`).

## Dependencies
- Python 3.8 or higher
- Required Libraries:
  - `numpy`
  - `matplotlib`
  - `collections`
  - `tracemalloc`
  - `time`

## How It Works
1. **Matrix Generation**:
   - A 2D array is created where each cell is either:
     - Blocked (`1`) based on the probability.
     - Free (`0`).

2. **Algorithm Execution**:
   - Algorithms traverse the grid from the start position and perform their respective tasks:
     - **Custom Algorithms** leverage optimized heuristics.
     - **BFS Algorithms** use traditional breadth-first traversal.

3. **Performance Tracking**:
   - Execution time and memory usage are logged for comparison.
   - Results are validated for correctness.

4. **Visualization**:
   - The grid is plotted, highlighting:
     - Free slots (green).
     - Blocked slots (red).
     - Best slot found (blue).

## Example
### Finding All Reachable Points:
```bash
python compare_find_all.py
```
Input:
```
Enter the number of rows: 10
Enter the number of columns: 10
Enter the starting x coordinate: 0
Enter the starting y coordinate: 0
Enter the probability of a cell being blocked: 0.1
Enter the number of iterations: 5
```
Output:
- Algorithm performance metrics (execution time, memory usage, accuracy).
- Summary of results.

### Visualizing Results:
```bash
python main.py
```
Result:
- A color-coded grid with results displayed in a GUI.

## License
This project is released under the MIT License.

## Contributions
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## Contact
For queries or suggestions, feel free to reach out.
