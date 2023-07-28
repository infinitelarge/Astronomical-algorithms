#赤道坐标转到黄道坐标
import numpy as np
import obliquities.obliquity_of_ecliptic as gst
# Don't care about this err, you can still use it.
def equatorial_to_ecliptic(ra, dec, epoch):
    """
    Convert equatorial coordinates to ecliptic coordinates.

    Parameters
    ----------
    ra : float
        Right ascension in degrees.
    dec : float
        Declination in degrees.
    epoch : float
        Epoch of coordinates in Julian years.

    Returns
    -------
    lon : float
        Ecliptic longitude in degrees.
    lat : float
        Ecliptic latitude in degrees.
    """
    ra = np.radians(ra)
    dec = np.radians(dec)
    obliquity = gst.obliquity_of_ecliptic(epoch)
    lon = np.arctan2(np.sin(ra) * np.cos(obliquity) + np.tan(dec) * np.sin(obliquity), np.cos(ra))
    lat = np.arcsin(np.sin(dec) * np.cos(obliquity) - np.cos(dec) * np.sin(obliquity) * np.sin(ra))
    lon = np.degrees(lon)
    lat = np.degrees(lat)
    return lon, lat
#黄道坐标转到赤道坐标
def ecliptic_to_equatorial(lon, lat, epoch):
    """
    Convert ecliptic coordinates to equatorial coordinates.

    Parameters
    ----------
    lon : float
        Ecliptic longitude in degrees.
    lat : float
        Ecliptic latitude in degrees.
    epoch : float
        Epoch of coordinates in Julian years.

    Returns
    -------
    ra : float
        Right ascension in degrees.
    dec : float
        Declination in degrees.
    """
    lon = np.radians(lon)
    lat = np.radians(lat)
    obliquity = gst.obliquity_of_ecliptic(epoch)
    ra = np.arctan2(np.sin(lon) * np.cos(obliquity) - np.tan(lat) * np.sin(obliquity), np.cos(lon))
    dec = np.arcsin(np.sin(lat) * np.cos(obliquity) + np.cos(lat) * np.sin(obliquity) * np.sin(lon))
    ra = np.degrees(ra)
    dec = np.degrees(dec)
    return ra, dec
