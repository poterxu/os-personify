#!/usr/bin/env python
import os
import sys
print sys.argv[1:]
commit_arg=''
for i in range(1, len(sys.argv)):
    commit_arg+=' '
    commit_arg+=sys.argv[i]



git_commit_cmd='git commit'+commit_arg
os.system(git_commit_cmd)
