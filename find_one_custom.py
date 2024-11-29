def find_one_custom(array, start_x, start_y):
    arr_x = len(array)
    arr_y = len(array[0])

    def is_valid(x, y):
        return x >= 0 and x < arr_x and y >= 0 and y < arr_y
    
    if array[start_x][start_y] == 0:
        return [(start_x, start_y)]

    nodes = [(start_x + 1, start_y), (start_x - 1, start_y), (start_x, start_y + 1), (start_x, start_y - 1)]
    nodes = [(x, y) for x, y in nodes if is_valid(x, y)]

    while len(nodes) > 0:
        x, y = nodes.pop(0)

        # Check if the current node is finish
        if array[x][y] == 0:
            return [(x, y)]

        # Check x's direction
        if (x > start_x):
            if x + 1 < arr_x: # validation
                nodes.append((x + 1, y))
        elif (x < start_x):
            if x - 1 >= 0: # validation
                nodes.append((x - 1, y))
        # Check y's direction
        elif (x == start_x):
            # Add left and right nodes
            if (x + 1 < arr_x):
                nodes.append((x + 1, y))
            if (x - 1 >= 0):
                nodes.append((x - 1, y))

            # Add up and down nodes
            if (y > start_y and y + 1 < arr_y):
                nodes.append((x, y + 1))
            if (y < start_y and y - 1 >= 0):
                nodes.append((x, y - 1))

    return []