#!/usr/bin/env python
#read config
import os
import sys
proxy_source=sys.argv[1]
if proxy_source == "Intel":
    fh=open("../config/intel_914_proxy.op")
elif proxy_source == "Duotai":
    fh=open("../config/duotai_proxy.op")
else:
    quit()
line=fh.readline()
print line
sys_cmd='export http_proxy='+line
os.system(sys_cmd)
os.environ['http_proxy'] = line
