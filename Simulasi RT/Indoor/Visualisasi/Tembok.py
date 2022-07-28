from vec3 import vec3
from numpy import array,pi,cos, sin, zeros, arccos

O = 1e-12

Dir_X = vec3(1,O,O).norm()
Dir_Y = vec3(O,1,O).norm()
Dir_Z = vec3(O,O,1).norm()

AOI1 = [vec3(O,O,O), Dir_X, Dir_Z, 5, 3]
AOI2 = [vec3(O,O,O), Dir_Y, Dir_Z, 5, 3]
AOI3 = [vec3(5,O,O), Dir_Y, Dir_Z, 5, 3]
AOI4 = [vec3(O,5,O), Dir_X, Dir_Z, 5, 3]

AOI = [AOI1, AOI2, AOI3, AOI4]

Tembok1 = vec3(-2.33,-5.736,O), Dir_X, Dir_Z, 1, 3, "t"
Tembok2 = vec3(-1.38,-5.736,O), Dir_Y, Dir_Z, 1.14, 3, "t"
Tembok3 = vec3(-1.38,-4.596,O), Dir_X, Dir_Z, .45, 3, "t"
Tembok4 = vec3(-.93,-5.076,O), Dir_Y, Dir_Z, .48, 3, "t"
Tembok5 = vec3(-.93,-5.076,O), Dir_X, Dir_Z, 7.13, 3, "t"
Tembok6 = vec3(6.20,-5.076,O), Dir_Y, Dir_Z, .46, 3, "t"
Tembok7 = vec3(6.20,-4.616,O), Dir_X, Dir_Z, .25, 3, "t"
Tembok8 = vec3(6.45,-4.616,O), Dir_Y, Dir_Z, 3.34, 3, "t"
Tembok9 = vec3(6.45,-1.276,O), Dir_X, Dir_Z, 1.21, 3, "t"
Tembok10 = vec3(7.66,-1.276,O), Dir_Y, Dir_Z, 3.31, 3, "t"
Tembok11 = vec3(6.23,2.034,O), Dir_X, Dir_Z, 1.43, 3, "t"
Tembok12 = vec3(6.23,2.034,O), Dir_Y, Dir_Z, .45, 3, "t"
Tembok13 = vec3(6.23,2.464,O), Dir_X, Dir_Z, 1.43, 3, "t"
Tembok14 = vec3(7.66,2.464,O), Dir_Y, Dir_Z, 6.9, 3, "t"
Tembok15 = vec3(-2.33,9.364,O), Dir_X, Dir_Z, 10, 3, "t"
Tembok16 = vec3(-2.33,-5.736,O), Dir_Y, Dir_Z, 15.14, 3, "t"
Lantai = vec3(-2.33,-5.736,O), Dir_X, Dir_Y, 10, 15.14, "t"
Atap = vec3(-2.33,-5.736,3), Dir_X, Dir_Y, 10, 15.14, "a"

Ruang = [Tembok1, Tembok2, Tembok3, Tembok4,
         Tembok5, Tembok6, Tembok7, Tembok8,
         Tembok9, Tembok10, Tembok11, Tembok12,
         Tembok13, Tembok14, Tembok15, Tembok16, Lantai, Atap]

polygon = [[-2.33,-5.736],
           [-1.38,-5.736],
           [-1.38,-4.596],
           [-.93,-4.596],
           [-.93,-5.076],
           [6.20,-5.076],
           [6.20,-4.616],
           [6.45,-4.616],
           [6.45,-1.276],
           [7.66,-1.276],
           [7.66,2.034],
           [6.23,2.034],
           [6.23,2.464],
           [7.66,2.464],
           [7.66,9.364],
           [-2.33,9.364]]

def Berpotongan (Ruang, ray) :
    no_tembok = 0
    data_Perpotongan = {}
        
    for Tembok in Ruang :
        Perpotongan = perTembok(ray, Tembok)
        if Perpotongan :
            rays = rRay(ray, Tembok)
            data_Perpotongan[rays[2]] = no_tembok
        no_tembok += 1
            
    if data_Perpotongan == {} :
        return False

    else : 
        jarak_min = min(data_Perpotongan)
        per_tembok = data_Perpotongan[jarak_min]

        return per_tembok
    
