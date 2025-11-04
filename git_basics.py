"""
.

📌 Working with remote repositories
Let’s begin by looking at 6 common tasks that frequently arise when working with remote repositories:

📍 Create a copy of remote branch, make changes and push it
When working on a code change, one useful workflow is to:

Create a local branch from an existing remote branch
Make changes in the branch locally
Push local changes to the upstream branch
Here’s how to accomplish this task:

# Step 0: Clone the repo
git clone <repo-url>
# Step 1: Create a local copy of the existing remote branch
git fetch origin # Ensure latest changes are fetched
git switch --track origin/<branch-name>
# Step 2: Make code changes, stage and commit
git add <file-path(s)>
git commit -m "<commit-message>"
# Step 3: Push the local changes to the upstream branch
git push
git switch --track origin/<branch-name> is an efficient way of git switch -c <branch-name> origin/<branch-name>, it is especially useful if your branch name is quite long.

📍 Create new local branch and push the new branch to remote
When working on a code change, another more common workflow is to:

Create a new local branch, often called a feature branch, from the base branch (e.g. main, develop)
Make code changes in the feature branch locally.
Push the feature branch to a remote repository.
# Assuming you have local clone of remote repository
# Step 1: Create new local branch based of base branch and switch to it
git switch <base-branch>
git pull # Ensure base branch is at the latest version
git switch -c <feature-branch>
# Step 2: Make code changes, stage and commit
git add <file-path(s)>
git commit -m "<commit-message>"
# Step 3: Push the local branch to a new remote branch with the same name
git push -u origin HEAD
In the last command, -u is short for -set--upstream. After pushing it the first time to remote branch, you can simply use git push for subsequent pushes as the upstream branch is already setup.

📍 Edit last commit in both local and remote repository
Mistakes happen, such as a typo in a commit message or forgetting to include a file. There will be an occasional need to edit our last commit. In these cases, we can use the following workflow to update that last commit that was already pushed upstream:

# Step 1: Check recent commit history
git show HEAD
# Step 2: Update commit locally
git add <file-path(s)>
git commit --amend -m "<New-commit-message>"
# Step 3: Check recent commit history to verify the correct edit
git show HEAD
# Step 4: Push the edit upstream
git push -f # Then, verify it in the web interface of the hosting service
If you don’t need to change your commit message, then simply use this git commit --amend --no-edit when committing. In the last line, -f is short for --force, we need this to update upstream branch to align with the new changes so that our local branch and remote branch won’t diverge and create conflicts later on.

📍 Delete last commit in both local and remote repository
In some circumstances, we will need to delete commits:

# Step 1: Check recent commit history to check
git log --oneline -5
# Step 2: Delete commit locally and push the change to remote
git reset --soft HEAD~1 # Delete commit locally
git push -f # Delete commit upstream
# Step 3: Check recent commit history to check
git log --oneline -5
Using --soft will keep the changes from the commit in our working directory as staged files. If we want to discard the changes completely, then use --hard instead.

📍 Delete local and remote branch
Once branch changes are merged and we no longer need the branch, it’s a good practice to clean up redundant branches to keep our repository tidy:

# Step 1: Check all local and remote branches
git branch -a
# Step 2: Delete branch in both local and remote repo
git branch -d <branch-name>
git push origin -d <branch-name>
# Step 3: Check all local and remote branches
git branch -a


"""
