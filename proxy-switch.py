#!/usr/bin/env python
import sys
import os
#print sys.argv[0]
enable_str = 'enable'
disable_str = 'disable'
auto_mode_cmd ='gsettings set org.gnome.system.proxy mode \'auto\''
none_mode_cmd ='gsettings set org.gnome.system.proxy mode \'none\''

pac_url_cmd = 'gsettings set org.gnome.system.proxy autoconfig-url http://xduotai.com/xTUKZ9fObNA.pac'


if sys.argv[1] == enable_str:
    os.system(auto_mode_cmd)
    os.system(pac_url_cmd)
    print 'duotai enabled'
elif sys.argv[1] == disable_str:
    os.system(none_mode_cmd)
    print 'duotai disabled'
else:
    print 'Wrong option, do nothing'

#os.system('gsettings set org.gnome.system.proxy mode 'auto'')
#os.system('gsettings set org.gnome.system.proxy autoconfig-url http://xduotai.com/xTUKZ9fObNA.pac')
