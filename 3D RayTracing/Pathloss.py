from vec3 import vec3
from Tembok import *
from numpy import array,pi,cos, sin, zeros, log10
from perhitungan import *
from time import time

AP_O = [vec3(2.5,0,1)]
AP_S = 0

x = 5
y = 1
AP_D = vec3(x,y,0).norm()

ray = [AP_O[0], AP_D,AP_S] 

def RSSI (R, perm, kond, d, Ang, f) :
    ER = er (perm, kond, f)
    ED = Ed (d, f*1e9)
    Par = RPar(Ang, ER)
    Per = RPer(Ang, ER)
    EDPar = ED * Par
    EDPer = ED * Per

    if R == "p" :
        return EDPar
    if R == "s" :
        return EDPer
    else :
        return ED
    
def RayTrace (n, Rx) :
    temp = 0
    rssi = 0
    for teta in range (90,91) :
        teta = (teta/180 * pi)
        
        for deg in range(0,720) :
            deg = (deg/180 * pi)/2
            x = sin (teta) * cos (deg)
            y = sin (teta) * sin (deg)
            z = cos (teta)

            AP_D = vec3(x,y,z).norm()

            ray = [AP_O[n], AP_D,AP_S]

            bounce = 0
            path_ray = []
                        
            while bounce <= 1 :
                per_tembok = Berpotongan (Ruang, ray)
                
                origin = ray[0]

                try :
                    PerpRx = perRx(ray,Rx)
                    Tembok = Ruang[per_tembok]
                    PerpTb = rRay(ray, Tembok)
                                        
                    if PerpRx :               
                        if PerpRx > PerpTb[2] :
                            break
                        
                        ray[2] = ray[2] + PerpRx
                        
                        if abs(temp - ray[2]) < 0.5 :
                            break
                        
                        point = [origin, Rx[0]]
                        path_ray.append(point)
                        
                        temp = ray[2]
                        
                        # Menghitung RSSI
                        f = 2.4
                        Ang = PerpTb[3]
                        d = ray[2]
                        
                        if Tembok[5] == "t" :
                            perm = 3.75
                            kond = 0.038
                            R = "p"

                        if Tembok[5] == "a" :
                            perm = 1.5
                            kond = 0.0005 * f**1.1634
                            R = "s"
                            
                        rss = RSSI (R, perm, kond, d, Ang, f)

                        c = 299792458
                        lambdac = c / (2.4e9)
                        rssi += rss

                        break
                    
                    if ray == None :
                        break

                    ray = rRay(ray, Tembok)
                
                    point = [origin, ray[0]]
                    path_ray.append(point)
                    
                except Exception as e:
                    pass 
                
                bounce += 1

    c = 299792458
    lambdac = c / (2.4e9)
    RSS = 20 * log10((lambdac / (4 * pi)) * rssi/1.5)
    return round(RSS.real, 2)

def main () :
    t0 = time()
    
    file = open("RayTracing.csv", "w")
    file.write("x, y, AP1\n")

    count = 0
    for i in range(1,13) :
        x = 2.5
        y = i/2
        z = 1
            
        Rx = [vec3(x,y,z), 0.05]

        AP1 = RayTrace (0, Rx)
            
        print ("{},{},{}".format(x,y,AP1))

        file.write("{},{},{}\n".format(x,y,AP1))

        count += 1

    t1 = time() - t0

    file.write("Waktu : {}\n".format(t1))
    file.close()
    

main()
