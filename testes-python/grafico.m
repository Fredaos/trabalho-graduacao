% Grafico
clc;
close all;
clear all;

g = load('spi2.txt'); #freq amostragem 1000 ksps

%grafico
figure()
plot(g(:,2),g(:,1))
title('Corrente vs. tempo')
xlabel('t [s]')
ylabel('I [A]')
grid()
