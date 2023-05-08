from regex_replace.cudf_regex_replace import cudf_regex_replace
from regex_replace.pandas_regex_replace import pandas_regex_replace
from utils import plot


def regex_replace(testcases):
    cudf_size, cudf_time = cudf_regex_replace(testcases)
    pandas_size, pandas_time = pandas_regex_replace(testcases)

    cu = ("cudf", cudf_size, cudf_time)
    pd = ("pandas", pandas_size, pandas_time)

    results = [pd, cu]

    plot("regex_replace", "Size", "Time in ms",
         results, "regex_replace_time.png")

    pd_throughput = [size / time for size,
                     time in zip(pandas_size, pandas_time)]
    cu_throughput = [size / time for size, time in zip(cudf_size, cudf_time)]

    tp_results = [("pandas", pandas_size, pd_throughput),
                  ("cudf", cudf_size, cu_throughput)]

    plot("regex_replace", "Size", "Throughput in bytes/ms",
         tp_results, "regex_replace_throughput.png", base=2, isThroughput=True)
