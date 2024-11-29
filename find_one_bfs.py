from collections import deque

def find_one_bfs(array, start_x, start_y):
    arr_x, arr_y = len(array), len(array[0])

    if array[start_x][start_y] == 0:
        return [(start_x, start_y)]

    # BFS Initialization
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])

    # Directions for movement (right, left, down, up)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()  # Efficient pop from the left

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Check bounds and if not visited
            if 0 <= new_x < arr_x and 0 <= new_y < arr_y and (new_x, new_y) not in visited:
                if array[new_x][new_y] == 0:
                    return [(new_x, new_y)]
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))

    return []
