from matrix_multiplication.main import matmul
from elementwise_mult.main import el_mult
from array_init.main import array_init

if __name__ == "__main__":
    test_cases = 10
    sizes = [2**i for i in range(1, 13)]
    
    array_init(test_cases=test_cases, sizes=sizes)
    el_mult(test_cases=test_cases, sizes=sizes)
    matmul(test_cases=test_cases, sizes=sizes)