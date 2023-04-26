import matplotlib.pyplot as plt
from array_init.np_array_init import np_array_init
from utils import plot

def array_init(test_cases, sizes, test = False):
    if test:
        run_numpy_test(test_cases, sizes)
        return

    from array_init.cp_array_init import cp_array_init

    numpy_size, numpy_time = np_array_init(test_cases, sizes)
    cupy_size, cupy_time = cp_array_init(test_cases, sizes)

    numpy_res = ("numpy", numpy_size, numpy_time)
    cupy_res = ("cupy", cupy_size, cupy_time)

    results = [numpy_res, cupy_res]

    plot("Matrix init", "Matrix Size", "Time in seconds", results, "array_init.png")

def run_numpy_test(test_cases, sizes):
    numpy_size, numpy_time = np_array_init(test_cases, sizes)
    numpy_res = ("numpy", numpy_size, numpy_time)
    
    results = [numpy_res]
    
    plot("Matrix init", "Matrix Size", "Time in seconds", results, "array_init.png")
