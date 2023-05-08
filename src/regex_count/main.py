from regex_count.cudf_regex_count import cudf_regex_count
from regex_count.pandas_regex_count import pandas_regex_count
from utils import plot

def regex_count(testcases):
    cudf_size, cudf_time = cudf_regex_count(testcases)
    pandas_size, pandas_time = pandas_regex_count(testcases)

    cu = ("cudf", cudf_size, cudf_time)
    pd = ("pandas", pandas_size, pandas_time)

    results = [pd, cu]

    plot("regex_count", "Size", "Time in ms", results, "regex_count_time.png")
    
    pd_throughput = [size / time for size, time in zip(pandas_size, pandas_time)]
    cu_throughput = [size / time for size, time in zip(cudf_size, cudf_time)]

    plot("regex_count", "Size", "Throughput in bytes/ms", [("pandas", pandas_size, pd_throughput), ("cudf", cudf_size, cu_throughput)], "regex_count_throughput.png")
