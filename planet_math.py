#! /usr/bin/python3
# Copyright (c) 2020, Keita Kitaura
# All rights reserved.
#
# $Id: $
#
# ref: Planet Math
# https://planetmath.org/

import sys
import re
import requests
import bs4

def get_page(word):
    get_web_page = requests.get(f'http://planetmath.org/{word}')
    bsobj = bs4.BeautifulSoup(get_web_page.text, 'lxml')
    text = bsobj.get_text()
    t_list = text.split('\n')
    # print(t_list)
    for t in t_list[15:]:
        if t == 'Title':
            break
        if not len(t) == 0:
            print(t)
    # text = re.sub("^$","",text)
    # print(text)

def main():
    word =  sys.argv[1]

    f = open("/home/keita/bof/unix/dict/planetmath/word_list")
    w_list = f.read()
    
    list_regex = re.compile(f'/{word}"', re.I)
    title = list_regex.findall(w_list)
    
    if len(title) == 0:
        print(f"'{word}' does not exist in Planet Math. ")
        return 0
    
    get_page(word)
    
if __name__ == "__main__":
    main()



