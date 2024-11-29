from find_all_bfs import find_all_bfs
from find_all_custom import find_all_custom

from general import apply_generic_algorithm
from matrix import create_2d_array

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    start_x = int(input("Enter the starting x coordinate: "))
    start_y = int(input("Enter the starting y coordinate: "))

    if rows < 1 or cols < 1 or start_x < 0 or start_x >= rows or start_y < 0 or start_y >= cols:
        print("Invalid input")
        exit(0)

    prob = input("Enter the probability of a cell being blocked (default=0.0005): ")



    count = int(input("Enter the number of iterations: "))
    if count < 1:
        print("Invalid input")
        exit(0)

    total_execution_time_custom = 0
    total_execution_time_bfs = 0

    total_peak_memory_custom = 0
    total_peak_memory_bfs = 0

    array = None
    for i in range(count):
        print(f"Progress: {i} / {count}")

        if prob.strip() == '':
            array = create_2d_array(rows, cols)
        else:
            array = create_2d_array(rows, cols, float(prob))
        print("Done creating array")

        correct_custom, result_custom, distance_custom, time_custom, peak_custom = apply_generic_algorithm(find_all_custom, array, start_x, start_y)
        correct_bfs, result_bfs, distance_bfs, time_bfs, peak_bfs = apply_generic_algorithm(find_all_bfs, array, start_x, start_y)

        print(f"Correct: {correct_custom}, BFS: {correct_bfs}")
        print(f"Algorithm: {result_custom[0]}, BFS: {result_bfs[0]}")
        print(f"Algorithm Distance: {distance_custom}, BFS Distance: {distance_bfs}")
        print(f"Algorithm Time: {time_custom:.6f} seconds, BFS Time: {time_bfs:.6f} seconds")
        print(f"Algorithm Peak Memory: {peak_custom / 1024:.2f} KB, BFS Peak Memory: {peak_bfs / 1024:.2f} KB")
        print("-" * 50)

        total_execution_time_custom += time_custom
        total_execution_time_bfs += time_bfs

        total_peak_memory_custom += peak_custom
        total_peak_memory_bfs += peak_bfs

    print("-" * 50)

    print(f"Total Algorithm Time: {total_execution_time_custom:.6f} seconds")
    print(f"Total BFS Time: {total_execution_time_bfs:.6f} seconds")
    print(f"Average Algorithm Time: {total_execution_time_custom / count:.6f} seconds")
    print(f"Average BFS Time: {total_execution_time_bfs / count:.6f} seconds")
    print(f"Algorithm is {100 * (total_execution_time_bfs - total_execution_time_custom) / total_execution_time_bfs:.2f}% better than BFS")

    print("-" * 50)

    print(f"Total Algorithm Memory: Peak: {total_peak_memory_custom / 1024:.2f} KB")
    print(f"Total BFS Memory: Peak: {total_peak_memory_bfs / 1024:.2f} KB")
    print(f"Average Algorithm Memory: Peak: {total_peak_memory_custom / 1024 / count:.2f} KB")
    print(f"Average BFS Memory: Peak: {total_peak_memory_bfs / 1024 / count:.2f} KB")
    print(f"Algorithm is {100 * (total_peak_memory_bfs - total_peak_memory_custom) / total_peak_memory_bfs:.2f}% better than BFS")