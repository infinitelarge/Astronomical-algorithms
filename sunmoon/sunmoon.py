import numpy as np
import coordinatetrans.coordinatetrans as ct

def calc(Jday):
    T = (Jday - 2451545) / 36525
    #平距角(日月对地心的角距离)
    D = np.radians(297.85036 + 445267.111480 * T - 0.0019142 * T ** 2 + T ** 3 / 189474)
    #太阳平近点角(太阳在黄道上的位置)
    M = np.radians(357.52772 + 35999.050340 * T - 0.0001603 * T ** 2 - T ** 3 / 300000)
    #月亮平近点角(月亮在黄道上的位置)
    M_ = np.radians(134.96298 + 477198.867398 * T + 0.0086972 * T ** 2 + T ** 3 / 56250)
    #月球纬度参数
    F = np.radians(93.27191 + 483202.017538 * T - 0.0036825 * T ** 2 + T ** 3 / 327270)
    #黄道与月球平轨道升交点黄经，从 Date 黄道平分点开始算起
    O = np.radians(125.04452 - 1934.136261 * T + 0.0020708 * T ** 2 + T ** 3 / 450000)
    return D,M,M_,F,O
#2
def sunrise(Jday,longitude,latitude):
    D,M,M_,F,O = calc(Jday)
    # 太阳视黄经
    l = ct.sun_look_longtitude(Jday)
    #太阳视赤经
    alpha = ct.ecliptic_to_equatorial(ct.sun_true_longitude(Jday),ct.sun_true_latitude(Jday),Jday)[0]
    #太阳视赤纬，公式来源：https://en.wikipedia.org/wiki/Sunrise_equation
    delta = ct.ecliptic_to_equatorial(ct.sun_true_longitude(Jday),ct.sun_true_latitude(Jday),Jday)[1]
    #太阳视地方时角，公式来源：https://en.wikipedia.org/wiki/Sunrise_equation
    H = np.arccos((np.sin(np.radians(-0.83)) - np.sin(np.radians(latitude)) * np.sin(delta)) / (np.cos(np.radians(latitude)) * np.cos(delta)))
    #太阳视地方时角
    H = np.degrees(H)
    #太阳视地方时角
    H = H / 15
    #太阳视地方时角
    H = H + alpha
    #太阳视地方时角
    H = H - np.radians(longitude)
    #太阳视地方时角
    H = H / (2 * np.pi)
    #太阳视地方时角
    H = H - np.floor(H)
    #太阳视地方时角
    H = H * 24
    #Equation of time,from
    E = 4 * np.degrees((np.sin(M) - 0.0145 - np.sin(M_) * np.cos(F) + np.sin(2 * M_) * 0.0004 - np.cos(2 * M_) * 0.0004) * np.pi / 180)
    H = H + E / 60
    return H
#sunset
def sunset(Jday,longitude,latitude):
    D,M,M_,F,O = calc(Jday)
    # 太阳视黄经
    l = ct.sun_look_longtitude(Jday)
    #太阳视赤经
    alpha = ct.ecliptic_to_equatorial(ct.sun_true_longitude(Jday),ct.sun_true_latitude(Jday),Jday)[0]
    #太阳视赤纬，公式来源：https://en.wikipedia.org/wiki/Sunrise_equation
    delta = ct.ecliptic_to_equatorial(ct.sun_true_longitude(Jday),ct.sun_true_latitude(Jday),Jday)[1]
    #太阳视地方时角，公式来源：https://en.wikipedia.org/wiki/Sunrise_equation
    H = np.arccos((np.sin(np.radians(-0.83)) - np.sin(np.radians(latitude)) * np.sin(delta)) / (np.cos(np.radians(latitude)) * np.cos(delta)))
    #太阳视地方时角
    H = np.degrees(H)
    #太阳视地方时角
    H = H / 15
    #太阳视地方时角
    H = H + alpha
    #太阳视地方时角
    H = H - np.radians(longitude)
    #太阳视地方时角
    H = H / (2 * np.pi)
    #太阳视地方时角
    H = H - np.floor(H)
    #太阳视地方时角，来自https://en.wikipedia.org/wiki/Sunrise_equation
    H = H * 24
    #Equation of time,来自https://en.wikipedia.org/wiki/Equation_of_time
    E = 4 * np.degrees((np.sin(M) - 0.0145 - np.sin(M_) * np.cos(F) + np.sin(2 * M_) * 0.0004 - np.cos(2 * M_) * 0.0004) * np.pi / 180)
    H = 24 - H
    H = H + E/ 60
     #日落时间
    return H
