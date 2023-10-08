import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('temixcoEnero2019.csv', sep = ',', skiprows = 5)
df.columns = ["time", "Gb", "G", "Gd", "UV", "T", "phi", "v", "p"]
df.time = pd.to_datetime(df["time"], format = "%Y-%m-%d %H:%M:%S")
df.set_index(df['time'], inplace=True)

N = df.index.day.unique().values
dt = 10*60

H = []
for n in N:
    dfw = df[df.index.day == n]
    aux = dt * dfw.Gb.sum() / 1E6
    H.append(aux)

dfw = pd.DataFrame({'N':N, 'H': H})
dfw.to_csv('Enero2019.dat', index = False, sep ='\t')
plt.xlabel("Dia")
plt.ylabel("H [MJ/m2]")
plt.bar(dfw.N, dfw.H)
plt.show()

Hm = dfw["H"].mean()
print("Irradiacion promedio mensual = %.2f MJ/m2" % Hm)
