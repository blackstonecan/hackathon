import time
import tracemalloc

def check_result(array, result):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0 and (i, j) not in result:
                return False
            
    return True


def apply_generic_algorithm(algorithm_func, array, start_x, start_y, find_one=True):
    tracemalloc.start()
    start_time = time.time()
    result = algorithm_func(array, start_x, start_y)
    execution_time = time.time() - start_time
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    if len(result) == 0:
        return check_result(array, []) ,[], None, execution_time, peak
    best = result[0]

    correct = False
    if find_one:
        correct = array[best[0]][best[1]] == 0
    else:
        correct = check_result(array, result)
    
    distance = abs(best[0] - start_x) + abs(best[1] - start_y)
    return correct, result, distance, execution_time, peak