#!/usr/bin/python2.7 

import numpy as np
import math

dados = range(0,10) #dados que viriam da aquisicao de dados analogicos
dados = np.asarray(dados) #transformando a lista em matriz
dados = dados[:, np.newaxis] #criando uma dimensao para as colunas do array
n_amostras = 5 #numero de amostras

m_pi = np.loadtxt('texto.txt') #carrega o arquivo txt c matriz pseudo-inversa 

sinal_demodulado = m_pi.dot(dados[range(0,n_amostras)]) #multiplica matriz pseudo-inversa pelos dados

print"forma da matriz do sinal demodulado", sinal_demodulado.shape

#extracao dos componentes do sinal demodulado
amplitude = math.sqrt(pow(sinal_demodulado[0,0],2)+pow(sinal_demodulado[1,0],2))
print"amplitude ", amplitude
