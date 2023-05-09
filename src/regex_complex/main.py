from regex_complex.cudf_regex_complex import cudf_regex_complex
from regex_complex.pandas_regex_complex import pandas_regex_complex
from utils import plot


def regex_complex(testcases):
    cudf_size, cudf_time = cudf_regex_complex(testcases)
    pandas_size, pandas_time = pandas_regex_complex(testcases)

    cu = ("cudf", cudf_size, cudf_time)
    pd = ("pandas", pandas_size, pandas_time)

    results = [pd, cu]

    plot("regex_complex", "Size", "Time in ms",
         results, "regex_complex_time.png")

    pd_throughput = [size / time for size,
                     time in zip(pandas_size, pandas_time)]
    cu_throughput = [size / time for size, time in zip(cudf_size, cudf_time)]

    tp_results = [("pandas", pandas_size, pd_throughput),
                  ("cudf", cudf_size, cu_throughput)]

    plot("regex_complex", "Size", "Throughput in bytes/ms",
         tp_results, "regex_complex_throughput.png", base=2, isThroughput=True)
