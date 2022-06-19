# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 02:51:00 2022

@author: DELL
"""
#Scraping html data using beautiful soup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
summ=0
url=('http://py4e-data.dr-chuck.net/comments_1516334.htmlURL:')
#html=urlopen(url).read
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags=soup('span')
#Print the numbers and display sum of the numbers
for tag in tags:
    no=tag.contents[0]
    no_int=int(no)
    summ=summ+no_int
    print(tag.contents[0])
   # print(tag.contents[0])
print('Sum = ',summ)
