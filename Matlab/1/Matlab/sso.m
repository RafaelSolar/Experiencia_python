function xp=sso(t,x)
%Frecuencia natural de resonancia
w_n=1;
%Factor de amortiguamiento
rho=0.1;

A=[0 1; -w_n^2 -2*rho*w_n];
B=[0; w_n*w_n];
%señal de entrada
u=1;
xp=A*x+B*u;

end