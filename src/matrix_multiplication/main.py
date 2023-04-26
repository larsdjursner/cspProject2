import matplotlib.pyplot as plt
from matrix_multiplication.np_mat_mul import np_mat_mul
from utils import plot

def matmul(test_cases, sizes, test = False):
    if test:
        run_numpy_test(test_cases, sizes)
        return

    from matrix_multiplication.cp_mat_mul import cp_mat_mul
    
    numpy_size, numpy_time = np_mat_mul(test_cases, sizes)
    cupy_size, cupy_time = cp_mat_mul(test_cases, sizes)

    numpy_res = ("numpy", numpy_size, numpy_time)
    cupy_res = ("cupy", cupy_size, cupy_time)

    results = [numpy_res, cupy_res]

    plot("Matrix multiplication", "Matrix Size", "Time in seconds", results, "matmul.png")

def run_numpy_test(test_cases, sizes):
    numpy_size, numpy_time = np_mat_mul(test_cases, sizes)
    numpy_res = ("numpy", numpy_size, numpy_time)

    results = [numpy_res]
    
    plot("Matrix multiplication", "Matrix Size", "Time in seconds", results, "matmul.png")
