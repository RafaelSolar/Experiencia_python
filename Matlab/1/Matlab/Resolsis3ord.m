clc; clearvars; close all; format short;
%parametos de simulacion
ti=0;  %Tiempo inicial
tfin=10; %Tiempo final
h=0.001; %Periodo de muestreo
ts=ti:h:tfin; %Intervalo de simulacion

% RESOLUCION POR INTEGRACION DE RUNGE-KUTTA 4/5 ADAPTABLE
cond_iniciales=[0;-5;5]; %Condiciones inicilaes del sistema dinamico
opciones=odeset('RelTol',1e-06,'AbsTol',1e-06,'InitialStep',h,'MaxStep',h); %Propiedades de integración numérica
disp('Simulacion de sistema de tercer orden')
[t,x]=ode45('sis3ord',ts,cond_iniciales,opciones); %Comando que retorna la solucion del sistema dinamico
[n,m]=size(x(:,1)); %Retorna las dimension del vector x en la primera columna (posicion)

% RESOLUCION POR METODO NUMERICO DE EULER
ypos=zeros(n,m); %Creamos matriz nxm de ceros para la posicion
yvel=zeros(n,m); %Creamos matriz nxm de ceros para la velocidad
yacel=zeros(n,m); %Creamos matriz nxm de ceros para la aceleracion

%Constantes del metodo numerico
a3=pi^3;
a2=exp(2);
a1=pi^4;
a0=a2;
alpha=exp(-pi);
ck0=(a3/h^3)+(a2/h^2)+(a1/h)+a0;
ck1=(3*a3/h^3)+(2*a2/h^2)+a1/h;
ck2=(3*a3/h^3)+a2/h^2;
ck3=a3/h^3;

for k=4:n %Simulacion de la posicion del sistema discreto de tercer orden 
    u=alpha*((tanh(ts(k)))/(1+(tanh(ts(k))).*(tanh(ts(k))))); % Deficion de la entrada
    ypos(k)=(ck0^(-1))*(u+ck1*ypos(k-1)-ck2*ypos(k-2)+ck3*ypos(k-3)); % Solucion y(tk)
end

for k=2:n %Simulacion de la velocidad del sistema discreto de tercer orden 
    yvel(k)=(ypos(k)-ypos(k-1))/h; %Solicion yp(tk)
end

for k=3:n %Simulacion de la aceleracion del sistema discreto de tercer orden 
    yacel(k)=(ypos(k)-2*ypos(k-1)+ypos(k-2))/h^2; %Solucion ypp(yk)
end

figure %Comparacion de posicion por INTEGRACION DE RUNGE-KUTTA 4/5 ADAPTABLE y POR METODO NUMERICO DE EULER
subplot(3,1,1);plot(t,x(:,1))
title('Grafica a) de posición por Runge-Kutta')
grid
xlabel('t (segundos)')
ylabel('y(t) (metros)')
subplot(3,1,2);plot(t,ypos)
title('Grafica b) de posicion por Metodo de Euler')
grid
xlabel('t (segundos)')
ylabel('y(t) (metros)')
subplot(3,1,3);plot(t,x(:,1),t,ypos)
title('Grafica c)Comparacion de graficas')
grid
xlabel('t (segundos)')
ylabel('y(t) (metros)')
legend('R-K','Euler')

figure %Comparacion de velocidad por INTEGRACION DE RUNGE-KUTTA 4/5 ADAPTABLE y POR METODO NUMERICO DE EULER
subplot(3,1,2);plot(t,x(:,2))
title('Grafica a) de velocidad por Runge-Kutta')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg)')

subplot(3,1,2);plot(t,yvel)
title('Grafica b) de velocidad por Metodo de Euler')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg)')
subplot(3,1,3);plot(t,x(:,2),t,yvel)
title('Grafica c) Comparacion de graficas')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg)')
legend('R-K','Euler')
figure %Comparacion de aceleracion por INTEGRACION DE RUNGE-KUTTA 4/5 ADAPTABLE y POR METODO NUMERICO DE EULER
subplot(3,1,3);plot(t,x(:,3))
title('Grafica a) de aceleración por Runge-Kutta')
grid
xlabel('t (segundos)')
ylabel('ypp(t) (m/seg^2)')
subplot(3,1,2);plot(t,yacel)
title('Grafica b) de aceleracion por Metodo de Euler')
grid
xlabel('t (segundos)')
ylabel('yp(t) (m/seg^2)')
subplot(3,1,3);plot(t,x(:,3),t,yacel)
title('Grafica c) Comparacion de graficas')
grid
xlabel('t (segundos)')
ylabel('ypp(t) (m/seg^2)')
legend('R-K','Euler')
