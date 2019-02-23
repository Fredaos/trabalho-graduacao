#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:23:33 2019

@author: fred
"""
import numpy as np
dados = []
    # Salva valores do osciloscopio para um arquivo.txt
for x in [1,2,3,4,5]: # recupera num samples de dados do driver de memoria DDR
    tensao = ('%0.6f' %((x*1.8)/4096))
    tensao = float(tensao) 
    dados.append(tensao) # adiciona valores de tensao em dados
    
dados = np.asarray(dados) #converte data para array