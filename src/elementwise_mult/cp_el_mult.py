import cupy as cp
import numpy as np

import time 
import random

def run_tests(test_cases, sizes):
    ### Cupy and GPU
    cupy_results = []
    
    for size in sizes:
        results = []

        for _ in range(test_cases):
            x = cp.ones(shape=(size, size))
            rand = random.randint(1, 1000)
            start = time.time()
            y = cp.multiply(x, rand)
            y.size
            end = time.time()
            results.append(end - start)

        average = np.mean(results)
        cupy_results.append((size*size, average))
        
    return cupy_results

def cp_el_mult(test_cases, sizes):
    cupy_results = run_tests(test_cases, sizes)
    cupy_size, cupy_time = zip(*cupy_results)

    return (cupy_size, cupy_time)