def isometrik (x,y,z) :
    u = (x - y) * cos (30 * pi/180)
    v = (x + y) * cos (60 * pi/180) + z
    return u,v

def perRx(Ray, Rx, zero = 1e-10) :

    Or = Ray[0]
    Dr = Ray[1]

    Ol = Rx[0]
    r = Rx[1]
    
    Orl = Or - Ol
    
    a = 1
    b = 2 * Dr.dot(Orl)
    c = Orl.dot(Orl) - r * r

    Disc = b * b - 4 * c

    if Disc >= zero :
        s = (-b - Disc**.5)/2
        if s > 0 :
            return s
    return False

def perTembok(Ray, Tembok, zero = 1e-10) :
    Or = Ray[0]
    Dr = Ray[1]

    O = Tembok[0]
    D1 = Tembok[1]
    D2 = Tembok[2]
    
    t1min = zero
    t1max = Tembok[3]
    
    t2min = zero
    t2max = Tembok[4]
    
    a = -Dr.x/D1.x-((D2.x/D1.x)*(Dr.x/D1.x-Dr.y/D1.y)/(-D2.x/D1.x+D2.y/D1.y))
    b = (O.x-Or.x)/D1.x -((D2.x/D1.x)*(-(O.x-Or.x)/D1.x+(O.y-Or.y)/D1.y)/(-D2.x/D1.x+D2.y/D1.y))
    c = (Dr.x/D1.x-Dr.y/D1.y)/(-D2.x/D1.x+D2.y/D1.y)
    d = (-(O.x-Or.x)/D1.x+(O.y-Or.y)/D1.y)/(-D2.x/D1.x+D2.y/D1.y)
    e = (Dr.x/D1.x-Dr.z/D1.z)/(-D2.x/D1.x+D2.z/D1.z)
    f = (-(O.x-Or.x)/D1.x+(O.z-Or.z)/D1.z)/(-D2.x/D1.x+D2.z/D1.z)

    t1 = -(b-a*((-d+f)/(-c+e)))
    t2 = -(d-c*(-d+f)/(-c+e))
    tr = -((-d+f)/(-c+e))
    
    x = Or.x + Dr.x*tr
    y = Or.y + Dr.y*tr
    z = Or.z + Dr.z*tr

    if tr >= zero :
        if t1min <= t1 <= t1max :
            if t2min <= t2 <= t2max :
                return vec3(x,y,z),[t1, t2, tr]
        else :
            False
    else :
        False

def normTembok(Tembok, t1, t2, n = 2) :

    D1 = Tembok[1]
    D2 = Tembok[2]
    
    a = D1*t1
    b = D2*t2
    
    x = a.z/a.x - (a.y/a.x)*(-a.z/a.x+b.z/b.x)/(-a.y/a.x+b.y/b.x)
    y = (-a.z/a.x+b.z/b.x)/(-a.y/a.x+b.y/b.x)
    z = 1

    r = (x**2 * y**2 * z**2)**.5
    
    x = round(x/r, n)
    y = round(y/r, n)
    z = round(z/r, n)

    return vec3(x, y, z).norm()

# mencari reflection ray
def rRay(Ray, Tembok) :
    O = perTembok(Ray, Tembok)
    Dr = Ray[1]
    n = normTembok(Tembok, O[1][0], O[1][1])
    rDr = Dr + n*(-2*Dr.dot(n))
    Ref = Ray[0] + Ray[1]*O[1][2]
    s = Ray[2] + ((Ray[0].x - O[0].x)**2+(Ray[0].y - O[0].y)**2+(Ray[0].z - O[0].z)**2)**.5
    ang = arccos((Dr.norm()).dot(n))
    
    return [O[0],rDr.norm(),s, ang]
