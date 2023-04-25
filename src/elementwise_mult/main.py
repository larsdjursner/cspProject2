import matplotlib.pyplot as plt
from elementwise_mult.np_el_mult import np_el_mult
from elementwise_mult.cp_el_mult import cp_el_mult

def el_mult(test_cases, sizes):
    numpy_size, numpy_time = np_el_mult(test_cases, sizes)
    cupy_size, cupy_time = cp_el_mult(test_cases, sizes)

    plt.title("Elementwise Multiplication")
    plt.xlabel("Matrix Size")
    plt.ylabel("Time in seconds")
    
    plt.plot(numpy_size, numpy_time, label="numpy")
    plt.plot(cupy_size, cupy_time, label="cupy")
    plt.legend(loc="upper left")

    plt.savefig('elementwise_mult.png')
    plt.clf()
