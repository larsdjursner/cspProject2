import cupy as cp
import numpy as np

import time

# Define matrix multiplication function for CuPy
def cupy_matmul(a, b):
    return cp.matmul(a, b)

def run_tests(test_cases, sizes):
    cupy_results = []

    for size in sizes:
        results = []
        
        for _ in range(test_cases):
            a = cp.array(np.random.rand(size, size))
            b = cp.array(np.random.rand(size, size))
            
            start = time.time()
            x = cupy_matmul(a, b)
            x.size
            # ensure that all streams have stopped before capturing time
            cp.cuda.Stream.null.synchronize()
            end = time.time()
            
            diff = (end - start)*1000 # convert to milliseconds
            
            results.append(diff)
            a = None
            b = None
            x = None
            cp.get_default_memory_pool().free_all_blocks()

        average = np.mean(results)
        cupy_results.append((size*size, average))
    
    return cupy_results

def cp_mat_mul(test_cases, sizes):
    cupy_results = run_tests(test_cases, sizes)
    cupy_size, cupy_time = zip(*cupy_results)

    return (cupy_size, cupy_time)
