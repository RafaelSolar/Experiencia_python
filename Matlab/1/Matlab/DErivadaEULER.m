clc;
clearvars;
close all;
format short;

h=0.1;
t=0:h:10;
%[n1,m1]=size(t);
[renglones, columnas]=size(t); %dimension del vecotr t
%funcion a derivar

f=t;

%Derivada teorica

derteorica(1,1:columnas)=1;


derEuler=zeros(renglones,columnas);

for k=2:columnas
    derEuler(1,k)=(f(k)-f(k-1))/(t(k)-t(k-1));
end
plot(t,derteorica,t,derEuler)