#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("aq_adc.txt")

fs = int(len(dados[:])/5)
tempo = np.linspace(0,5,len(dados[:]))

#grafico 2 adc
plt.figure()
plt.hist(dados[tempo<=1], bins=10 )
plt.title("Histograma: #Amostras x Tensão %.3d %s" %(fs,"sps"))
plt.xlabel("tensao [V]")
plt.ylabel("frequencia #amostras")
plt.grid()
plt.show()
plt.savefig('hist_adc.png')
print(np.mean(dados[tempo<=1]))
print(np.std(dados[tempo<=1]))