import matplotlib.pyplot as plt
from array_init.np_array_init import np_array_init
from utils import plot


def array_init(test_cases, sizes):
    from array_init.cp_array_init import cp_array_init

    numpy_size, numpy_time = np_array_init(test_cases, sizes)
    cupy_size, cupy_time = cp_array_init(test_cases, sizes)

    numpy_res = ("numpy", numpy_size, numpy_time)
    cupy_res = ("cupy", cupy_size, cupy_time)

    results = [numpy_res, cupy_res]

    plot("Matrix init", "Matrix Size", "Time in ms",
         results, "array_init_time.png")

    numpy_troughput = [size / time for size,
                       time in zip(numpy_size, numpy_time)]
    cupy_troughput = [size / time for size, time in zip(cupy_size, cupy_time)]

    tp_results = [("numpy", numpy_size, numpy_troughput),
                  ("cupy", cupy_size, cupy_troughput)]

    plot("Matrix init", "Matrix Size", "Troughput in datasize/ms",
         tp_results, "array_init_troughput.png", base=2, isThroughput=True)
