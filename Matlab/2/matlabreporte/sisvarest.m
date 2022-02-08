function xp=sisvarest(t,x) %Funcion del sistema dinamico
%Matriz A
A=[0 1 0;
  0 0 1;
  -5 -9 -9];
%Vector B
B=[0;
    0;
     1];
%Señal de entrada u(t)
u(t==0)=0;
u(t>0)=1;
%Sistema dinamico lineal
xp=A*x+B*u;
end