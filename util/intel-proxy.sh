# setup proxies for various chrome os tools to get out
export http_proxy="http://child-prc.intel.com:913"
export https_proxy="http://child-prc.intel.com:913"
export ftp_proxy=$http_proxy
export RSYNC_PROXY=$http_proxy
export all_proxy="socks://proxy-prc.intel.com:911"
export no_proxy="intel.com, .intel.com, localhost, 127.0.0.0"
 
 
# set for building Chromium for google authentication
export NO_AUTH_BOTO_CONFIG="$HOME/.boto"
