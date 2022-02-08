     clc; clearvars; close all; format short;
     
     syms p11 p22 p21 p12 alpha0 alpha1 p11d p22d p21d p12d alpha0d alpha1d;
     
     disp('Analisis de estabalidad del observador continuo')
     
     %MAtriz A0
     A0=[-0.1225 1;-0.6125 -0.245]
     %Matriz p
     P=[p11 p12;p21 p22];
     
     %Punto de equilirio unico 
     detA0=det(A0)
     
     %A0TP+PA0
     Ecua=A0'*P+P*A0;
     Ecuasim=vpa(Ecua,4)
     
     % Ecuaciones del sistema
    mQecu=[-0.245 -1.225 0;
          1 -0.3675 -0.6125;
             0 2 -0.49];

     alpha0=1; alpha1=1;   
     
        mAlpha=[-alpha0;
            0;
        -alpha1];
     
     %Hallar matriz Q
     Pr=inv(mQecu)*mAlpha
     Prn=[Pr(1,1) Pr(2,1);Pr(2,1) Pr(3,1)]
     
     
     disp('Analisis de estabalidad del observador dicreto')
     
     %MAtriz A0
     phi0=[-0.8775 0.001;-0.123 0.9998]
     %Matriz p
     P=[p11d p12d;p21d p22d];
     
     %Punto de equilirio unico 
     detphi0=det(phi0)
     
     Ecuad=phi0'*P*phi0-P;
     Ecuasimd=vpa(Ecuad,4)
     
     % Ecuaciones del sistema
    mQecud=[-0.23 (0.1079+0.1079) 0.01513;
          -0.0008775 (-1.877-0.000123) -0.123;
             1.0e-6 (0.0009998+0.0009998) -0.0004];

     alpha0d=1; alpha1d=1;   
     
        mAlphad=[-alpha0d;
            0;
        -alpha1d];
     
     %Hallar matriz Q
     Prd=inv(mQecud)*mAlphad
     Prnd=[Prd(1,1) Prd(2,1);Prd(2,1) Prd(3,1)]
     det(Prnd)
     
     