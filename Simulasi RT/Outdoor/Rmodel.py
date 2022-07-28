from numpy import *
from reflection import reflection

class tworaymodel :
    def __init__ (self, f, zt, er, omega,xt,yt,xr,yr) :
        self.f = f
        self.zt = zt
        self.er = er
        self.omega = omega
        self.c = 3e8
        self.lambdac = self.c / f
        self.k = 2 * pi / self.lambdac
        
        self.xt = xt
        self.yt = yt
        self.xr = xr
        self.yr = yr
        self. zr = 1

        self.dtr = sqrt((self.xr - self.xt) ** 2 + (self.yr - self.yt) ** 2 + (self.zr - self.zt) ** 2)
        self.Edir = (exp(-1j * self.k * self.dtr)) / self.dtr
        
        self.angle = arctan(self.yr / (self.zt + self.zr))
        self.degree = self.angle * 180 / pi
        

    def vertical(self) :
        
        Rg = reflection(self.angle, self.er, self.omega, self.f).vertical()
        imagegroundzt = -self.zt
        dimagegroundtr = sqrt((self.xr - self.xt) ** 2 + (self.yr - self.yt) ** 2 + (self.zr - imagegroundzt) ** 2)
        
        Erefground = (Rg * exp(-1j * self.k * dimagegroundtr)) / dimagegroundtr
        Etotal = self.Edir + Erefground
        
        PL = 20 * log10((self.lambdac / (4 * pi)) * abs(Etotal))
        
        return PL
    
    def horizontal (self) :
        
        Rg = reflection(self.angle, self.er, self.omega, self.f).horizontal()
        imagegroundzt = -self.zt
        dimagegroundtr = sqrt((self.xr - self.xt) ** 2 + (self.yr - self.yt) ** 2 + (self.zr - imagegroundzt) ** 2)
        
        Erefground = (Rg * exp(-1j * self.k * dimagegroundtr)) / dimagegroundtr
        Etotal = self.Edir + Erefground
        
        PL = 20 * log10((self.lambdac / (4 * pi)) * abs(Etotal)/1.3)
        
        return PL
    
class fspl :
    def fspl (f, Gt = 0, Gr = 0) :
        c = 3e8
        d = linspace(50, 1e3, int(1e6))
        return 20 * log10 (d) + 20 * log10 (f) + 20 * log10 (4 * pi / c) - Gt - Gr

