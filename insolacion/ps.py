import numpy as np
from myfunc import *
from math import sin, cos, acos, tan, atan2, pi

# Las salidas de las funciones radianes
# -------------------------------------

#print("Funciones para el calculo de la posición solar, en [rad]")

def hms(h,m,s):
    """ Tiempo en horas, decimal"""
    return h+m/60.0+s/3600.0

def EdT(B):
    """ Ecuacion del Tiempo [min]"""
    x = 229.2 * ( 7.5E-5 + 0.001868*cos(B) -0.032077*sin(B) - 0.014615*cos(2*B) - 0.04089*sin(2*B))
    return x

def dtiempo(E, Lst, Lloc, v):
    """Diferencia en [min]"""
    x = 4.0*(Lst-Lloc)+E-60.0*v
    return x

def omega(HMS, dt, tp):
    """ Omega en [rad]
       hms tiempo en decimales
       dt  diferencia de tiempo
       tp  tiempo solar 0/tiempo estandar 1
"""
    return d2r(15.0*(HMS-12.0 + tp*dt/60.0))

def omegaA(phi, delta):
    """
Omega de amanecer y anochecer [rad]
phi   - latitud [rad]
delta - declinacio [rad]
"""
    return acos( -tan(phi)*tan(delta) )

def B(N):
    """ B [rad]"""
    x = d2r( (N-1)*(360/365) )
    return x

def delta(N):
    """ Declinación Cooper [rad]"""
    x = d2r( (360/365)*(284+N) )
    return d2r(23.45*sin(x))

#delta_v = np.vectorize(delta)

def theta_z(phi, delta, omega):
    """  ángulo cenital en [rad]
phi   [rad]
delta [rad]
omega [rad]
"""
    a = cos(phi) * cos(delta)*cos(omega)
    b = sin(phi) * sin(delta)
    return acos(a+b)

def gamma_s(phi, delta, omega):
    """ángulo acimutal medido desde el sur [rad]
phi   [rad]
delta [rad]
omega [rad]
"""
    num = cos(delta)*sin(omega)
    den = sin(phi)*cos(delta)*cos(omega) - cos(phi)*sin(delta)
    ##print(num, den)
    return atan2(num,den)

def tzgs(h, m, s, D, M, Y, lat, Lloc, Lst, tp, v):
    """Regresa los valores de theta_z y gamma_s
    h:m:s : hora:minuto:segundo
    D/M/Y : dia/mes/año
    lat   : latitud en [rad]
    Lloc  : longitud local en [grad]
    Lst   : longitud estandar en [grad]
    tp    : tiempo solar 0/tiempo estandar 1
    v     : 0/1 horario de verano
"""
    N = doy(Y,M,D)
    HMS = hms(h,m,s)
    b = B(N)
    d = delta(N)
    E = EdT(b)
    dt = dtiempo(E, Lst, Lloc, v)
    w = omega(HMS, dt, tp)
    tz = theta_z(lat, d, w)
    gs = gamma_s(lat, d, w)
    return tz, gs
