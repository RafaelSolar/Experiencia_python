    function xp=siscontrol(t,x) %Funcion del sistema dinamico
    global xd kp kv wn p;
    x1=x(1);
    x2=x(2);
    x3=x(3);
    %Matriz A
    A=[0 1 ;
    -wn^2 -2*p*wn];
    %Vector B
    B=[0;
   wn^2];
    %Parametros
    xtilde=xd-x1;
    epsi=xtilde;
    u=kp*tanh(xtilde)-kv*tanh(x2)+log(cosh(x1));
    %Sistema dinamico lineal
    ode=A*[x1;x2]+B*u;
    xp=[ode(1);ode(2);epsi];
    end