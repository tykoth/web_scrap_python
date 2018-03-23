#!/usr/bin/env python2
# engine='python'.
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:43:06 2016

@author: andrepignata
"""
import urllib.request
from os import getcwd

import pandas as pd
import numpy as np

cwd = getcwd()
print(cwd)

aCidades = pd.read_csv('bases/cidades.csv')
#aTemas = [{'ano':2010,'tema':1}]
aTemas = [{'ano':2015,'tema':118}]
rCidade = aCidades.ix[0]
iTema = aTemas[0]
for rCidade in aCidades:    
    for iTema in aTemas:
        sArquivo = './csv/'+str(rCidade[0])+'_'+str(iTema['tema'])+'.csv'
        print(sArquivo)
        urllib.request.urlretrieve('http://cidades.ibge.gov.br/xtras/csv.php?lang=&idtema='+str(iTema['tema'])+'&codmun='+str(rCidade[0]),sArquivo)
        with open(sArquivo, 'r',encoding='iso-8859-1') as f:
            content = f.readlines()
        iEspaco = 0;
        aDado = list()
        for sLinha in content:
            if (sLinha.strip() == ''):
                iEspaco += 1
            if iEspaco == 1:
                sLinha = sLinha.replace(';-;',';Null;')
                sLinha = sLinha.replace('N&atilde;o informado','Null')
                sLinha = sLinha.replace('.','')
                sLinha = sLinha.replace(',','.')
                aDado.append(sLinha.split(';'))
        aDado.pop(0)
        aDado.pop(0)
        
        data = pd.DataFrame(aDado)
        

        data['ano'] = iTema['ano']
        data['codmun'] = rCidade[0]
        data.columns = ['descricao','valor','unidade','ano','codmun']
        data.replace('Null',np.nan,inplace=True)
        print(data)
        #data.to_sql('idh',engine,if_exists='append')

