import matplotlib.pyplot as plt
from elementwise_mult.np_el_mult import np_el_mult
from utils import plot

def el_mult(test_cases, sizes, test = False):
    if test:
        run_numpy_test(test_cases, sizes)
        return
    
    from elementwise_mult.cp_el_mult import cp_el_mult

    numpy_size, numpy_time = np_el_mult(test_cases, sizes)
    cupy_size, cupy_time = cp_el_mult(test_cases, sizes)

    numpy_res = ("numpy", numpy_size, numpy_time)
    cupy_res = ("cupy", cupy_size, cupy_time)

    results = [numpy_res, cupy_res]

    plot("Elementwise Multiplication", "Matrix Size", "Time in seconds", results, "elementwise_mult.png")


def run_numpy_test(test_cases, sizes):
    numpy_size, numpy_time = np_el_mult(test_cases, sizes)
    numpy_res = ("numpy", numpy_size, numpy_time)

    results = [numpy_res]
    
    plot("Elementwise Multiplication", "Matrix Size", "Time in seconds", results, "elementwise_mult.png")

    
    