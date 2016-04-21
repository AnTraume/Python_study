#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#The program just for extract one statement for www.wufazhuce.com.
import mechanize
import bs4
import sys
number = 50;
def viewPage(url) :
        try:
            browser = mechanize.Browser()
            page = browser.open(url)
            source_code = page.read()
            soup = bs4.BeautifulSoup(source_code,"html.parser")
            for meta in soup.select('meta') :
                if meta.get('name') == 'description':
                    print meta.get('content')
                    print "\n"
        except:
            print number
            print "\n"
while number < 58:
    viewPage('http://wufazhuce.com/one/' + str(number) )
    number = number + 1;
