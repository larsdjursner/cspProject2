#!/bin/bash

module load Anaconda3
module load CUDA
. $(conda info --base)/etc/profile.d/conda.sh
conda create --name csp_numpy_cupy python=3.8
source activate csp_numpy_cupy
conda install -c conda-forge -c rapidsai cudf cupy cudatoolkit=10 numpy matplotlib pandas 
conda deactivate
conda init --all
source /home/$USER/.bashrc

