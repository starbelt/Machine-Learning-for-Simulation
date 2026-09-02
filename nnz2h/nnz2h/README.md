# Neural Networks Zero to Hero

Files and directories for Karpathy's Neural Networks playlist.

## Directory Contents

* [00-setup](00-setup/README.md): Setup scripts
* [01-lessons](01-lessons/README.md): Jupyter Lab Notebooks lessons
* [pygrad](pygrad/__init__.py): The `pygrad` package
* [README.md](README.md): This document

## Quickstart

Clone the repository and change directories into the repository.

```bash
cd ~
mkdir -p git-repos
cd ./git-repos/
git clone git@github.com:starbelt/repo-name.git
cd repo-name/
git config --global user.name "First Last"
git config --global user.email "flast@vt.edu"
```

Ensure prerequisites are installed.

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-tk
sudo apt install python3-pip
sudo apt install python3-venv
sudo apt install graphviz
```

Run the setup script.

```bash
cd 00-setup/
./setup_p3_venv.sh
```

Activate the virtual environment.

```bash
cd ../
source p3-env/bin/activate
```

Start Jupyter Lab.

```bash
jupyter lab
```

Open each Notebook (e.g., `lesson-01.ipynb`, `lesson-02.ipynb`). Use the ">>"
button (Restart the kernel and run all cells), or run each cell in sequence.

When finished, close all windows and shutdown the Jupyter Lab.

Deactivate virtual environment.

```bash
cd ../
deactivate
```
