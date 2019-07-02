#!/usr/bin/python

import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

file = open("aq_adc.txt","w+") # abre arquivo de texto chamado teste.txt

t0 = time.time() #tempo inicial [s]
tempo = 0 # [s]
fim = 5 # [s]

while tempo < fim:
  valor = ADC.read("P9_39") # BBB le o valor no Analog Input 0 no pino P9_39
  tensao = valor*1.8 # converte o valor de tensao lido para a escala de volts
  file.write("%.3f \n" %(tensao)) # escreve o valor de tensao no arquivo de texto
  tempo = time.time() - t0

file.close() # fecha o arquivo de texto
