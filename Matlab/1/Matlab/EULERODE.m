clc;
clearvars;
close all;
format short

h=0.001; %periodo de muestreo

ts=0:h:10;
cond_iniciales=[0;0;0];
opciones=odeset('RelTol' ,1e-06, 'AbsTol' , 1e-06, 'InitialStep',h,'MaxStep',h);
disp('Simulacion de un sistema lineal de tercer orden')
[t,x]=ode45('ode45terord',ts,cond_iniciales,opciones);
[n,m]=size(x(:,1));
ypos=zeros(n,m);
yvel=zeros(n,m);
yacel=zeros(n,m);
a1=exp(2)/pi^3;
a2=pi;
a3=exp(2)/pi^3;
alpha=exp(-pi)/pi^3;
ck0=1/h^3 + a1/h^2 + a2/h + a3;
ck1=3/h^3 + 2*a1/h^2 +a2/h;
ck2=3/h^3 + a1/h^2;
ck3=1/h^3;
for k=4:n
u=((tanh(ts(k)))/(1+(tanh(ts(k)).*(tanh(ts(k))))));
ypos(k)=(1/ck0)*(ck1*ypos(k-1)- ck2*ypos(k-2) + ck3*ypos(k-3)+alpha*u);
end

for k=2:n
    yvel(k)=(ypos(k)-ypos(k-1))/h;
end

for k=3:n
    yacel(k)=(ypos(k)-2*ypos(k-1)+ypos(k-2))/h^2;
end
figure
subplot(3,1,1);plot(t,x(:,1))
subplot(3,1,2);plot(t,ypos)
subplot(3,1,3);plot(t,x(:,1),t,ypos)

figure
subplot(3,1,1);plot(t,x(:,2))
subplot(3,1,2);plot(t,yvel)
subplot(3,1,3);plot(t,x(:,2),t,yvel)

figure
subplot(3,1,1);plot(t,x(:,3))
subplot(3,1,2);plot(t,yacel)
subplot(3,1,3);plot(t,x(:,3),t,yacel)