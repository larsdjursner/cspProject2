import sys
from matrix_multiplication.main import matmul
from elementwise_mult.main import el_mult
from array_init.main import array_init
from regex_count.main import regex_count
from regex_replace.main import regex_replace
from regex_complex.main import regex_complex


def main():

    test_cases = 10
    sizes = [2**i for i in range(1, 13)]

    # array_init(test_cases=test_cases, sizes=sizes)
    # el_mult(test_cases=test_cases, sizes=sizes)
    # matmul(test_cases=test_cases, sizes=sizes)
    # regex_count(test_cases)
    regex_replace(test_cases)
    # regex_complex(test_cases)


if __name__ == "__main__":
    main()
