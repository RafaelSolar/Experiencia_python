clc; clearvars; close all; format short;
%parametos de simulacion
ti=0;  %Tiempo inicial
tfin=10; %Tiempo final
h=0.001; %Periodo de muestreo
ts=ti:h:tfin; %Intervalo de simulacion
syms alpha0 alpha1 alpha2 alpha_0 alpha_1 alpha_2 alpha_0n alpha_1n alpha_2n ta  hs;
% Variables de estado fase
A=[0 1 0; %Matriz A
   0 0 1
   -5 -9 -9];
B=[0 %Vector B
   0
   1]; 
C=[1 3 1]; %Vector C
%-------

% RESOLUCION POR INTEGRACION DE RUNGE-KUTTA 4/5 ADAPTABLE
x_0=[0;0;-23]; %Condiciones inicilaes del sistema dinamico
opciones=odeset('RelTol',1e-06,'AbsTol',1e-06,'InitialStep',h,'MaxStep',h); %Propiedades de integración numérica
disp('Simulacion de sistema de tercer orden')
[t,x]=ode45('sisvarest',ts,x_0,opciones); %Comando que retorna la solucion del sistema dinamico
[n,m]=size(t); %Retorna las dimensiones del vector t en la primera columna (posicion)
y=zeros(n,1);
for i=1:n
    y(i,1)=C*[x(i,1);x(i,2);x(i,3)];
end

%RESOLUCION POR MODELO DISCRETO POR RETENEDOR DE ORDEN CERO

lamda=eig(A);

th=ti:h/1000:h; %Intervalo de integracion discreto
[n1,m1]=size(th);
Gamma=[0;0;0];
%Gamma en forma numerica
for i=1:n1
    hs=th(i);
    
    alphas=(inv([1 lamda(1) lamda(1)^2 ; 1 -0.5267 -0.0744 ; 0 -0.5931 0.6248])*[exp(lamda(1)*hs); exp(-0.5267*hs)*cos(0.5931*hs); -exp(-0.5267*hs)*sin(0.5931*hs)]);
    alpha0=alphas(1,1);
    alpha1=alphas(2,1);
    alpha2=alphas(3,1);
    phi=alpha0*eye(3)+alpha1*A+alpha2*(A*A);
    Gamma=Gamma+h*phi*B;
end

 hs=h;
 alphas=(inv([1 lamda(1) lamda(1)^2 ; 1 -0.5267 -0.0744 ; 0 -0.5931 0.6248])*[exp(lamda(1)*hs); exp(-0.5267*hs)*cos(0.5931*hs); -exp(-0.5267*hs)*sin(0.5931*hs)]);
 alpha0=alphas(1,1);
 alpha1=alphas(2,1);
 alpha2=alphas(3,1);
 phi=alpha0*eye(3)+alpha1*A+alpha2*(A*A);
 
 u(t>0)=1;
 u(1)=0;
 xk0=x_0;
 
 for i=2:n
     xk=phi*xk0+Gamma*u(i-1);
     
     xk11(i)=xk(1,1);
     xk21(i)=xk(2,1);
     xk31(i)=xk(3,1);
 end
 
yk=zeros(n,1);
for i=1:n
    yk(i,1)=C*[xk11(i);xk21(i);xk31(i)];
end


%Solucion Analitica
Integrala=[0;0;0];
for i=1:n
alphaana=(inv([1 lamda(1) lamda(1)^2 ; 1 -0.52668936 -0.074394857 ; 0 -0.59312439 0.62478461])*[exp(lamda(1)*t(i)); exp(-0.5267*t(i))*cos(0.5931*t(i)); -exp(-0.5267*t(i))*sin(0.5931*t(i))]);
alpha_0=alphaana(1,1);
alpha_1=alphaana(2,1);
alpha_2=alphaana(3,1);
eAt=alpha_0*eye(3)+alpha_1*A+alpha_2*(A*A);

alphaana_n=(inv([1 lamda(1) lamda(1)^2 ; 1 -0.52668936 -0.074394857; 0 -0.59312439 0.62478461])*[exp(lamda(1)*(t(i))); exp(-0.5267*(-t(i)))*cos(0.5931*(-t(i))); -exp(-0.5267*(-t(i)))*sin(0.5931*(-t(i)))]);
alpha_0n=alphaana_n(1,1);
alpha_1n=alphaana_n(2,1);
alpha_2n=alphaana_n(3,1);


eAtn=alpha_0n*eye(3)+alpha_1n*A+alpha_2n*(A*A);
Integrala=Integrala+h*(eAtn)*B*u(i);
x_ana=(eAt)*x_0+(eAt)*Integrala;
x_ana11(i)=x_ana(1,1);
x_ana21(i)=x_ana(2,1);
x_ana31(i)=x_ana(3,1);
end
y_ana=zeros(n,1);
for i=1:n
    y_ana(i,1)=C*[x_ana11(i);x_ana21(i);x_ana31(i)];
end


figure %Comparacion de posicion 
subplot(3,1,1);plot(t,x(:,1))
title('Grafica a) de posición por Runge-Kutta')
grid
xlabel('t (segundos)')
ylabel('y(t) (metros)')
subplot(3,1,2);plot(t,x_ana11)
title('Grafica b) de posicion analitica')
grid
xlabel('t (segundos)')
ylabel('y(t) (metros)')
subplot(3,1,3);plot(t,xk11)
title('Grafica c) de posicion por modelo discreto')
grid
xlabel('t (segundos)')
ylabel('y(t) (metros)')
figure
plot(t,x(:,1),t,xk11,t,x_ana11)
title('Comparacion de graficas de posicion')
grid
xlabel('t (segundos)')
ylabel('y(t) (metros)')
legend('R-K','Discreta','Analitica')

figure %Comparacion de velocidad
subplot(3,1,1);plot(t,x(:,2))
title('Grafica a) de velocidad por Runge-Kutta')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg)')

subplot(3,1,2);plot(t,x_ana21)
title('Grafica b) de velocidad analitica')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg)')

subplot(3,1,3);plot(t,xk21)
title('Grafica c) de velocidad por modelo discreto')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg)')

figure
plot(t,x(:,2),t,xk21,t,x_ana21)
title('Comparacion de graficas de velocidad')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg)')
legend('R-K','Dicreta', 'Analitica')

figure %Comparacion de aceleracion por INTEGRACION DE RUNGE-KUTTA 4/5 ADAPTABLE y POR METODO NUMERICO DE EULER
subplot(3,1,1);plot(t,x(:,3))
title('Grafica a) de aceleración por Runge-Kutta')
grid
xlabel('t (segundos)')
ylabel('ypp(t) (m/seg^2)')
subplot(3,1,2);plot(t,x_ana31)
title('Grafica b) de aceleracion analitica')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg^2)')
subplot(3,1,3);plot(t,xk31)
title('Grafica c) de aceleracion discreto')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg^2)')
figure
plot(t,x(:,3),t,xk31,t,x_ana31)
title('Comparacion de graficas de aceleracion')
grid
xlabel('t (segundos)')
ylabel('ypp(t) (m/seg^2)')
legend('R-K','Dicreta','Analitica')