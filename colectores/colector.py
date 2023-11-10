import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# °C   °C      °C      W/m2    kg/min
df = pd.read_csv("colector.csv", sep = ',', skiprows = 3, names = ["Tin", "Tout", "Tamb", "G", "m"])


# Calculo de la eficiencia, eta
#
Cp = 4181.3 # J/(kgK)
Ac = 0.17   # m2
Q = (df.m/60.)*Cp * (df.Tout- df.Tin)
d = Ac*df.G
y = Q/d

# Calculo del parámetro a, b
x = (df.Tin-df.Tamb)/df.G

plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), 'r')
plt.xlabel("$\dfrac{(T_{in}-T_{amb})}{G}$")
plt.ylabel("$\eta$")
plt.text(0.020, 0.65, "$y = %.2f x + %0.2f$" % (p[1], p[0]) )
plt.show()
