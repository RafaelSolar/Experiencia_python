    clc; clearvars; close all; format short;

    %Parametros de control PID
    global xd kp kv ki;
    xd=5;
    kp=15;
    kv=0.7*kp;
    ki=0.00857*kv;
%     kp=10;
%     kv=0.7*kp;
%     ki=0.015*kv;
    syms hs alpha0 alpha1
    
    ti=0; tfin=10; h=0.001; %Parametros de simulación
    ts=ti:h:tfin; %Intervalo de simulacion

    x0=[-15;12;2]; %Condiciones inicilaes del sistema dinamico
    opciones=odeset('RelTol',1e-06,'AbsTol',1e-06,'InitialStep',h,'MaxStep',h); %Propiedades de integración numérica
    disp('Simulacion de sistema de tercer orden')
    [t,x]=ode45('PIDsis',ts,x0,opciones); %Comando que retorna la solucion del sistema dinamico
    xode=x(:,1);
    xpode=x(:,2);
    error=x(:,3);
    [ren,colum]=size(t);
    
%------- Sistema discreto
    th=ti:h/1000:h;
    [n1,m1]=size(th);
    A=[0 1;-0.33 -0.45];
    B=[0;1];
    Gamma=[0;0];
    Integral_PID=x0(3,1);
    Integral=[0;0];

    for i=1:n1
        hs=th(i);
        %alpha0=exp(-0.225*hs)*cos(0.5286*hs)+(exp(-0.225*hs)*sin(0.5286*hs))/(0.5286);
        alpha0=exp(-0.225*hs)*(cos(0.5286*hs)+0.225*sin(0.5286*hs)/0.5286);
        %alpha1=(exp(-0.225*hs)*sin(0.5286*hs))/(0.5286);
        alpha1=exp(-0.225*hs)*sin(0.5286*hs)/0.5286;
        phi=alpha0*eye(2)+alpha1*A;
        Gamma=Gamma+h*phi*B;
    end
    hs=h;
    alpha0=exp(-0.225*hs)*(cos(0.5286*hs)+0.225*sin(0.5286*hs)/0.5286);
    alpha1=exp(-0.225*hs)*sin(0.5286*hs)/0.5286;
    phi=alpha0*eye(2)+alpha1*A;
    xk=[x0(1,1);x0(2,1)];
    for i=2:ren
        xtildedis=xd-x(i,1);
        Integral_PID=Integral_PID+h*xtildedis;
        u(i)=kp*xtildedis+ki*Integral_PID-kv*x(i,2);
        
        xk=phi*xk+Gamma*u(i-1);
        
        xk11(i)=xk(1,1);
        xk21(i)=xk(2,1);
    end
    errorposode=zeros(ren,colum);
    errorposdis=zeros(ren,colum);
    for i=1:ren
        errorposode(i)=xd-xode(i);
        errorposdis(i)=xd-xk11(i);
    end


    figure %Posicion 
    subplot(3,1,1);plot(t,xode)
    title('Grafica a) de posición por Runge-Kutta')
    grid
    xlabel('t (segundos)')
    ylabel('Posicion(m)')

    subplot(3,1,2);plot(t,xk11)
    title('Grafica b) de posición por sistema discreto')
    grid
    xlabel('t (segundos)')
    ylabel('Posicion(m)')

    subplot(3,1,3);plot(t,xode,t,xk11)
    title('Grafica c) de comparación de posición')
    grid
    xlabel('t (segundos)')
    ylabel('Posicion(m)')
    legend('R-K','Discreto')
%--------------------------------------------------------
    figure %Velocidad
    subplot(3,1,1);plot(t,xpode)
    title('Grafica a) de velocidad por Runge-Kutta')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')

    subplot(3,1,2);plot(t,xk21)
    title('Grafica b) de velocidad por sistema discreto')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')

    subplot(3,1,3);plot(t,xpode,t,xk21)
    title('Grafica c) de comparación de velocidad')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')
    legend('R-K','Discreto')
    figure % error de posicion
    subplot(3,1,1);plot(t,errorposode)
    title('Grafica del error de posición de Runge-Kutta')
    grid
    xlabel('t (segundos)')
    ylabel('Error de posicion (m)')
    subplot(3,1,2);plot(t,errorposdis)
    title('Grafica del error de posición de sistema discreto')
    grid
    xlabel('t (segundos)')
    ylabel('Error de posicion (m)')
    subplot(3,1,3);plot(t,errorposode,t,errorposdis)
    title('Grafica c) de comparación de error de posicion')
    grid
    xlabel('t (segundos)')
    ylabel('Error de posicion (m)')
    legend('R-K','Discreto')