#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("teste7.txt")

#fs = int(len(dados[:])/5)

tempo = np.linspace(0,4,len(dados[:]))

#grafico 2 adc
plt.figure()
plt.plot(tempo,dados[:],c="red", marker = ".")
plt.title("Tensão x Tempo ")
plt.xlabel("tempo [s]")
plt.ylabel("tensão [V]")
plt.grid()
plt.show()
#plt.savefig('teste8_grafico.png')