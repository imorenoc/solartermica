from aux import *
from ps import *

# Tiempo solar
h= 13
m= 30
s= 0

Year = 2023
Month = 2
Day = 27

phi=d2r(27.16)

N =doy (Year, Month, Day)
d = delta(N)

HMS = hms(h,m,s)
dt = 0 #tiempo solar
tp = 0 #tiempo solar
w = omega(HMS, dt, tp)

tz = theta_z(phi, d, w)
gs = gamma_s(phi, d, w)

print(r2d(tz), r2d(gs))
print("(%.2f, %.2f)" % (r2d(tz), r2d(gs)))
