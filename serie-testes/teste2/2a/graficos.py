#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#dados = np.loadtxt("aquisicao1.txt")
#fs = len(dados[:,1])/10
#
##grafico 1 adc
#plt.figure()
#plt.scatter(dados[:,0],dados[:,1],c="red", marker = ".")
#plt.title("tensão x tempo [813 ksps]")
#plt.xlabel("tempo [s]")
#plt.ylabel("tensão [V]")
#plt.show()
#plt.savefig('aq1.png')

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