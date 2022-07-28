from numpy import *
import time
import copy
import sys


class vec3():
    def __init__(self, x, y, z):
        (self.x, self.y, self.z) = (x, y, z)
    def __mul__(self, other):
        return vec3(self.x * other, self.y * other, self.z * other)
    def __rdiv__(self, other):
        return vec3(self.x / other, self.y / other, self.z / other)
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def __abs__(self):
        return self.dot(self)
    def norm(self):
        mag = sqrt(abs(self))
        return self * (1.0 / where(mag == 0, 1, mag))
    def components(self):
        return (self.x, self.y, self.z)
    def extract(self, cond):
        return vec3(extract(cond, self.x),
                    extract(cond, self.y),
                    extract(cond, self.z))
    def place(self, cond):
        r = vec3(zeros(cond.shape), zeros(cond.shape), zeros(cond.shape))
        place(r.x, cond, self.x)
        place(r.y, cond, self.y)
        place(r.z, cond, self.z)
        return r

def GaussJordan(a,n = 3) :
    x = zeros(n)

    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    for i in range(n):
        x[i] = a[i][n]/a[i][i]
        
    return x
    

#a = ([Dr.x, -D1.x, -D2.x, O.x-Or.x],
#         [Dr.y, -D1.y, -D2.y, O.y-Or.y],
#         [Dr.z, -D1.z, -D2.z, O.z-Or.z])
#a = np.array(a)

thetha = array([(i) for i in linspace(pi/2,pi/2,1) for j in linspace(0,2*pi,360)])
phi  = array([(j) for i in linspace(pi/2,pi/2,1) for j in linspace(0,2*pi,360)])
x = sin (thetha) * cos (phi)
y = sin (thetha) * sin (phi)
z = cos (thetha)

AP_D = vec3(x,y,z).norm()

#Or = AP_O[n]
#Dr = AP_D
#Sr = AP_S
