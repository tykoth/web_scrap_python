# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 06:19:55 2016

@author: André Pignata
"""

import pandas as pd
from sqlalchemy import create_engine
import itertools
import numpy
from bs4 import BeautifulSoup
import requests

##### Driver

# Criar o diretório para download

engine = create_engine('postgresql://XXXXXX@nv1.fearp.usp.br:1754/rosana_dva')

aLetras = [chr(x) for x in numpy.array(range(ord('A'),ord('Z')+1))]
aNumeros = numpy.array(range(0,10))
for sLetra in itertools.chain(aLetras,aNumeros) :
    print(sLetra)
    url = 'https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial='+str(sLetra)
    soup = BeautifulSoup(requests.get(url,verify=False).text,'lxml')
    sTabela = soup.find('table',{'id':'dlCiasCdCVM'})
    if (sTabela is not None):
        sTabela = sTabela.prettify()
        df = pd.read_html(sTabela,header=0)[0]
        df.columns = ['cnpj','nome','tipo','codigo','situacao']
        df.to_sql('instituicao_cvm',engine, if_exists='append',index=False)   

