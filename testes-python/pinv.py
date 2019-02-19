#!/usr/bin/python

#discente: Frederico Alves de Oliveira Silva RA: 11067110

#primeiro codigo para obtencao da matriz pseudo-inversa com os sinais I e Q para o calculo de demodulacao
#codigo adaptado do trabalho de graduacao realizado pelo discente Samuel Alkmin

import numpy as np

# declaracao de variaveis
fs = 110000 #freq de amostragem 110 ksps (obedece ao teorema de Nyquist fs >= 2*f) 
pts = 100 # pontos a serem analisados
f = 10000 #freq sinal 10 kHz
passo = float(1)/fs
tempo = np.arange(0, 1, passo) #vetor igualmente espacado [inicio, fim, passo]
i = np.cos(2*np.pi*f*tempo[range(0, pts)]) # o sinal in-phase, i, eh um cosseno, a funcao range pega o num pontos de t e atribui para a variavel a
q = np.sin(2*np.pi*f*tempo[range(0, pts)]) # o sinal quadrature, q, eh um seno

# obtencao das matrizes para os sinais senoidais
i_matrix = np.matrix(i)
q_matrix = np.matrix(q)

# concatenacao das matrizes i e q
m1 = np.concatenate((i_matrix.transpose(),q_matrix.transpose()),axis=1) #junta as matrizes i e q

# adicao de uma coluna de 1s na matriz
m2 = np.concatenate((m1,np.ones((pts,1))),axis=1) #junta uma coluna de 1s em m1

# obtencao "formal" de uma matriz com os sinais i, q e 1s
m = np.matrix(m2)

# obtencao da matriz pseudo-inversa a partir da matriz m
pseudoinv = np.linalg.pinv(m) #calcula a matriz pseudo-inversa de m

np.savetxt("matriz_pseudo-inversa.txt", pseudoinv, fmt='%.5f', delimiter=' ') #funcao que salva os dados de um array em um arquivo .txt
