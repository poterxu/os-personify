#!/usr/bin/env python
#read config
import os
import glob
import sys
from douban_client import DoubanClient
#sys_cmd="ls -pR ~/Dropbox/book | grep -v / "
#file_list = os.popen(sys_cmd).read()
#print "start list..."
#print file_list
#print "end list"
#print len(file_list)
#for i in range(0, len(file_list) -1):
 #   print "book:"+ file_list[i]
#dir_list=os.listdir("/home/poter/Dropbox/book/")
#for i in range(0, len(dir_list) -1):
#   print "book:"+ dir_list[i]
#
#book_list= glob.glob("/home/poter/Dropbox/book/*.pdf")
#book_list+= glob.glob("/home/poter/Dropbox/book/*.epub")
#book_list+= glob.glob("/home/poter/Dropbox/book/*.txt")
#book_list+= glob.glob("/home/poter/Dropbox/book/*.djvu")

#for i in range(0, len(book_list)-1):
 #   print book_list[i]
search_item=sys.argv[1]
book_list=[]
real_book_list=[]
book_name_with_author_list=[]
for root,dirs,files in os.walk("/home/poter/Dropbox"):
    for name in dirs:
        book_path =(os.path.join(root,name))
        book_list+=glob.glob(book_path+'/*.png')
        book_list+=glob.glob(book_path+'/*.jpg')
        book_list+=glob.glob(book_path+'/*.pnm')
        book_list+=glob.glob(book_path+'/*.gif')
        book_list+=glob.glob(book_path+'/*.svg')

for i in range(0, len(book_list)-1):
    book_name =book_list[i]
    book_full_name=book_name.split('/')
    real_book_list.append(book_full_name[len(book_full_name)-1])
for i in range(0, len(real_book_list)-1):
    book_name_with_author=real_book_list[i].split('.')
    book_name_with_author_list.append( book_name_with_author[len(book_name_with_author)-2])
#book_name_with_author_list.sort()
for i in range(0, len(book_name_with_author_list)-1):
   # if search_item in book_name_with_author_list[i]:
        print book_name_with_author_list[i]
        print book_list[i]
    
#print 'Go to the following link in your browser:' 
#print client.authorize_url
