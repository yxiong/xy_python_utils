================================================================
Workflow.
================================================================

# Keep the `master` branch clean and sync-ed with `origin/master`.

$ git remote -v
origin       git@github.com:yxiong/xy_python_utils.git (fetch)
origin       git@github.com:yxiong/xy_python_utils.git (push)
$ git checkout master
$ git pull origin master
From github.com:yxiong/xy_python_utils
 * branch            master     -> FETCH_HEAD
 Already up-to-date.


# Create a separate `dev` or `feature` branch for everyday development. It is
# okay to make multiple commits (including "oops-commits") in this branch, as we
# will clean it up in the `master` branch.

$ git checkout [-b] dev
# Make some edits.
$ git commit -am "commit message"
# Make more edits.
$ git commit -am "commit message"
$ git push origin dev


# Once we are happy with the `dev` branch, use `git checkout .` in `master`
# branch to create a single commit (and therefore a clean git history).

$ git checkout master
$ git checkout dev .
$ git diff dev           # Should show nothing.
$ git status             # Double check this is the changes we want to make.
$ git commit -am "commit message"
$ git push origin master


# Delete the `dev` branch once merged to master, and start with a new one if
# necessary.

$ git checkout master
$ git branch -D dev
$ git push origin :dev
$ git checkout -b dev


================================================================
Naming Conventions.
================================================================
We try to follow the Google Python Style Guild, which has the following naming
convention:

module_name, package_name, ClassName, method_name, ExceptionName, function_name,
GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name,
function_parameter_name, local_var_name.

Some of the old code (prior to Oct 28, 2014) does not follow this convention,
and is likely to be updated in the future.


================================================================
TODO.
================================================================

Add a README entry for using pychecker.


================================================================
NOTES.
================================================================

Some historic code of this project can be found at the private repo
https://bitbucket.org/ylxiong/xy_python_utils.
