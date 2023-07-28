def greenwich_sidereal(JD):
    T=(JD-2451545.0)/36525.0
    theta0=280.46061837+360.98564736629*(JD-2451545.0)+0.000387933*T*T-T*T*T/38710000.0
    theta0=theta0%360
    return theta0
