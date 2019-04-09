% Graficos protoboard

clc;
close all;
clear all;

a1 = load('Aquisicao_Demodulacao_Controle.txt');
a2 = load('Aquisicao_Demodulacao_Controle2.txt');
a3 = load('Aquisicao_Demodulacao_Controle3.txt');
a4 = load('Aquisicao_Demodulacao_Controle4.txt');
a5 = load('Aquisicao_Demodulacao_Controle5.txt');
a6 = load('Aquisicao_Demodulacao_Controle6.txt');

% Arquivo 1
figure()
plot(a1(:,2),a1(:,1))
title('Corrente vs. tempo')
xlabel('t [s]')
ylabel('I [A]')
grid()

% Arquivo 2
figure()
plot(a2(:,2),a2(:,1))
title('Corrente vs. tempo')
xlabel('t [s]')
ylabel('I [A]')
grid()

% Arquivo 3
figure()
plot(a3(:,2),a3(:,1))
title('Corrente vs. tempo')
xlabel('t [s]')
ylabel('I [A]')
grid()

% Arquivo 4
figure()
plot(a4(:,2),a4(:,1))
title('Corrente vs. tempo')
xlabel('t [s]')
ylabel('I [A]')
grid()

% Arquivo 5
figure()
plot(a5(:,2),a5(:,1))
title('Corrente vs. tempo')
xlabel('t [s]')
ylabel('I [A]')
grid()

% Arquivo 6
figure()
plot(a6(:,2),a6(:,1))
title('Corrente vs. tempo')
xlabel('t [s]')
ylabel('I [A]')
grid()