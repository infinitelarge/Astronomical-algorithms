import numpy as np
import sunmoon.sunmoon as sm
def obliquity_of_ecliptic1(Jday):
    """
    Calculate the obliquity of the ecliptic.

    Parameters
    ----------
    epoch : float
        Epoch of coordinates in Julian years.

    Returns
    -------
    obliquity : float
        Obliquity of the ecliptic in radians.
    """
    O=sm.calc(Jday).O
    D=sm.calc(Jday).D
    M_=sm.calc(Jday).M
    Δε=(9.20*np.cos(O)-0.57*np.cos(2*D)-0.10*np.cos(2*M_)-0.09*np.cos(2*O))/3600 
    obliquity=Δε
    return obliquity
