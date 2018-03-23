#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 17:54:20 2018

@author: andrepignata
"""

import requests
from os import getcwd

import pandas as pd

cwd = getcwd()
print(cwd)

aCidades = pd.read_csv('bases/cidades.csv')

aCidade =aCidades.iloc[0]

for aCidade in aCidades:
    sUrl = "https://maps.google.com/maps/api/geocode/json?"
    aParams = {'sensor':'false'
              ,'address':aCidade['nome']
              ,'key':''}
    
    sEnd  = requests.get(sUrl,params=aParams)
    
    aRes = sEnd.json()['results']
    
    aLoc = aRes[0]['geometry']['location']
    print(aLoc['lng'],aLoc['lat'])