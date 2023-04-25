import matplotlib.pyplot as plt
from array_init.cp_array_init import cp_array_init
from array_init.np_array_init import np_array_init

def array_init(test_cases):
    numpy_size, numpy_time = np_array_init(test_cases)
    cupy_size, cupy_time = cp_array_init(test_cases)

    plt.title("Matrix init")
    plt.xlabel("Matrix Size")
    plt.ylabel("Time in seconds")

    plt.plot(numpy_size, numpy_time, label="numpy")
    plt.plot(cupy_size, cupy_time, label="cupy")
    plt.legend(loc="upper left")

    plt.savefig('array_init.png')
