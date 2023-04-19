import np_mat_mul
import cp_mat_mul

if __name__ == "__main__":
    test_cases = 10
    numpy_size, numpy_time = np_mat_mul.np_mat_mul(test_cases)
    cupy_size, cupy_time = cp_mat_mul.cp_mat_mul(test_cases)

    plt.plot(numpy_size, numpy_time)
    plt.savefig('numpy.png')

    plt.plot(cupy_size, cupy_time)
    plt.savefig('cupy.png')
