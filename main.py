import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

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

    array = None
    if prob.strip() == '':
        array = create_2d_array(rows, cols)
    else:
        array = create_2d_array(rows, cols, float(prob))
    print("Done creating array")

    correct, result, distance, _, _ = apply_generic_algorithm(find_all_custom, array, start_x, start_y)

    print(f"Correct: {correct}")

    if correct:
        print(f"Distance: {distance}")
        if len(result) > 0:
            print(f"Best result: {result[0]}")
            array[result[0][0]][result[0][1]] = 2
        print(f"Result: {result}")


        # Colors corresponding to 0: green, 1: red, 2: blue
        cmap = ListedColormap(['green', 'red', 'blue'])

        # Create the plot
        plt.figure(figsize=(cols, rows))
        plt.imshow(array, cmap=cmap, origin='upper')

        # Add a colorbar with labels for clarity
        cbar = plt.colorbar(ticks=[0, 1, 2])
        cbar.ax.set_yticklabels(['Empty Slots', 'Blocked Slots', 'Best Slot'])

        # Add gridlines and labels if needed
        plt.grid(which='major', color='black', linestyle='-', linewidth=0.5)
        plt.xticks(ticks=range(array.shape[1]), labels=[])  # Keep ticks but remove labels for columns
        plt.yticks(ticks=range(array.shape[0]), labels=[])  # Keep ticks but remove labels for rows

        plt.title("Park Area with Slots")
        if len(result) > 0:
            plt.title(f"Park Area with Slots\nBest Slot: {result[0]}, Distance: {distance}")
        else:
            plt.title("Park Area with Slots\nNo best slot found")

plt.show()