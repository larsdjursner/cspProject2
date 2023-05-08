import matplotlib.pyplot as plt
from elementwise_mult.np_el_mult import np_el_mult
from utils import plot


def el_mult(test_cases, sizes):
    from elementwise_mult.cp_el_mult import cp_el_mult

    numpy_size, numpy_time = np_el_mult(test_cases, sizes)
    cupy_size, cupy_time = cp_el_mult(test_cases, sizes)

    numpy_res = ("numpy", numpy_size, numpy_time)
    cupy_res = ("cupy", cupy_size, cupy_time)

    results = [numpy_res, cupy_res]

    plot("Elementwise Multiplication", "Matrix Size",
         "Time in ms", results, "elementwise_mult_time.png")

    numpy_troughput = [size / time for size,
                       time in zip(numpy_size, numpy_time)]
    cupy_troughput = [size / time for size, time in zip(cupy_size, cupy_time)]

    plot("Elementwise Multiplication", "Matrix Size", "Troughput in datasize/ms",
         [("numpy", numpy_size, numpy_troughput), ("cupy", cupy_size, cupy_troughput)], "elementwise_mult_troughput.png")
