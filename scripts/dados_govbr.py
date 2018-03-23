#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 17:47:31 2018

@author: andrepignata
Saúde da Família - Número de equipes
"""



import urllib.request

import pandas as pd
import numpy as np

urllib.request.urlretrieve('http://i3geo.saude.gov.br/i3geo/ogc.php?service=WFS&version=1.0.0&request=GetFeature&typeName=psf_equipes&outputFormat=CSV','bases/saude_familia.csv')

dSaude = pd.read_csv('bases/saude_familia.csv')