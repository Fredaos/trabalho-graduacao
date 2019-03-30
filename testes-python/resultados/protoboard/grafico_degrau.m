%Nome: Frederico
% Grafico Degrau
clear all; close all; clc;

data = load('Degrau1.txt');
data2 = load('Degrau2.txt');
data3 = load('Degrau3.txt');
data4 = load('Degrau4.txt');
data5 = load('Degrau5.txt');

figure();
plot(data(:,2),data(:,1))
figure();
plot(data2(:,2),data2(:,1))
figure();
plot(data3(:,2),data3(:,1))
figure();
plot(data4(:,2),data4(:,1))
figure();
plot(data5(:,2),data5(:,1))