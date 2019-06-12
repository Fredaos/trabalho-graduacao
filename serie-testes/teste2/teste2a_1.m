% Variacao da frequencia de amostragem da BeagleBone
% nome: Frederico Alves de Oliveira Silva 

clear all;
close all;
clc;

dados = load("teste2a_5.txt");
fs = length(dados(:,2));

figure;
scatter(dados(:,1),dados(:,2),"r");
title('tensao x tempo (600 sps)');
xlabel('tempo [s]');
ylabel('tensao [V]');
grid on;

