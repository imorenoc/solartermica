import pandas as pd

def G0(N):
    """Radiaci'on extraterrestre en funci'on del d'ia del a~no"""
    from math import cos, pi
    Gsc = 1367
    return Gsc * ( 1 + 0.033 * cos( 2*pi*N/365) )

def H(G, dt):
    """ Insolaci'on o Irradiancia promedio diaria H. G es un DataFrame que contiene las fecha en el indice
    G [W/m2]
    H [MJ/m2]
    Hasta un año, para que no se repitan los meses.
    >> Comprobado con el TMY de NSRDB, de SAM
"""
    G = G.dropna()
    meses = G.index.month.unique().values
    H = []
    F = []
    for mes in meses:
         dfmes = G[G.index.month == mes]
         dias = dfmes.index.day.unique().values
         for dia in dias:
             dfw = dfmes[dfmes.index.day == dia]            
             h = dt * dfw.sum() / 1E6
             H.append(h)
             f = str(dfw.index.year[0]) + '-' + str(mes) + '-' + str(dia)
             F.append(f)
    data = {'Fecha':F, 'H':H}
    df = pd.DataFrame(data)
    df.Fecha = pd.to_datetime(df.Fecha, format="%Y-%m-%d")
    df.set_index('Fecha', inplace = True)
    return df

def Kt(H,phi):
    """
    H [MW/m2]. DataFrame con fecha
    phi [rad]
Hasta un año, para que no se repitan los meses
"""
    from numpy import cos, arange
    from vsolar import omega, omegaA, theta_z, delta, doy,d2r

    Y = H.index.year[0]
    meses = H.index.month.unique().values
    F = []
    K = []
    for mes in meses:
        dfmes = H[H.index.month == mes]
        dias = dfmes.index.day.unique().values
        n = len(dias)
        for i in range(0, n):
            N = doy(Y, mes,dias[i])
            dw = 0.5
            dt = dw*(1/15) * 60 * 60
            dw = d2r(dw)
            ha = omegaA(phi,delta(N))
            intervalos = arange(-ha,ha+dw,dw)
            cosmean = 0
            for omega in intervalos:
                tz = theta_z(phi, delta(N), omega)
                costz = cos(tz)
                cosmean += costz
            H0i = G0(N) * cosmean * dt / 1E6 # MJ/m2
            ###print(H0i)
            Ki = dfmes.H[i]/H0i
            K.append(Ki)
            f = str(Y) + '-' + str(mes) + '-' + str(dias[i])
            F.append(f)
    data = {'Fecha':F, 'Kt': K}
    df = pd.DataFrame(data)
    df.Fecha = pd.to_datetime(df.Fecha, format = '%Y-%m-%d')
    df.set_index('Fecha', inplace =True)
    return df
