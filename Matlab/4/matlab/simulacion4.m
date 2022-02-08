    clc; clearvars; close all; format short;

    %Parametros de control
    global xd kp kv wn p;
    c=[1 ;0];
    xd=12;
    kp=15;
    kv=0.4*kp;
    wn=0.7;
    p=0.175;
    syms hs alpha0 alpha1
    
    ti=0; tfin=10; h=0.001; %Parametros de simulación
    ts=ti:h:tfin; %Intervalo de simulacion
    
     %---------- Sistema continuo
    opciones=odeset('RelTol',1e-06,'AbsTol',1e-06,'InitialStep',h,'MaxStep',h); %Propiedades de integración numérica
    oe0=[-3; 1;-3;1];
    [t, oe]=ode45( 'observadorcont',ts,oe0,opciones); % algoritmo de integración numérica Runge-Kutta 4/5
    [ren,colum]=size(t);
     xode=oe(:,1);
    xpode=oe(:,2);
    
%------- Sistema discreto
    th=ti:h/1000:h;
    [n1,m1]=size(th);
    A=[0 1;-wn^2 -2*p*wn];
    B=[0;wn^2];
    Gamma=[0;0];
   % Integral_PID=x0(3,1);
    Integral=[0;0];

    for i=1:n1
        hs=th(i);
        alpha0=exp(-0.1225*hs)*(cos(0.6892*hs)+0.1225*sin(0.6892*hs)/0.6892);
        alpha1=exp(-0.1225*hs)*sin(0.6892*hs)/0.6892;
        phi=alpha0*eye(2)+alpha1*A;
        Gamma=Gamma+h*phi*B;
    end
    hs=h;
    alpha0=exp(-0.1225*hs)*(cos(0.6892*hs)+0.1225*sin(0.6892*hs)/0.6892);
    alpha1=exp(-0.1225*hs)*sin(0.6892*hs)/0.6892;
    phi=alpha0*eye(2)+alpha1*A;
    
    lambda=eig(A);
    Ld=-real(lambda);
    phi_0=phi-Ld*c';
    xk=[oe0(1,1);oe0(2,1)];
    xkobs=[oe0(1,1);oe0(2,1)];
    for i=2:ren
        xtildedis=xd-oe(i,1);
       % Integral_PID=Integral_PID+h*xtildedis;
        u(i)=kp*tanh(xtildedis)-kv*tanh(oe(i,2))+log(cosh(oe(i,1)));
        xk=phi*xk+Gamma*u(i-1);
        xk11(i)=xk(1,1);
        xk21(i)=xk(2,1);
        
        %Observador
        xkobs=phi_0*xkobs+Ld*c'*xk+Gamma*u(i-1);
        xk11e(i)=xkobs(1,1);
        xk22e(i)=xkobs(2,1);

    end
    xkauxd=[xk11,xk21]; xkobsee=[xk11e,xk22e];
    yode=zeros(ren,1);
    ydis=zeros(ren,1);
    for i=2:ren
        yode(i)=c'*[xode(i); xpode(i)];
        ydis(i)=c'*[ xk11(i); xk21(i)];
    end
    error_poscon=norm(oe(:,1)-oe(:,3),2);
    error_velcon=norm(oe(:,2)-oe(:,4),2);
    error_posdis=norm(xkauxd(:,1)-xkobsee(:,1),2);
    error_veldis=norm(xkauxd(:,2)-xkobsee(:,2),2);
    figure %Posicion 
    subplot(3,1,1);plot(t,yode)
    title('Grafica a) de posición por Runge-Kutta')
    grid
    xlabel('t (segundos)')
    ylabel('Posicion(m)')

    subplot(3,1,2);plot(t, oe(:,3))
    title('Grafica b) de posicion observador continuo')
    grid
    xlabel('t (segundos)')
    ylabel('posicion(m)')
    

    subplot(3,1,3);plot(t,yode,t, oe(:,3))
    title('Grafica c) de comparación de posición')
    grid
    xlabel('t (segundos)')
    ylabel('Posicion(m)')
    legend('R-K','Observador')
    
    %----------------------------------------------
        figure %Posicion discreto
    subplot(3,1,1);plot(t,ydis)
    title('Grafica a) de x1 del modelo discreto')
    grid
    xlabel('t (segundos)')
    ylabel('x1dis-Posicion(m)')

    subplot(3,1,2);plot(t, xk11e)
    title('Grafica b) de x1e observador discreto')
    grid
    xlabel('t (segundos)')
    ylabel('x1dise-posicion(m)')
    

    subplot(3,1,3);plot(t,ydis, t,  xk11e)
    title('Grafica c) de comparación de posición')
    grid
    xlabel('t (segundos)')
    ylabel('Posicion(m)')
    legend('Discreto','Observador')
    
    
% %--------------------------------------------------------
    figure %Velocidad continuo
    subplot(3,1,1);plot(t,xpode)
    title('Grafica a) de velocidad por Runge-Kutta')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')

    subplot(3,1,2);plot(t, oe(:,4))
    title('Grafica b) de velocidad por sistema discreto')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')

    subplot(3,1,3);plot(t,xpode,t, oe(:,4))
    title('Grafica c) de comparación de velocidad')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')
    legend('R-K','Observador')
    %---------------------------------
        figure %Velocidad dicreto
    subplot(3,1,1);plot(t,xk21)
    title('Grafica a) de velocidad por sistema discreo')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')

    subplot(3,1,2);plot(t, xk22e)
    title('Grafica b) de velocidad por sistema discreto')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')

    subplot(3,1,3);plot(t,xk21,t,  xk22e)
    title('Grafica c) de comparación de velocidad')
    grid
    xlabel('t (segundos)')
    ylabel('Velocidad (m/s)')
    legend('Discreto','Observador')


 
