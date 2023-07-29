#赤道坐标转到黄道坐标
import numpy as np
import obliquities.obliquity_of_ecliptic as gst
import sunmoon.sunmoon as sm
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
#计算本地地平坐标
def equatorial_to_horizontal(ra, dec, lat, lon, jd, lst):
    """
    Convert equatorial coordinates to horizontal coordinates.

    Parameters
    ----------
    ra : float
        Right ascension in degrees.
    dec : float
        Declination in degrees.
    lat : float
        Latitude of observer in degrees.
    lon : float
        Longitude of observer in degrees.
    jd : float
        Julian date.
    lst : float
        Local sidereal time in degrees.

    Returns
    -------
    az : float
        Azimuth in degrees.
    alt : float
        Altitude in degrees.
    """
    ra = np.radians(ra)
    dec = np.radians(dec)
    lat = np.radians(lat)
    lon = np.radians(lon)
    lst = np.radians(lst)
    ha = lst - ra
    alt = np.arcsin(np.sin(dec) * np.sin(lat) + np.cos(dec) * np.cos(lat) * np.cos(ha))
    az = np.arctan2(np.sin(ha), np.cos(ha) * np.sin(lat) - np.tan(dec) * np.cos(lat))
    az = np.degrees(az)
    alt = np.degrees(alt)
    return az, alt
#地平坐标转到赤道坐标
def horizontal_to_equatorial(az, alt, lat, lon, jd, lst):
    """
    Convert horizontal coordinates to equatorial coordinates.

    Parameters
    ----------
    az : float
        Azimuth in degrees.
    alt : float
        Altitude in degrees.
    lat : float
        Latitude of observer in degrees.
    lon : float
        Longitude of observer in degrees.
    jd : float
        Julian date.
    lst : float
        Local sidereal time in degrees.

    Returns
    -------
    ra : float
        Right ascension in degrees.
    dec : float
        Declination in degrees.
    """
    az = np.radians(az)
    alt = np.radians(alt)
    lat = np.radians(lat)
    lon = np.radians(lon)
    lst = np.radians(lst)
    ha = np.arctan2(np.sin(az), np.cos(az) * np.sin(lat) + np.tan(alt) * np.cos(lat))
    dec = np.arcsin(np.sin(lat) * np.sin(alt) - np.cos(lat) * np.cos(alt) * np.cos(az))
    ra = lst - ha
    ra = np.degrees(ra)
    dec = np.degrees(dec)
    return ra, dec
#从 B1950.0 标准分点赤道坐标转到银道坐标
def equatorial_to_galactic(ra, dec):
    """
    Convert equatorial coordinates to galactic coordinates.

    Parameters
    ----------
    ra : float
        Right ascension in degrees.
    dec : float
        Declination in degrees.

    Returns
    -------
    lon : float
        Galactic longitude in degrees.
    lat : float
        Galactic latitude in degrees.
    """
    ra = np.radians(ra)
    dec = np.radians(dec)
    l = np.radians(33)
    sinb = np.sin(dec) * np.sin(l) + np.cos(dec) * np.cos(l) * np.sin(ra - np.radians(282.25))
    b = np.arcsin(sinb)
    cosl = (np.sin(dec) - np.sin(b) * np.sin(l)) / (np.cos(b) * np.cos(l))
    l = np.arccos(cosl)
    lon = np.degrees(l) + 33
    lat = np.degrees(b)
    return lon, lat
#从银道坐标转到 B1950.0 标准分点赤道坐标
def galactic_to_equatorial(lon, lat):
    """
    Convert galactic coordinates to equatorial coordinates.

    Parameters
    ----------
    lon : float
        Galactic longitude in degrees.
    lat : float
        Galactic latitude in degrees.

    Returns
    -------
    ra : float
        Right ascension in degrees.
    dec : float
        Declination in degrees.
    """
    lon = np.radians(lon)
    lat = np.radians(lat)
    l = np.radians(33)
    sindec = np.sin(lat) * np.sin(l) + np.cos(lat) * np.cos(l) * np.sin(lon - np.radians(33))
    dec = np.arcsin(sindec)
    cosra = (np.sin(lat) - np.sin(dec) * np.sin(l)) / (np.cos(dec) * np.cos(l))
    ra = np.arccos(cosra) + np.radians(282.25)
    ra = np.degrees(ra)
    dec = np.degrees(dec)
    return ra, dec
#太阳真黄经
def sun_true_longitude(jd):
    #太阳中间方程
    t = (jd - 2451545.0) / 36525
    #太阳平黄经
    l0 = 280.46646 + 36000.76983 * t + 0.0003032 * t ** 2
    #太阳平近点角
    m = sm.calc(jd).M
    #太阳中心方程
    c = (1.914602 - 0.004817 * t - 0.000014 * t ** 2) * np.sin(np.radians(m)) + (0.019993 - 0.000101 * t) * np.sin(np.radians(2 * m)) + 0.000289 * np.sin(np.radians(3 * m))
    #太阳真黄经
    l = l0 + c
    return l
def sun_look_longtitude(Jday):
    D, M, M_, F, O = sm.calc(Jday)
    L = sun_true_longitude(Jday)
    l = L + np.radians(1.9146) * np.sin(M) + np.radians(0.019993) * np.sin(2 * M)
    return l
#太阳赤经
def sun_ra(jd):
    l = np.radians(sun_true_longitude(jd))
    e = np.radians(23.439291)
    ra = np.arctan2(np.sin(l) * np.cos(e), np.cos(l))
    ra = np.degrees(ra)
    return ra