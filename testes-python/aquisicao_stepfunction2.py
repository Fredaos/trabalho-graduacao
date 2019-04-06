#!/usr/bin/python

# autor: Frederico Alves de Oliviera Silva RA: 11067110

# codigo para aquisicao de dados, demodulacao e controle PID
# codigo adaptado do trabalho de graduacao realizado pelo discente Samuel Alkmin

############################
# IMPORTACAO DE BIBLIOTECAS
############################
import numpy as np
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
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
correnteSet = 0.002 #valor de referencia para a corrente
erroResistencia = 0 #parametro utilizado para a realizacao do controle
cont1 = 0 # contador para fazer o degrau LOW
cont2 = 0 # contador 2 para fazer degrau HIGH

# variaveis do controle PID
instante = 0 #variavel de tempo para a realizacao de controle PID
kp = 2.5
ki = 0.5
kd = 0.7

p = 0
i = 0
d = 0

# preparo das portas da BBB para utilizacao
GPIO.setup("P9_31", GPIO.OUT)
GPIO.setup("P9_20", GPIO.OUT)
GPIO.setup("P9_30", GPIO.OUT)
GPIO.setup("P9_29", GPIO.IN)
GPIO.setup("P9_22", GPIO.OUT)
GPIO.setup("P9_18", GPIO.OUT)
GPIO.setup("P9_21", GPIO.IN)
GPIO.setup("P9_17", GPIO.OUT)

ADC.setup()

############################################################################################################
# INICIO DA ROTINA DE AMOSTRAGEM, DEMODULACAO E CONTROLE PID (tudo ocorre dentro de um laco de repeticao)
############################################################################################################
print("Inicio")
while cont2 < 2:
    while cont1 < 40:
        tempoAtual = time.time()
        dados = []
        ############################
        # PROCESSO DE AMOSTRAGEM
        ############################
        # baseado no codigo do github encontrado em: https://github.com/pgmmpk/beaglebone_pru_adc
        numsamples = 100 # how many samples to capture
        
        capture = adc.Capture()
        capture.encoder0_pin = 0 # posiciona para valor [0-7] e habilita encoder 0
        capture.encoder0_dalay = 100 # atraso para filtrar ruido
        capture.enconder0_threshold = 5000 # nivel para Schmitt do encoder
        capture.oscilloscope_init(adc.OFF_ENC0_VALUES, numsamples) # captures AIN0 - the first elt in AIN array
        capture.cap_dalay = 100 # atraso introduzido para baixar a velocidade de captura
        
        capture.start()
        
        for _ in range(200000):
        	if capture.oscilloscope_is_complete():
        		break
        	   
        capture.stop() # sinalizacao no driver para sair do loot de captura e parar
        capture.wait() # bloqueia chamada ate o driver parar
        
        # Salva valores do osciloscopio para um arquivo.txt
        for x in capture.oscilloscope_data(numsamples): # recupera num samples de dados do driver de memoria DDR
        	tensao = ('%0.6f' %((x*1.8)/4096))
            tensao = float(tensao) 
            dados.append(tensao) # adiciona valores de tensao em dados
            
        dados = np.asarray(dados) #converte data para array
        capture.close() # libera todos os recursos do driver
        
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
        degrau = np.heaviside(corrente,0)
        erro_corrente = correnteSet - corrente
        erro_tensao = erro_corrente*rs
        erro_resistencia = erro_tensao*r1/vi
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
        
        text_file.write("%.8f" %degrau + " " + "%.5f " %instante + "\n")
        
        if pid > 0:
            for x in xrange(iteracoes):
                GPIO.output("P9_20", GPIO.LOW)             
                GPIO.output("P9_22", GPIO.LOW)
                GPIO.output("P9_18", GPIO.LOW)
                GPIO.output("P9_17", GPIO.LOW)
                
                GPIO.output("P9_31", GPIO.HIGH)
                GPIO.output("P9_31", GPIO.LOW)
                GPIO.output("P9_30", GPIO.HIGH)
                GPIO.output("P9_30", GPIO.LOW)
                            
        if pid < 0:
            for x in xrange(iteracoes):
                GPIO.output("P9_20", GPIO.HIGH)             
                GPIO.output("P9_22", GPIO.HIGH)
                GPIO.output("P9_18", GPIO.HIGH)
                GPIO.output("P9_17", GPIO.HIGH)
                            
                GPIO.output("P9_31", GPIO.HIGH)
                GPIO.output("P9_31", GPIO.LOW)
                GPIO.output("P9_30", GPIO.HIGH)
                GPIO.output("P9_30", GPIO.LOW)
        cont1 = cont1 + 1
    correnteSet = float(input("digite 0.004 (este valor eh 4 mA)"))
    cont1 = 0
    cont2 = cont2 + 1
    
text_file.close()
print("Text file close")
print("Fim")    