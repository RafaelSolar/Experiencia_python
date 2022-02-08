function xp=sis3ord(t,x) %Funcion del sistema dinamico
%Matriz A
A=[0 1 0;
  0 0 1;
  -exp(2)/pi^3 -pi -exp(2)/pi^3];
%Vector B
B=[0;
    0;
    exp(-pi)/pi^3];
%Señal de entrada u(t)
u=((tanh(t))/(1+(tanh(t)).*(tanh(t))));
%Sistema dinamico lineal
xp=A*x+B*u;
end