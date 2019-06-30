#!/usr/bin/python

import beaglebone_pru_adc as adc
import time
import numpy as np

numsamples =550000

file = open("pru_550ksamples.txt","w+")

capture = adc.Capture()
capture.encoder0_pin = 0
capture.oscilloscope_init(adc.OFF_ENC0_VALUES,numsamples)
capture.encoder0_threshold = 4096

tempo = 0
fim = 5

capture.start()
t0 = time.time()

print("inicio da captura")

while tempo < fim:

#	if capture.oscilloscope_is_complete():
#		break
	tempo = time.time() - t0

capture.stop()
capture.wait()
capture.close()

print("fim da captura")

for x in capture.oscilloscope_data(numsamples):
	tensao = float(x)*1.8/4096
	file.write("%.3f \n" %(tensao))

file.close()
print("fim do codigo")
