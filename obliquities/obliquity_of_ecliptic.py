import numpy as np
import sunmoon.sunmoon as sm
import coordinatetrans.coordinatetrans as ct
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
    O=ct.sun_true_longitude(Jday)
    D=sm.calc(Jday).D
    M_=sm.calc(Jday).M_
    Δε=(9.20*np.cos(O)-0.57*np.cos(2*D)-0.10*np.cos(2*M_)-0.09*np.cos(2*O))/3600 
    obliquity=Δε
    ecliptic+=Δε
    return obliquity
def ecliptic(Jday):
    #平黄赤交角
    ε0=(84381.448-46.8150*Jday-0.00059*Jday**2+0.001813*Jday**3)*3600
    ε0+=obliquity_of_ecliptic1(Jday)
    return ε0
