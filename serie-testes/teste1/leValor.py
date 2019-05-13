#!/usr/bin/python

import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

file = open("teste5.txt","w+") # abre arquivo de texto chamado teste.txt

fim = time.time() + 1 # fim = 5 s

while time.time() < fim:
  valor = ADC.read("P9_39") # BBB le o valor no Analog Input 0 no pino P9_39
  tensao = valor*1.8 # converte o valor de tensao lido para a escala de volts
  file.write("tensao %.3f\n" %(tensao)) # escreve o valor de tensao no arquivo de texto

file.close() # fecha o arquivo de texto
