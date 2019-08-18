#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("teste8_fora.txt")

fs = int(len(dados[:])/1)
tempo = np.linspace(0,1,len(dados[:]))

#grafico 2 adc
plt.figure()
plt.hist(dados[tempo<=1], bins=10 )
plt.title("Histograma: #Amostras x Tensão")
plt.xlabel("tensao [V]")
plt.ylabel("frequencia #amostras")
plt.grid()
plt.show()
#plt.savefig('hist_550kfora.png')
print(np.mean(dados[tempo<=1]))
print(np.std(dados[tempo<=1]))
