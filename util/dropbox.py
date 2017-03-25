#!/usr/bin/env python
import os
import glob
import sys
import subprocess
import PyPDF2
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from douban_client import DoubanClient
from colorconsole import terminal
import dropbox.client
app_key='1qp8zxvkvzgowj0'
app_secret='i5ajtsv0z7laip3'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()
quit()
screen=terminal.get_terminal(conEmu=False)
def get_pdf_line(pdf_file,page):
    for line in pdf_file.getPage(page).extractText().splitlines():
        yield line
search_item=sys.argv[1]
book_list=[]
real_book_list=[]
book_name_with_author_list=[]
for root,dirs,files in os.walk("/home/poter/Dropbox/book"):
    for name in dirs:
        book_path =(os.path.join(root,name))
        book_list+=glob.glob(book_path+'/*.pdf')
        book_list+=glob.glob(book_path+'/*.epub')
        book_list+=glob.glob(book_path+'/*.txt')
        book_list+=glob.glob(book_path+'/*.djvu')
        book_list+=glob.glob(book_path+'/*.chm')

for i in range(0, len(book_list)-1):
    book_name =book_list[i]
    book_full_name=book_name.split('/')
    real_book_list.append(book_full_name[len(book_full_name)-1])
for i in range(0, len(real_book_list)-1):
    book_name_with_author=real_book_list[i].split('.')
    book_name_with_author_list.append( book_name_with_author[len(book_name_with_author)-2])
result_list=[]
result_file_location=[]
for i in range(0, len(book_name_with_author_list)-1):
    if search_item in book_name_with_author_list[i]:
        result_list.append(book_name_with_author_list[i])
        result_file_location.append(book_list[i])
if len(result_list) < 1:
    print "not found"
    quit()
for i in range(0, len(result_list)):
    print '['+str(i)+']:'+result_list[i]

#print "open?"
while 1:
    option=raw_input('open?')
    if option == 'q':
        quit()
        index=int(option)
        print len(result_list)
        if index >= len(result_list):
            print "index out of range"
        else:
            break

search_item=raw_input('search in book?')
if search_item=='q':
    quit()

pdf_file=open(result_file_location[index], 'rb')
read_pdf=PyPDF2.PdfFileReader(pdf_file)
i=-1
for pageNumber in range(0, read_pdf.getNumPages()):
    i=-1
    for line in get_pdf_line(read_pdf,pageNumber):
        i+=1
        if search_item in line:
            output= "Page"+str(pageNumber)+",Line"+str(i)+":"+ line+'\n'
            if i%2 == 0:
                screen.cprint(4,0,output)
            else:
                screen.cprint(10,1,output)
                screen.reset_colors()

