def Jd(Y,M,D):
    if M<=2:
        Y=Y-1
        M=M+12
    A=int(Y/100)
    B=2-A+int(A/4)       
    JD = int(365.25*(Y+4716))+int(30.6001*(M+1))+D+B-1524.5
    MJD=JD-2400000.5
    return JD
def JdtoDate(JD):
    JD=JD+0.5
    Z=int(JD)
    F=JD-Z
    if Z<2299161:
        A=Z
    else:
        alpha=int((Z-1867216.25)/36524.25)
        A=Z+1+alpha-int(alpha/4)
    B=A+1524
    C=int((B-122.1)/365.25)
    D=int(365.25*C)
    E=int((B-D)/30.6001)
    day=B-D-int(30.6001*E)+F
    if E<14:
        month=E-1
    else:
        month=E-13
    if month>2:
        year=C-4716
    else:
        year=C-4715
    return year,month,day
#闰年判断
def leapyear(year):
    if year%400==0:
        return 1
    elif year%100==0:
        return 2
    elif year%4==0:
        return 1
    else:
        return 2
 
def dayofyear(Y,M,D):
    K=leapyear(Y)
    N=int(275*M/9)-K*int((M+9)/12)+D-30
    return N
