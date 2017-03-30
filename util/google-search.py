#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.
Command-line application that does a search.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import pprint
import httplib2
import webbrowser
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
#def http_test(url):
#    connect=httplib2.Http(".cache")
#    #connect.force_exception_to_status_code = True
#    #connect.disable_ssl_certificate_validation = self.insecure
#    #headers['User-Agent'] = 'searchlight-client'
#    resp, content = connect.request(url, "GET")

def main():
    print "start main"
    p = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP, 'http://duotai:xTUKZ9fObNA@rosewood.h.xduotai.com', 21693)
    connect = httplib2.Http()
    content = connect.request("https://www.google.com")[1]
    html = content.decode('utf-8')
    #quit()
    f = open('content.html', 'w')
    f.write(content)
    f.close()
    webbrowser.open_new_tab('content.html')
    quit()
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build("customsearch", "v1",
            developerKey="AIzaSyB9kpXmj5eUdZJkjgYZNO8EOe6WtL9peQk")
    print "service built"
    res = service.cse().list(
            q='lectures',
            cx='017576662512468239146:omuauf_lfve',
            ).execute()
    pprint.pprint(res)
    print "executed"
if __name__ == '__main__':
    main()
