import cudf as cd
import cupy as cp
import numpy as np
import os
import glob

def run_tests(test_cases):
    path = "/home/tovs/cspProject2/src/texts" 
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

            desc = df['Description'].str.replace(pattern, "awesome", regex=True)
            title = df['Title'].str.replace(pattern, "awesome", regex=True)


            end.record()
            end.synchronize()

            diff = cp.cuda.get_elapsed_time(start, end)  

            total = desc.sum() + title.sum()

            results.append(diff)

            total = None

            cp.get_default_memory_pool().free_all_blocks()
    
        average = np.mean(results)
        cudf_results.append((os.path.getsize(os.path.join(path, file_name)),average))

    return cudf_results

def cudf_regex_replace(test_cases):
    cudf_results = run_tests(test_cases)
    cudf_size, cudf_time = zip(*cudf_results)

    return (cudf_size, cudf_time)

if __name__ == "__main__":
    print(cudf_regex_replace(1))