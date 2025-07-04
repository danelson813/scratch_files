'''
What You’ll Need
Before we get started, make sure you have:

Python (3.8 or higher recommended)
pip or conda — I prefer pip, but conda is fine too
A terminal or command prompt — I am using Git Bash

Create a virtual environment
# Go to one of your drive in your PC/laptop
mkdir <your-project-name> # Name your project anything
cd <your-project-name> # Go into the project directory
python -m venv .venv # Name your virtual environment anything "python -m venv <your-env-name>
# In the below code replace the ".venv" with your virtual environment name
source .venv/Scripts/activate # for cmd - ".venv/Scripts/activate" for linux "source .venv/bin/activate"


The virtual environment is created and activated. Now all we need to do is install “Jupyter-lab” or “Jupyter-notebook” into this virtual environment and load our virtual environment into the Jupyter kernels.

pip install notebook # For install jupyter-notebook
pip install jupyterlab # For install jupyter-lab


All that is left is to install ipykernel (Interactive Python kernel) and link your virtual environment to the kernel.

pip install ipykernel # For pip
conda install anaconda::ipykernel # For Conda

# Link your environment to the ipykernel (Replace .venv with your virtual env name)
# You can choose your display name as something which helps you quickly identify
# Prefered name - "Python<version-number> (<your-project-name>)
python -m ipykernel install --user --name=.venv --display-name "Python (myproject)"

# Run Jupyter-lab
jupyter lab
# Run Jupyter-notebook
jupyter notebook


'''