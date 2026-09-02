#!/bin/bash
#
# setup_p3_venv.sh
# A bash script to set up Python 3 virtual environment
# To check available package versions: python3 -m pip index versions [name]
#
# Usage: ./setup_p3_venv.sh
#  - Must execute from the setup directory
# Prerequisites:
#  - sudo apt install python3-tk
#  - sudo apt install python3-pip
#  - sudo apt install python3-venv
#  - sudo apt install graphviz
# Arguments:
#  - None
# Outputs:
#  - Python 3 virtual environment

cd ../
python3 -m venv p3-env
source p3-env/bin/activate
python3 -m pip install numpy==2.4.1
python3 -m pip install matplotlib==3.10.8
python3 -m pip install scikit-learn==1.8.0
python3 -m pip install jupyterlab==4.5.3
# once installed, type `jupyter lab` to start a server
python3 -m pip install graphviz==0.21
# See https://pytorch.org/get-started/locally/#start-locally for updates
python3 -m pip install torch==2.10.0 torchvision==0.25.0 \
 --index-url https://download.pytorch.org/whl/cpu
# install pygrad
python -m pip install --editable .
deactivate
