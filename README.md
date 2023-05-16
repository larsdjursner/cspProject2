# cspProject2
MiniProject 2 for Computer Systems Performance 2023

## Setup
The setup step will take a long while due to the size of rapidsai.
```bash
conda create --name cuenv -c rapidsai -c conda-forge -c nvidia cudf python=3.8 cudatoolkit=11.4

conda activate cuenv

conda install matplotlib

```


## Running the program locally
```bash
python src/main.py
```

## running on HPC
```bash
cd /jobs

sbatch cspv2.job

squeue -u $USER
```

## 
