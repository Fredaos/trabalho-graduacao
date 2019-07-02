#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("aq_adc.txt")

fs = int(len(dados[:])/5)

tempo = np.linspace(0,5,len(dados[:]))

#grafico 2 adc
plt.figure()
plt.scatter(tempo,dados[:],c="red", marker = ".")
plt.title("Tensão x Tempo com ADC simples %.3d %s" %(fs,"sps"))
plt.xlabel("tempo [s]")
plt.ylabel("tensão [V]")
plt.grid()
plt.show()
plt.savefig('adc.png')