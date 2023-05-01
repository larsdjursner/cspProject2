#!/bin/bash

module load Anaconda3
module load CUDA
. $(conda info --base)/etc/profile.d/conda.sh

conda create --name csp_numpy_cupy python=3.8
source activate csp_numpy_cupy
# conda install -c conda-forge -c rapidsai cudf cupy cudatoolkit=10 numpy matplotlib pandas 
conda install -c conda-forge cupy cudatoolkit=10 matplotlib numpy pandas
conda deactivate


# conda create --name csp_numpy_cupy 
# source activate csp_numpy_cupy
# conda create -n rapid -c rapidsai -c conda-forge -c nvidia rapids=23.04 python=3.10 cudatoolkit=11.2
# conda activate rapid
# conda install -c conda-forge -c rapidsai cudf cupy cudatoolkit=10 numpy matplotlib pandas 
# conda install -c rapidsai -c conda-forge cudf cupy cudatoolkit=11.2 numpy matplotlib pandas 
# conda deactivate

conda init --all
source /home/$USER/.bashrc

# conda install -c rapidsai cudf -c conda-forge cupy cudatoolkit=10 numpy matplotlib pandas 
