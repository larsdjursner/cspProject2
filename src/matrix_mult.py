import numpy as np
import cupy as cp
import time
import sys
import matplotlib.pyplot as plt

# Define matrix multiplication function for NumPy
def numpy_matmul(a, b):
    return np.matmul(a, b)

# Define matrix multiplication function for CuPy
def cupy_matmul(a, b):
    return cp.matmul(a, b)


def run_tests(test_cases):
    # Results
    numpy_results = []
    cupy_results = []

    # NumPy
    runs_per_testcase = 10
    sizes = [j*1000 for j in range(1, runs_per_testcase+1)]

    for size in sizes:
        results = []
        
        for _ in range(test_cases):
            # Generate test data
            a = np.random.rand(size, size)
            b = np.random.rand(size, size)

            start = time.time()
            # run numpy matrix mult
            _ = numpy_matmul(a, b)
            end = time.time()
            
            diff = end - start
            
            results.append(diff)

        average = np.mean(results)
        numpy_results.append((size, average))

    # CuPy
    runs_per_testcase = 10
    sizes = [j*1000 for j in range(1, runs_per_testcase+1)]

    for size in sizes:
        results = []
        
        for _ in range(test_cases):
            # Generate test data
            a = np.random.rand(size, size)
            b = np.random.rand(size, size)

            start = time.time()
            # run cupy matrix mult
            _ = cupy_matmul(a, b)

            # ensure that all streams have stopped before capturing time
            cp.cuda.Stream.null.synchronize()
            end = time.time()
            
            diff = end - start
            
            results.append(diff)

        average = np.mean(results)
        cupy_results.append((size, average))
    
    return numpy_results, cupy_results

if __name__ == "__main__":
    test_cases = 10
    numpy_results, cupy_results = run_tests(test_cases)

    numpy_size, numpy_time = zip(*numpy_results)
    cupy_size, cupy_time = zip(*cupy_results)

    print('NumPy')
    print(numpy_results)
    print(numpy_size)
    print(numpy_time)

    print('CuPy')
    print(numpy_results)
    print(numpy_size)
    print(numpy_time)

    plt.plot(numpy_size, numpy_time)
    plt.savefig('numpy.png')

    plt.plot(cupy_size, cupy_time)
    plt.savefig('cupy.png')