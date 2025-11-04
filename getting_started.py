# this uses uv to do a lot
# This is based on a Medium article
# Fully Explained Git + Python Workflow with uv, ruff, and ty
# by Gwang-Jin
"""
start with smart defaults
git config --global color.ui auto
git config --global fetch.prune true
and a couple of alias'
git config --global alias.st status
git config --global alias.co checkout
"""

"""
setup:  uv venv
        uv pip install ruff ty
        touch main.py
    then:
        git checkout -b  feature/<name of feature>
when the feature is ready:
    fit fetch origin
    git rebase origin/main
    this pulls new commits from main and replayus your changes on top
"""
"""
add this to your project's .gitignore:
    __pychache__/
    *.pyc
    .venv/
    .env
    .cache/    
"""
"""
nano .precommit-config.yaml
repos:
  -repo: local
   hooks:
     - id: ruff
       name: Run ruff vial uv
       entry: uv run ruff check --fix
       language: system
       types: [python]
       
     - id: ruff-format
       name: Format with ruff vial uv
       entry: uv run ruff format
       language: system
       types: [python]
       
     - id: ty
       name: Run ty type checker
       entry: uv run ty check
       language: system
       types: [python]   
then run:
    uv run pre-commit install   
"""

"""
to set up the project structure:
    # create a project folder
    mkdir <project name>
    cd <project name>
    #create a fast virtual environment
    uv venv
    # install ruff , ty, and pre-commit
    uv pip install ruff, ty, and pre-commit
"""
"""
# create .gitignore
add:
    echo "__pycache__/
    .venv/
    *.pyc
    .env
    " > .gitignore
"""

"""
# add .pre-commit-config.yaml

# nano .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: ruff
        name: Run ruff via uv
        entry: uv run ruff check --fix
        language: system
        types: [python]

      - id: ruff-format
        name: Format with ruff via uv
        entry: uv run ruff format
        language: system
        types: [python]

      - id: ty
        name: Run ty type checker
        entry: uv run ty check
        language: system
        types: [python]
        
        
then run:
    uv run pre-commit install
"""
