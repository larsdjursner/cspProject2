import numpy as np
import time 
import random

def run_tests(test_cases, sizes):
    ### Numpy and CPU
    numpy_results = []
    
    for size in sizes:
        results = []

        for _ in range(test_cases):
            x = np.ones(shape=(size, size))
            rand = random.randint(1, 1000)
            start = time.time()
            y = np.multiply(x, rand)
            y.size
            end = time.time()
            diff = (end - start)*1000 # convert to milliseconds
            results.append(diff)

        average = np.mean(results)
        numpy_results.append((size*size, average))
    return numpy_results

def np_el_mult(test_cases, sizes):
    numpy_results = run_tests(test_cases, sizes)
    numpy_size, numpy_time = zip(*numpy_results)

    return (numpy_size, numpy_time)