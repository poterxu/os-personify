#!/usr/bin/env python

import sys
import os
#setup_des = '/home/personify'
home_dir = os.getenv("HOME")
setup_des = home_dir + '/personify'

print home_dir
print setup_des
print os.path.isdir(setup_des)
if True == os.path.isdir(setup_des):
    print 'already exits'
else:
    os.system('mkdir '+ setup_des)
#System Proxy setup
os.system('cp ./switch-proxy.py ' +setup_des+'/')
bashrc_backup = 'cp '+ home_dir+'/.bashrc'
#VIM setup & Config

