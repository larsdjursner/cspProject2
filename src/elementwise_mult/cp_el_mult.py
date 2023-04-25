import cupy as cp
import numpy as np

import time 
import random

def run_tests(test_cases):
    ### Cupy and GPU
    cupy_results = []

    runs_per_testcase = 10
    sizes = [j*1000 for j in range(1, runs_per_testcase+1)]
    
    for size in sizes:
        results = []

        for _ in range(test_cases):
            x = cp.ones(shape=(size, size))
            rand = random.randint(1, 1000)
            start = time.time()
            cp.multiply(x, rand)
            end = time.time()
            results.append(end - start)

        average = np.mean(results)
        cupy_results.append((size*size, average))
        
    return cupy_results

def cp_el_mult(test_cases):
    cupy_results = run_tests(test_cases)
    cupy_size, cupy_time = zip(*cupy_results)

    return (cupy_size, cupy_time)