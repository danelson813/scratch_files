"""

start with:
pip install jupyterlab

uv init <new_name>

This creates a new folder with the name and populates it with essential files.

To install new libraries, move to that folder and use uv add <package name>for whatever packages you need. Do NOT add Jupyter, but DO add ipykernel.

On terminal:
uv run python -m ipykernel install --user --name myproject --display-name "Python (MyProject)"


Use your project name as the name (the display name is optional and probably unnecessary).

You can find the registered kernels with the following command:

jupyter kernelspec list

OR use this  bash script, call it juv.bat

uv init %1
cd %1
uv add ipykernel
uv run python -m ipykernel install --user --name %1 --display-name "%1"

for instance:    ./jub.bat mynewproject

In your new directory, you can uv add the packages that you need, and when you run Jupyter, the new kernel, with the same name as your project, will be waiting there for you.

"""
