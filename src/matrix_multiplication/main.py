
from matrix_multiplication.np_mat_mul import np_mat_mul
from utils import plot


def matmul(test_cases, sizes):
    from matrix_multiplication.cp_mat_mul import cp_mat_mul

    numpy_size, numpy_time = np_mat_mul(test_cases, sizes)
    cupy_size, cupy_time = cp_mat_mul(test_cases, sizes)

    numpy_res = ("numpy", numpy_size, numpy_time)
    cupy_res = ("cupy", cupy_size, cupy_time)

    results = [numpy_res, cupy_res]

    plot("Matrix multiplication", "Matrix Size",
         "Time in ms", results, "matmul_time.png")

    numpy_troughput = [size / time for size,
                       time in zip(numpy_size, numpy_time)]
    cupy_troughput = [size / time for size, time in zip(cupy_size, cupy_time)]

    plot("Matrix multiplication", "Matrix Size", "Troughput in datasize/ms",
         [("numpy", numpy_size, numpy_troughput), ("cupy", cupy_size, cupy_troughput)], "matmul_troughput.png")
