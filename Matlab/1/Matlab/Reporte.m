clc;
clearvars;
close all;
format short;
%parametos de simulacion
ti=0;
tfin=10;
h=0.001;
%Intervalo de simulacion
ts=ti:h:tfin;
cond_iniciales=[0;0;0];
opciones=odeset('RelTol',1e-06,'AbsTol',1e-06,'InitialStep',h,'MaxStep',h);
disp('Simulacion de ODE')
[t,x]=ode45('sis3ord',ts,cond_iniciales,opciones);
[n,m]=size(x(:,1));
y=zeros(n,m);
a3=pi^3;
a2=exp(2);
a1=pi^4;
a0=a2;
alpha=exp(-pi);
ck0=(a3/h^3)+(a2/h^2)+(a1/h)+a0;
ck1=(3*a3/h^3)+(2*a2/h^2)+a1/h;
ck2=(3*a3/h^3)+a2/h^2;
ck3=a3/h^3;
for k=4:n
    u=((tanh(k))/(1+(tanh(k)).^2));
    y(k)=(ck0^(-1))*(alpha*u+ck1*y(k-1)-ck2*y(k-2)+ck3*y(k-3));
end
figure
subplot(3,1,1);plot(t,x(:,1))
subplot(3,1,2);plot(t,y)
subplot(3,1,3);plot(t,x(:,1),t,y)

