import pandas as pd

file='21.8061_-102.2957_21.8053_-102.295_psm3-tmy_60_tmy.csv'

df = pd.read_csv(file, header = None, names = ["Year", "Month", "Day", "Hour", "Minute", "DNI", "DHI", "GHI", "Dew Point", "Temperature", "Pressure", "Wind Direction", "Wind Speed", "Surface Albedo"], sep=",", skiprows = 3, parse_dates={'fecha' : ['Year', 'Month', 'Day', 'Hour', 'Minute']})

df.fecha = pd.to_datetime(df.fecha, format ='%Y %m %d %H %M')
df.set_index('fecha', inplace=True)
print(df.head())
