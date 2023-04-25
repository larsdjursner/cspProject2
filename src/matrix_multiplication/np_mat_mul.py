import numpy as np
import time

# Define matrix multiplication function for NumPy
def numpy_matmul(a, b):
    return np.matmul(a, b)

def run_tests(test_cases):
    numpy_results = []

    runs_per_testcase = 10
    sizes = [j*1000 for j in range(1, runs_per_testcase+1)]

    for size in sizes:
        results = []

        for _ in range(test_cases):
            a = np.random.rand(size, size)
            b = np.random.rand(size, size)

            start = time.time()
            _ = numpy_matmul(a, b)
            end = time.time()
            
            diff = end - start
            
            results.append(diff)

        average = np.mean(results)
        numpy_results.append((size*size, average))

    return numpy_results

def np_mat_mul(test_cases):
    numpy_results = run_tests(test_cases)
    numpy_size, numpy_time = zip(*numpy_results)

    return(numpy_size, numpy_time)
