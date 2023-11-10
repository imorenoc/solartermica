reset
set datafile separator ","

Cp = 4181.3 # J/(kgK)
Ac = 0.17   # m2

fy(fm,Cp,Ti,To,Ac,G)= (fm*Cp*(Ti-To))/(Ac*G)
fx(Ti,Ta,G) = (Ti-Ta)/G

f(x) = m*x+b
fit f(x) 'colector.csv' using (fx($1,$3,$4)):(fy($5/60, Cp, $2, $1,Ac,$4)) via m,b

set xlabel '$\dfrac{(Ti-Ta)}{G_I}$'
set ylabel '$\eta$'
set grid

plot 'colector.csv' using (fx($1,$3,$4)):(fy($5/60, Cp, $2, $1,Ac,$4)) notitle,\
     f(x)