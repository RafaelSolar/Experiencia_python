function xp=ode45terord(t,x)

A=[0 1 0;0 0 1;(-exp(2)/pi^3) -pi (-exp(2)/pi^3)];
B=[0;0;exp(-pi)/pi^3];

u=((tanh(t))/(1+(tanh(t)).*(tanh(t))));
xp=A*x+B*u;
end
