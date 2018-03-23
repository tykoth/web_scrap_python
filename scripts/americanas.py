#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 18:28:16 2018

@author: andrepignata
"""
import requests
from bs4 import BeautifulSoup as bs



r = requests.get("https://www.americanas.com.br/categoria/beleza-e-perfumaria")
r.encoding = 'UTF-8'
s = bs(r.content,"html5lib")
file = open('testfile.txt','w') 
file.write(str(s) )

#Encontrando as categorias
aCategorias = s.find('div',{'id':'collapse-categoria'}).findAll('li', {'class' : 'filter-list-item'})
sCategoria = aCategorias[0]
for sCategoria in aCategorias:
    sDescricao = sCategoria.find('a').text
    sLink = sCategoria.find('a')['href']
    #cur.execute("insert into categorias (site,categoria,link) values ('americanas.com.br','"+sDescricao+"','"+sLink+"')")
    #conn.commit()
    


    