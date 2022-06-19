# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 04:52:32 2022

@author: DELL
"""



from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count= int(input('count : '))
pos= int(input('Pos : '))
link = ('http://py4e-data.dr-chuck.net/known_by_Astra.htmll')


for tag in range(count):
    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup('a')
    link=tags[pos-1].get('href',None)
    print(link)