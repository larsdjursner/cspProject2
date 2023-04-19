import cupy as cp
import numpy as np

import time

# Define matrix multiplication function for CuPy
def cupy_matmul(a, b):
    return cp.matmul(a, b)

def run_tests(test_cases):
    cupy_results = []

    runs_per_testcase = 10
    sizes = [j*1000 for j in range(1, runs_per_testcase+1)]

    print('Running cupy tests')
    for size in sizes:
        results = []
        print('Current size: ' + str(size))
        
        for _ in range(test_cases):
            a = cp.array(np.random.rand(size, size))
            b = cp.array(np.random.rand(size, size))
            
            start = time.time()
            _ = cupy_matmul(a, b)
            # ensure that all streams have stopped before capturing time
            cp.cuda.Stream.null.synchronize()
            end = time.time()
            
            diff = end - start
            
            results.append(diff)

        average = np.mean(results)
        cupy_results.append((size, average))
    
    return cupy_results

def cp_mat_mul(test_cases):
    cupy_results = run_tests(test_cases)
    cupy_size, cupy_time = zip(*cupy_results)

    print('CuPy')
    print(cupy_results)
    print(cupy_size)
    print(cupy_time)

    return (cupy_size, cupy_time)