#!/usr/bin/env python
import sys
import os
enable_str = 'enable'
disable_str = 'disable'
auto_mode_cmd ='gsettings set org.gnome.system.proxy mode \'auto\''
none_mode_cmd ='gsettings set org.gnome.system.proxy mode \'none\''
duotai_pac_url= 'http://xduotai.com/xTUKZ9fObNA.pac'
lantern_pac_url=''
pac_url_cmd = 'gsettings set org.gnome.system.proxy autoconfig-url http://xduotai.com/xTUKZ9fObNA.pac'

if len(sys.argv) <=  1:
    print 'no option'
    quit()

if sys.argv[1] == enable_str:
    os.system(auto_mode_cmd)
    os.system(pac_url_cmd)
    print 'duotai enabled'
elif sys.argv[1] == disable_str:
    os.system(none_mode_cmd)
    print 'duotai disabled'
else:
    print 'Wrong option, do nothing'

