import pandas as pd
import ps
import aux

def gsolar(phi, Lloc, Lst, tp, v, inicio,fin,ever='30min'):
    """
Genera un DataFrame con la fecha (inicio, fin, freq) que contiene los ángulos solares (alpha, thetaz, gammas). El data Frame que regresa esta en grados.
# inici = '2022-01-01'
# fin = '2022-12-31'
# freq = '30min'
# phi = d2r(45) [radianes]
# Lloc = Longitud local [grad]
# Lst  = Longitud estandar [grad]
# tp = 0  tiempo solar 0/ tiempo estandar 1
# v = 0   horario de verano 0/1

"""
    myindex = pd.date_range(inicio,fin, freq = ever)
    tz = []
    gs = []
    for i in myindex:
        [t, g] = ps.tzgs(i.hour, i.minute, i.second, i.day, i.month, i.year, phi, Lloc, Lst, tp, v)
        tz.append(t)
        gs.append(g)

    data = {'tz':tz, 'gs':gs}
    df = pd.DataFrame(data)
    df['alpha'] = aux.d2r(90) - df['tz']
    df.set_index(myindex, inplace=True)

    df['tz'] = aux.r2d(df['tz'])
    df['gs'] = aux.r2d(df['gs'])
    df['alpha'] = aux.r2d(df['alpha'])
    #df.to_csv('gammasa.dat', sep = '\t')
    return df
