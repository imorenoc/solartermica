import pandas as pd

df = pd.read_csv("DNI.csv")
df.columns = ["time", "G", "Gb"]
#print(df)
df.loc[df.Gb <0, 'Gb'] = 0

dt = 60*60
H = dt * df.Gb.sum() #J/m2
print("Insolacion = %.2f J/m2" % H)
print("Insolacion = %.2f MJ/m2" % (H/1E6))
print("Insolacion = %.2f kWh/m2" % ((H/3600)/1000) )
