#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:34:58 2017

@author: andrepignata
"""
import pprint
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from sqlalchemy import create_engine
from time import sleep
from os import getcwd
pp = pprint.PrettyPrinter(indent=4)

path = getcwd()
engine = create_engine('postgresql://rosana_leitura@nv1.fearp.usp.br:1754/rosana_dva')
# Arrumar a profile do Firefox para downlaod
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", path)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip;application/octet-stream;application/x-zip;application/x-zip-compressed")
#
browser = webdriver.Firefox(firefox_profile = profile)
#browser = webdriver.Chrome('./chromedriver')
iIni = '1'
dInst = pd.read_sql_query("""select * from documentos where id_documento not like 'javascri%%' and id_documento::integer >= """+iIni+""" order by id_documento::integer""",engine)
row = dInst.iloc[0]
for index,row in dInst.iterrows():
    print('Pegando documento:'+row['id_documento'])
    browser.get("https://www.rad.cvm.gov.br/enetconsulta/frmGerenciaPaginaFRE.aspx?CodigoTipoInstituicao=1&NumeroSequencialDocumento="+row['id_documento'])
    while (len(browser.find_elements_by_id('cmbGrupo'))==0):
        sleep(1)
    
    aGrupos = ['DFs Individuais','DFs Consolidadas']
    aQuadros = ['Balanço Patrimonial Ativo','Balanço Patrimonial Passivo','Demonstração do Resultado']
    aGrupo = aGrupos[0]
    aQuadro = aQuadros[0] 
    
    for aGrupo in aGrupos:
        if (len(browser.find_elements_by_xpath("//select[@id='cmbGrupo']/option[text()='"+aGrupo+"']")) > 0):
            print('Tenho '+aGrupo)
            Select(browser.find_element_by_id('cmbGrupo')).select_by_visible_text(aGrupo)
            #pegando Balanço patrimonial ativo
            while (len(browser.find_elements_by_id('cmbQuadro'))==0):
                sleep(1)
            
            for aQuadro in aQuadros:
                Select(browser.find_element_by_id('cmbQuadro')).select_by_visible_text(aQuadro)
                sleep(5)
                while (len(browser.find_elements_by_id('iFrameFormulariosFilho'))==0):
                    sleep(1)
                browser.switch_to_frame('iFrameFormulariosFilho')
                
                while (len(browser.find_elements_by_id('ctl00_cphPopUp_tbDados'))==0):
                    sleep(1)
                sTabela = browser.find_element_by_id('ctl00_cphPopUp_tbDados').get_attribute('innerHTML')
                if ((u'Justificativa para a não' in sTabela) == False):
                    df = pd.read_html("<table>"+sTabela+"</table>",header=0)[0]
                    
                    dfL = df.melt(id_vars=['Conta', u'Descrição'])
                    dfL['id_documento'] = row['id_documento']
                    dfL['grupo'] = aGrupo
                    dfL['quadro'] = aQuadro
                    #dfL.to_sql('balanco',engine, if_exists='append',index=False)    
                    browser.switch_to_default_content();
                sleep(1)
