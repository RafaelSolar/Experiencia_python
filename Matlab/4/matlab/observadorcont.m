function oep=observadorcont(t,oe)
    x1=oe(1,1); x2=oe(2,1); x=[x1; x2]; % vector de estados.
    xe1=oe(3,1); xe2=oe(4,1); xe=[xe1; xe2]; % vector de estados del observador.
    global wn p xd kp kv;
    %Matriz A
    A=[0 1 ;
    -wn^2 -2*p*wn];
    %Vector B
    B=[0;
   wn^2];
    c=[1; 0];
    lambda=eig(A);
    
    L=-real(lambda);
    %Entrada con esquema de control
    xtildeob=xd-x1;
    u=kp*tanh(xtildeob)-kv*tanh(x2)+log(cosh(x1));
    z=B*u;
    Ao=A-L*c';
    
    xp=A*x+B*u;
    y=c'*x;
    xep=Ao*xe+L*y+z;
    oep=[xp;xep];
end