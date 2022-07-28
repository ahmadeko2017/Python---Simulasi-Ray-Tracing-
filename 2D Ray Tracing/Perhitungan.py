from ruang import *

def er(perm, kond, f):
    eo = 8.854e-12
    return (perm - 1j * kond / (2 * pi * f)) / eo

def Ed(Tx, Rx, f):
    c = 299792458 # m/s
    lamda = c / f
    k = 2 * pi / lamda
    d = abs(Tx - Rx)
    return (exp(-1j * k * d) / d)

def RPar(Ang, er):
    try :
        R = (er * cos(Ang) - (er - sin(Ang) ** 2) ** .5) / (er * cos(Ang) + (er - sin(Ang) ** 2) ** .5)
        return R
    except :
        return 0
    
def RPer(Ang, er):
    try :
        R = (cos(Ang) - (er - sin(Ang) ** 2) ** .5) / (cos(Ang) + (er - sin(Ang) ** 2) ** .5)
        return R
    except :
        return 0
