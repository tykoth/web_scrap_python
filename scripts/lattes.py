#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 18:48:49 2018

@author: andrepignata
"""

import requests
from bs4 import BeautifulSoup as bs
import re

sUrl = "http://buscatextual.cnpq.br/buscatextual/busca.do"
aParams = { 'metodo':'buscar',
            'acao':'',
            'resumoFormacao':'',
            'resumoAtividade':'',
            'resumoAtuacao':'',
            'resumoProducao':'',
            'resumoPesquisador':'',
            'resumoIdioma':'',
            'resumoPresencaDGP':'',
            'resumoModalidade':'',
            'modoIndAdhoc':'',
            'buscaAvancada':'0',
            'filtros.buscaNome':'true',
            'textoBusca':'andre+luiz+martins+pignata',
            'buscarDemais':'true',
            'buscarBrasileiros':'true',
            'buscarEstrangeiros':'true',
            'paisNascimento':'0',
            'textoBuscaTodas':'',
            'textoBuscaFrase':'',
            'textoBuscaQualquer':'',
            'textoBuscaNenhuma':'',
            'textoExpressao':'',
            'buscarDoutoresAvancada':'true',
            'buscarBrasileirosAvancada':'true',
            'buscarEstrangeirosAvancada':'true',
            'paisNascimentoAvancada':'0',
            'filtros.atualizacaoCurriculo':'48',
            'quantidadeRegistros':'10',
            'filtros.visualizaEnderecoCV':'true',
            'filtros.visualizaFormacaoAcadTitCV':'true',
            'filtros.visualizaAtuacaoProfCV':'true',
            'filtros.visualizaAreasAtuacaoCV':'true',
            'filtros.visualizaIdiomasCV':'true',
            'filtros.visualizaPremiosTitulosCV':'true',
            'filtros.visualizaSoftwaresCV':'true',
            'filtros.visualizaProdutosCV':'true',
            'filtros.visualizaProcessosCV':'true',
            'filtros.visualizaTrabalhosTecnicosCV':'true',
            'filtros.visualizaOutrasProdTecCV':'true',
            'filtros.visualizaArtigosCV':'true',
            'filtros.visualizaLivrosCapitulosCV':'true',
            'filtros.visualizaTrabEventosCV':'true',
            'filtros.visualizaTxtJornalRevistaCV':'true',
            'filtros.visualizaOutrasProdBibCV':'true',
            'filtros.visualizaProdArtCultCV':'true',
            'filtros.visualizaOrientacoesConcluidasCV':'true',
            'filtros.visualizaOrientacoesAndamentoCV':'true',
            'filtros.visualizaDemaisTrabalhosCV':'true',
            'filtros.visualizaDadosComplementaresCV':'true',
            'filtros.visualizaOutrasInfRelevantesCV':'true',
            'filtros.radioPeriodoProducao':'1',
            'filtros.visualizaPeriodoProducaoCV':'',
            'filtros.categoriaNivelBolsa':'',
            'filtros.modalidadeBolsa':'0',
            'filtros.nivelFormacao':'0',
            'filtros.paisFormacao':'0',
            'filtros.regiaoFormacao':'0',
            'filtros.ufFormacao':'0',
            'filtros.nomeInstFormacao':'',
            'filtros.conceitoCurso':'',
            'filtros.buscaAtuacao':'false',
            'filtros.codigoGrandeAreaAtuacao':'0',
            'filtros.codigoAreaAtuacao':'0',
            'filtros.codigoSubareaAtuacao':'0',
            'filtros.codigoEspecialidadeAtuacao':'0',
            'filtros.orientadorCNPq':'',
            'filtros.idioma':'0',
            'filtros.grandeAreaProducao':'0',
            'filtros.areaProducao':'0',
            'filtros.setorProducao':'0',
            'filtros.naturezaAtividade':'0',
            'filtros.paisAtividade':'0',
            'filtros.regiaoAtividade':'0',
            'filtros.ufAtividade':'0',
            'filtros.nomeInstAtividade':''
            }

r = requests.get(sUrl,params=aParams)
r.encoding = 'UTF-8'
s = bs(r.content,"html5lib")
file = open('testfile.txt','w') 
file.write(str(s) )

aLinks = s.findAll('a')
aIds = []
for aLink in aLinks:
    #print(aLink['href'])
    if aLink['href'].find('abreDetalhe') > 0:
        m = re.search(".*abreDetalhe\('(.*?)',.*",aLink['href']) 
        print(m.group(1))
        aIds.append(m.group(1))

print(aIds)        
print(len(aIds))        
#OK! AGORA, QUERO OBTER O LATTES DE TODOS OS PESQUISADORES!        

r = requests.get("http://buscatextual.cnpq.br/buscatextual/busca.do?metodo=forwardPaginaResultados&registros=0;1000&query=%28+%2Bidx_nacionalidade%3Ae%29+or+%28+%2Bidx_nacionalidade%3Ab%29&analise=cv&tipoOrdenacao=null&paginaOrigem=index.do&mostrarScore=false&mostrarBandeira=true&modoIndAdhoc=null")
r.encoding = 'UTF-8'
s = bs(r.content,"html5lib")

