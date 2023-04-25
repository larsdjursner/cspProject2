import matplotlib.pyplot as plt
from matrix_multiplication.cp_mat_mul import cp_mat_mul
from matrix_multiplication.np_mat_mul import np_mat_mul

def matmul(test_cases):
    numpy_size, numpy_time = np_mat_mul(test_cases)
    cupy_size, cupy_time = cp_mat_mul(test_cases)

    plt.title("Matrix multiplication")
    plt.xlabel("Matrix Size")
    plt.ylabel("Time in seconds")
    
    plt.plot(numpy_size, numpy_time, label="numpy")
    plt.plot(cupy_size, cupy_time, label="cupy")
    plt.legend(loc="upper left")

    plt.savefig('matmul.png')
