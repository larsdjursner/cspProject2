import numpy as np
import time

# Define matrix multiplication function for NumPy
def numpy_matmul(a, b):
    return np.matmul(a, b)

def run_tests(test_cases, sizes):
    numpy_results = []

    for size in sizes:
        results = []

        for _ in range(test_cases):
            a = np.random.rand(size, size)
            b = np.random.rand(size, size)

            start = time.time()
            x = numpy_matmul(a, b)
            x.size
            end = time.time()
            
            diff = (end - start)*1000 # convert to milliseconds
            
            results.append(diff)

        average = np.mean(results)
        numpy_results.append((size*size, average))

    return numpy_results

def np_mat_mul(test_cases, sizes):
    numpy_results = run_tests(test_cases, sizes)
    numpy_size, numpy_time = zip(*numpy_results)

    return(numpy_size, numpy_time)
