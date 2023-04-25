import numpy as np
import time 

def run_tests(test_cases, sizes):
    ### Numpy and CPU
    numpy_results = []
    
    for size in sizes:
        results = []

        for _ in range(test_cases):
            start = time.time()
            _ = np.ones(shape=(size, size))
            end = time.time()
            results.append(end - start)

        average = np.mean(results)
        numpy_results.append((size*size, average))
    return numpy_results

def np_array_init(test_cases, sizes):
    numpy_results = run_tests(test_cases, sizes)
    numpy_size, numpy_time = zip(*numpy_results)

    return (numpy_size, numpy_time)