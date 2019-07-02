#!/usr/bin/python

import beaglebone_pru_adc as adc
import time
import numpy as np

numsamples =700000

file = open("pru_700ksamples.txt","w+")

capture = adc.Capture()
capture.encoder0_pin = 0
capture.encoder0_threshold = 4096

tempo = 0
fim = 5

capture.start()
t0 = time.time()
print("inicio da captura")

while tempo < fim:

	tempo = time.time() - t0
	tensao = float(capture.encoder0_values[0])*1.8/4096
	file.write("%.3f \n" %(tensao))

capture.stop()
capture.wait()
capture.close()

print("fim da captura")
file.close()
print("fim do codigo")
