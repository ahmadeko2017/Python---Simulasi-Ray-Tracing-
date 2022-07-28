from numpy import sin, cos, pi, sqrt

class reflection :
    def __init__(self, angle, er, omega, f) :
        self.angle = angle
        self.er = er
        self.omega = omega
        self.f = f
        self.e0 = 8.854e-12
        self.ep = self.er - 1j*omega / (2 * pi * f * self.e0)
        
    def vertical(self) :
        return (self.ep * cos(self.angle) - sqrt(self.ep - (sin(self.angle))**2)) / (self.ep * cos(self.angle) + sqrt(self.ep - (sin(self.angle))**2))
    
    def horizontal(self) :
        return (cos(self.angle) - sqrt(self.ep - (sin(self.angle))**2)) / (cos(self.angle) + sqrt(self.ep - (sin(self.angle))**2))
    
