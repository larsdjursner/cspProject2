import numpy as np
import os
import glob
import time
import pandas as pd

def run_tests(test_cases):
    path = "/home/tovs/cspProject2/src/texts" 
    file_extension = "*.csv"
    pandas_results = []
    for file_name in glob.glob(os.path.join(path, file_extension)):
        df = pd.read_csv(file_name)
        pattern = r'\b([Tt][Hh][Ee]|[Bb][Ee]|[Tt][Oo]|[Oo][Ff]|[Aa][Nn][Dd]|[Ii][Nn]|[Tt][Hh][Aa][Tt]|[Hh][Aa][Vv][Ee]|[Ii][Tt]|[Ff][Oo][Rr])\b'
        results = []

        for _ in range(test_cases):
            start = time.time()
            
            desc = df['Description'].str.replace(pattern, "awesome", regex=True)
            title = df['Title'].str.replace(pattern, "awesome", regex=True)

            end = time.time()
            diff = (end - start) * 1000 #convert to ms

            total = desc.sum() + title.sum()
            results.append(diff)
            total = None
        
        average = np.mean(results)
        pandas_results.append((os.stat(file_name).st_size, average))

    return pandas_results

def pandas_regex_replace(test_cases):
    pandas_results = run_tests(test_cases)
    pandas_size, pandas_time = zip(*pandas_results)
    return (pandas_size, pandas_time)

# if __name__ == "__main__":
#     print(pandas_regex_replace(1))