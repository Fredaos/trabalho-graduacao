#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time
import beaglebone_pru_adc as adc

# configuracao dos pinos
GPIO.setup("P8_10", GPIO.OUT) # clock
GPIO.setup("P8_12", GPIO.OUT) # up/down

# arquivo de texto
file = open("teste6c.txt","w+")

numsamples = 200 # numero de amostras

capture = adc.Capture()
capture.encoder0_pin = 0
capture.oscilloscope_init(adc.OFF_ENC0_VALUES,numsamples)
capture.encoder0_threshold = 4096

tempo = 0

print("inicio da captura")
capture.start()
t0 = time.time()

while tempo <= 4:
	tempo = time.time() - t0

	if tempo <= 2:
		print("descer")
		GPIO.output("P8_12",0)
		GPIO.output("P8_10",1)
		GPIO.output("P8_10",0)
		tensao = float(capture.encoder0_values[0])*1.8/4096
		file.write("%.3f \n" %(tensao))
	else:
		print("subir")
		GPIO.output("P8_12",GPIO.HIGH)
		GPIO.output("P8_10",GPIO.HIGH)
		GPIO.output("P8_10",GPIO.LOW)
		tensao = float(capture.encoder0_values[0])*1.8/4096
		file.write("%.3f \n" %(tensao))

capture.stop()
capture.wait()
capture.close()

print("fim da captura")
file.close()
print("fim")
