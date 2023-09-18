
def d2r(deg):
    """Convierte de grados a radianes"""
    from math import pi
    return deg*pi/180

def r2d(rad):
    """ Esta función convierte los radianes a grados  """
    from math import pi
    return rad*180/pi

def doy(y, m, d):
    """
    doy(y, m, d)
    y - año
    m - mes
    d - dia
    Regresa el día del año, 1-365
    """
    from datetime import datetime, date
    return date(y, m, d).timetuple().tm_yday

