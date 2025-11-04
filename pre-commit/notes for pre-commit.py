"""
first: pip install pre-commit

include the yaml file

install the git hooks.
Code

    pre-commit install
This command sets up the Git hooks in your local repository, so pre-commit will run automatically before each commit.
How it works:
When you attempt to commit changes after setting up the hooks, pre-commit will execute the configured Ruff hooks.
If ruff (the linter) finds any issues and --fix is enabled, it will attempt to automatically fix them.
If ruff-format (the formatter) finds any formatting inconsistencies, it will automatically reformat the code.
If any issues remain after automatic fixes, or if --fix is not enabled and issues are found, the commit will be blocked, and you will need to address the issues before committing again. You can then git add the fixed files and try committing again.
"""
