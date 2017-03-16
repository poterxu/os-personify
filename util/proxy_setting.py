#!/usr/bin/env python
#read config
import os
fh=open("../config/intel_914_proxy.op")
line=fh.readline()
print line
sys_cmd='export http_proxy='+line
os.system(sys_cmd)
os.environ['http_proxy'] = line
