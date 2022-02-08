clc;
clearvars;
close all;
format short;
t1=0; tf=10; h=0.001;
ts=t1:h:tf;
cond_ini=[0;0];
opciones=odeset(' RelTol',1e-06,' AbsTol ',1e-06, 'InitialStep ',h,' MaxStep ',h);
disp( 'Simulación de un sistema lineal de segundo orden' )
[t,x]=ode45('sso',ts,cond_ini,opciones);
[n,m]=size(x(:,1));
y=zeros(n,m)

