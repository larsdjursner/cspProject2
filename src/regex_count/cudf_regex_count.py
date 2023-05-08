import cudf as cd
import cupy as cp
import numpy as np
import os
import glob


def run_tests(test_cases):
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, '../texts/')

    file_extension = "*.csv"
    cudf_results = []
    for file_name in glob.glob(os.path.join(path, file_extension)):
        df = cd.read_csv(file_name)
        pattern = r'\b([Tt][Hh][Ee]|[Bb][Ee]|[Tt][Oo]|[Oo][Ff]|[Aa][Nn][Dd]|[Ii][Nn]|[Tt][Hh][Aa][Tt]|[Hh][Aa][Vv][Ee]|[Ii][Tt]|[Ff][Oo][Rr])\b'
        results = []

        for _ in range(test_cases):
            start = cp.cuda.Event()
            end = cp.cuda.Event()

            start.record()

            desc = df['Description'].str.contains(pattern)
            title = df['Title'].str.contains(pattern)

            end.record()
            end.synchronize()
            diff = cp.cuda.get_elapsed_time(start, end)

            total = desc.sum() + title.sum()
            results.append(diff)
            total = None

            cp.get_default_memory_pool().free_all_blocks()

        average = np.mean(results)
        cudf_results.append((os.stat(file_name).st_size, average))

    return cudf_results


def cudf_regex_count(test_cases):
    cudf_results = run_tests(test_cases)
    cudf_size, cudf_time = zip(*cudf_results)
    return (cudf_size, cudf_time)


# if __name__ == "__main__":
#     print(cudf_regex_count(10))
