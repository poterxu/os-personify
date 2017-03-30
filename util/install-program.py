#!/usr/bin/env python
import sys
import os

if len(sys.argv) <=  1:
    print 'no program'
    quit()
os.system('sudo apt-get install '+sys.argv[1])
quit()

