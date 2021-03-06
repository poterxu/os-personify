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
from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format

screen=terminal.get_terminal(conEmu=False)
def ascii_art_print(string):
    cprint(figlet_format(string,font="starwars"),'yellow',
            'on_red',attrs=['bold'])

def get_pdf_line(pdf_file,page):
    for line in pdf_file.getPage(page).extractText().splitlines():
        yield line

def pdf_book_search(path):
    pdf_file=open(path, 'rb')
    read_pdf=PyPDF2.PdfFileReader(pdf_file)
    for pageNumber in range(0, read_pdf.getNumPages()):
        i=-1
        for line in get_pdf_line(read_pdf,pageNumber):
            i+=1
            if search_item in line:
                output= "Page"+str(pageNumber)+",Line"+str(i)+":"+ line+'\n'
                #ascii_art_print('continue')
                if i%2 == 0:
                    screen.cprint(4,0,output)
                else:
                    screen.cprint(10,1,output)
                    screen.reset_colors()
def chm_book_search(path):
    print "To do"

def txt_book_search(path):
    print "To do"
ascii_art_print('book search')
if len(sys.argv) <= 1:
    print "No searh item"
    quit()
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

number_ascii=['0','1','2','3','4','5','6','7','8','9']
while 1:
    option=raw_input('open?')
    if option == 'q':
        quit()
    if option[0] not in number_ascii:
        print "Invalid index"
        continue
    index=int(option)
    print len(result_list)
    if index >= len(result_list):
        print "index out of range"
    else:
        break
file_full_path=result_file_location[index]
full_path_splited=file_full_path.split('.')
book_type=full_path_splited[len(full_path_splited)-1]

search_item=raw_input('search in book?')

if search_item=='q':
    quit()
ascii_art_print(book_type)
if book_type=='pdf':
    print "book type pdf"
    pdf_book_search(result_file_location[index])
elif book_type=='chm':
    chm_book_search(result_file_location[index])
elif book_type=='txt':
    txt_book_search(result_file_location[index])
else:
    print "unknown book type"

