#!/usr/bin/python

# autor: Frederico Alves de Oliviera Silva RA: 11067110

# codigo para aquisicao de dados, demodulacao e controle PID
# codigo adaptado do trabalho de graduacao realizado pelo discente Samuel Alkmin

############################
# IMPORTACAO DE BIBLIOTECAS
############################
import numpy as np
import Adafruit_BBIO.GPIO as GPIO
import beaglebone_pru_adc as adc
import time


# abrir arquivo para realizar controle PID
text_file = open("Aquisicao_Demodulacao_Controle.txt","w")

################################################################
# DECLARACAO DE VARIAVEIS (estes valores nao sao definitivos)
################################################################
passoDigipot = 39.0625 #valor correspondente a cada divisao do digipot de 10k de 8 bits 10000/256
vi = 0.5 #tensao de entrada que vem do gerador de ondas
r1 = 10000 #resistencia do resistor 1
rs = 47.0 #resistencia do resistor sentinela
rL = 100 #valor da impedancia correspondente a uma primeira carga
correnteSet = 0.002555 #valor de referencia para a corrente
erroResistencia = 0 #parametro utilizado para a realizacao do controle

# variaveis do controle PID
instante = 0 #variavel de tempo para a realizacao de controle PID
kp = 2.5
ki = 0.5
kd = 0.7

p = 0
i = 0
d = 0

# preparo das portas da BBB para utilizacao
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_12", GPIO.OUT)

############################################################################################################
# INICIO DA ROTINA DE AMOSTRAGEM, DEMODULACAO E CONTROLE PID (tudo ocorre dentro de um laco de repeticao)
############################################################################################################
while True:
    tempoAtual = time.time()
    
    ############################
    # PROCESSO DE AMOSTRAGEM
    ############################
    
    
    ############################
    # PROCESSO DE DEMODULACAO
    ############################
    dados = dados[:, np.newaxis] #o comando newaxis acrescenta uma dimensao
    pts = 100 #numero de pontos amostrados para o calculo da matriz pseudo-inversa
    pseudoinv = np.loadtxt("matriz_pseudo-inversa.txt") #carrega o arquivo .txt
    produtoMatriz = pseudoinv.dot(dados[range(0,pts)]) #multiplica matriz pseudo-inversa pelos dados obtidos. Esta eh uma matriz de 3 linhas e 1 coluna

    #demodulacao
    amplitude = np.sqrt(pow(produtoMatriz[0,0],2)+pow(produtoMatriz[1,0],2))     
    fase = np.arctan(produtoMatriz[1,0]/produtoMatriz[0,0])
    offset = produtoMatriz[2,0]
    
    ############################
    # REALIZACAO DO CONTROLE PID
    ############################

    corrente = amplitude/rs
    erro_corrente = correnteSet - corrente
    erro_tensao = erro_corrente*rs
    erro_resistencia = erro_tensao*r1/vin
    delta_time = time.time() - tempoAtual
    
    #controle proporcional
    p = erro_resistencia*kp
    
    #controle integral
    i = i + erro_resistencia*ki*delta_time
    
    #controle derivativo
    d = (erroResistencia - erro_resistencia)*-1*kd*delta_time
    erroResistencia = erro_resistencia
    
    #PID
    pid = p+i+d
    
    iteracoes = int(pid/passoDigipot)
    
    if iteracoes < 0:
        iteracoes = iteracoes*-1
        
    instante = instante + delta_time
    
    text_file.write("%.8f" %corrente + " " + "%.5f " %instante + "\n")
    
    if pid > 0:
        for x in xrange(iteracoes):
            GPIO.output("P8_10", GPIO.LOW)
            GPIO.output("P8_12", GPIO.HIGH)
            GPIO.output("P8_12", GPIO.LOW)
            
    if pid < 0:
        for x in xrange(iteracoes):
            GPIO.output("P8_10", GPIO.HIGH)
            GPIO.output("P8_12", GPIO.HIGH)
            GPIO.output("P8_12", GPIO.LOW)

text_file.close()
