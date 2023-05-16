#!/bin/bash

module load Anaconda3
module load CUDA
. $(conda info --base)/etc/profile.d/conda.sh

conda create --name cuenv -c rapidsai -c conda-forge -c nvidia cudf python=3.8 cudatoolkit=11.4
source activate cuenv
conda install matplotlib
conda deactivate

conda init --all
source /home/$USER/.bashrc
