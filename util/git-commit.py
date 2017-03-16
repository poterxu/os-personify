#!/usr/bin/env python
import os
import sys

commit_arg=sys.argv[1]
git_commit_cmd='git commit '+commit_arg
os.system(git_commit_cmd)
