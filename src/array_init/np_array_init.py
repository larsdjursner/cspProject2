import numpy as np
import time 

def run_tests(test_cases):
    ### Numpy and CPU
    numpy_results = []

    runs_per_testcase = 10
    sizes = [j*1000 for j in range(1, runs_per_testcase+1)]
    
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

def np_array_init(test_cases):
    numpy_results = run_tests(test_cases)
    numpy_size, numpy_time = zip(*numpy_results)

    return (numpy_size, numpy_time)