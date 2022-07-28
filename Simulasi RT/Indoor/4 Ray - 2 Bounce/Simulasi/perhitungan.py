from ruang import *
from numpy import sin, cos, pi, exp

def er(perm, kond, f = 2.4):
    eo = 8.854e-12
    return (perm - 1j * kond / (2 * pi * f)) / eo

def Ed(d, f = 2.4e9):
    c = 299792458 # m/s
    lamda = c / f
    k = 2 * pi / lamda
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

