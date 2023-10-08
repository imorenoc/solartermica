import pandas as pd
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

df = pd.read_csv('data_2014.csv', sep = ',', skiprows = 5)
df.columns = ["time", "record", "Gb", "G", "Gd", "UV", "T", "phi", "v", "p"]
df.time = pd.to_datetime(df["time"], format = "%d/%m/%Y %H:%M")
df.set_index(df['time'], inplace=True)
df.dtypes
df["Gb"] = df["Gb"].apply(pd.to_numeric, errors='coerce')

dt = 10*60
mes = 3


dfmes = df[ df.index.month == mes  ]
dias  = dfmes.index.day.unique().values
H     = []
for dia in dias:
    dfw = dfmes[dfmes.index.day == dia]
    aux = dt * dfw.G.sum() / 1E6
    H.append(aux)

dfw = pd.DataFrame({'dia':dias, 'H': H})


# G0 [W/m2]
dfw["G0"] = 1367 * (1 + 0.033 * np.cos(dias * 2*np.pi/365))



from ps import d2r, doy, B, delta, EdT, dtiempo, hms, omega, theta_z
# Calculo de cos_thetaz
D  = 1          # D'ias
M  = mes          # Mes
Y  = 2014       # Año, es irrelevante para esta ecuación
tp = 0          # tiempo solar 0, est'andar 1
v  = 0          # horario de verano, si = 1, no=0
h  = 0          # hora
m  = 10          # minuto
s  = 0          # segundo
lat  = 18.8391  # latirud
Lloc = 99.2352 # longitud local
Lst  = 6*15    # longitud est'andar

lat = d2r(lat)
costheta = []
for dia in dias:
    N   = doy(Y,M,dia)
    b   = B(N)
    d   = delta(N)
    E   = EdT(b)
    Dt  = dtiempo(E, Lst, Lloc, v)
    theta = [ ]
    for hora in range(0, 24, 1):
        for minuto in range(0,60, 10):
            HMS = hms(hora,minuto,s)
            w = omega(HMS, Dt, tp)
            tz = theta_z(lat, d, w)
            theta.append(tz)
    x = np.cos(theta)
    x[x < 0] = 0
    aux = sum(x) * dt
    costheta.append(aux)

dfw["costhetaDt"] = costheta
dfw["H0"] = dfw["G0"] * costheta /1E6

dfw["Kt"]  = dfw["H"]/dfw["H0"]
pd.options.display.float_format = '{:10,.2f}'.format
print(dfw)

dfw.to_csv('Kmarzo.dat', index=False, sep='\t', float_format='%.3f')

# plt.xlabel("Día")
# plt.ylabel("Ídice de claridad $K_T$")
# plt.plot(dfw["dia"], dfw["Kt"], 'o:')
# #plt.savefig("./fig/enero2014Kt.png")
# plt.show()
