import cupy as cp
import numpy as np
import time 

def run_tests(test_cases, sizes):
    ### Cupy and GPU
    cupy_results = []
    
    for size in sizes:
        results = []

        for _ in range(test_cases):
            start = time.time()

            start = cp.cuda.Event()
            end = cp.cuda.Event()

            start.record()

            x = cp.ones(shape=(size, size))
            x.size

            end.record()
            end.synchronize()

            diff = cp.cuda.get_elapsed_time(start, end)  
         
            results.append(diff)
            x = None
            cp.get_default_memory_pool().free_all_blocks()


        average = np.mean(results)
        cupy_results.append((size*size, average))
    
    return cupy_results


def cp_array_init(test_cases, sizes):
    cupy_results = run_tests(test_cases, sizes)
    cupy_size, cupy_time = zip(*cupy_results)

    return (cupy_size, cupy_time)