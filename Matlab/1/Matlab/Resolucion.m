clc;
clearvars;
close all;
format short;
%parametos de simulacion
ti=0;
tf=10;
h=0.001;
%Intervalo de simulacion
ts=ti:h:tf;
cond_iniciales=[0;0];
opciones=odeset('RelTol',1e-06,'AbsTol',1e-06,'InitialStep',h,'MaxStep',h);
disp('Simulacion de ODE')
[t,x]=ode45('sso',ts,cond_iniciales,opciones);
figure
subplot(2,1,1);plot(t,x(:,1))
subplot(2,1,2);plot(t,x(:,2))
%subplot(3,1,1);plot(x(:,1),(x(:,2)))