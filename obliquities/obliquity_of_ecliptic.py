import numpy as np

def obliquity_of_ecliptic(epoch):
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
    T = (epoch - 2000) / 100
    obliquity = np.radians(23.43929111 - 46.8150/3600 * T - 0.00059/3600 * T**2 + 0.001813/3600 * T**3)
    return obliquity
