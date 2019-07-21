#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
#import scipy.signal as sc



dados = np.loadtxt("teste.txt")

#b, a = sc.butter(3, 0.9,btype="highpass") #3a ordem, 15 Hz em relacao a freq Nyquist 

#dados = sc.filtfilt(b,a, data[:], axis = 0) #filtro butterworth, axis = 0 tem que dizer o eixo para dizer em que direcao quer se calcular

fs = int(len(dados[:])/5)

tempo = np.linspace(0,5,len(dados[:]))

#grafico 2 adc
plt.figure()
plt.plot(tempo,dados[:],c="red", marker = ".")
plt.title("Tensão x Tempo")
plt.xlabel("tempo [s]")
plt.ylabel("tensão [V]")
plt.grid()
plt.show()
plt.savefig('teste4.png')