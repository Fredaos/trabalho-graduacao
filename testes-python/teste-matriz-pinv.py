#!/usr/bin/python2.7

#teste para aprender o que faz cada coisa no codigo da matriz pseudo-inversa
#codigo adaptado do trabalho de graduacao realizado pelo discente Samuel Alkmin

import numpy as np

fs = 20 #freq amostragem
pontos = 5 # pontos a serem analisados
f = 5 #freq sinal

passo = float(1)/fs
t = np.arange(0, 0.91, passo) #vetor igualmente espacado [inicio, fim, passo]
a = t[range(0, pontos)] #pega o num pontos de t e atribui para a variavel a
b = range(0, pontos) #so para testar

a_matrix = np.matrix(a)
b_matrix = np.matrix(b)

m1 = np.concatenate((a_matrix.transpose(),b_matrix.transpose()),axis=1) #junta as matrizes a e b
m2 = np.concatenate((m1,np.ones((pontos,1))),axis=1) #junta uma coluna de 1s em m1

m = np.matrix(m2)

pseudoinv = np.linalg.pinv(m) #calcula a matriz pseudo-inversa de m

np.savetxt("texto.txt", pseudoinv, fmt='%.3f', delimiter='') #funcao que salva os dados de um array em um arquivo .txt


