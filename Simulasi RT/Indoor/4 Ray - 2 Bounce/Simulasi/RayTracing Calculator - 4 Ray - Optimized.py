from vec3 import vec3
from Tembok import *
from numpy import array,pi,cos, sin, zeros, log10, array, linspace
from perhitungan import *
from time import time

AP_O = [vec3(-.5,-.5,1),
        vec3(5.5,-.5,1),
        vec3(-.5,5.5,1),
        vec3(5.5,5.5,1)]
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

    thetha = array([(i) for i in linspace(pi/2,pi/2,1) for j in linspace(0,2*pi,360)])
    phi  = array([(j) for i in linspace(pi/2,pi/2,1) for j in linspace(0,2*pi,360)])
    x = sin (thetha) * cos (phi)
    y = sin (thetha) * sin (phi)
    z = cos (thetha)

    AP_D = vec3(x,y,z).norm()
    print (AP_D)
    Or = AP_O[n]
    Dr = AP_D
    print (Dr)
    Sr = AP_S

    bounce = 0
    path_ray = []
                        
    while bounce <= 2 :
        per_tembok = Berpotongan (Ruang, Or,Dr,Sr)
                
        origin = ray[0]

        try :
            PerpRx = perRx(Or,Dr,Sr,Rx)
            Tembok = Ruang[per_tembok]
            PerpTb = rRay(Or,Dr,Sr, Tembok)
                                        
            if PerpRx :               
                if PerpRx > PerpTb[2] :
                    break
                        
                Sr = Sr + PerpRx
                        
                if abs(temp - Sr) < 0.5 :
                    break
                        
                point = [origin, Rx[0]]
                path_ray.append(point)
                        
                temp = Sr
                        
                # Menghitung RSSI
                f = 2.4
                Ang = PerpTb[3]
                d = Sr
                        
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

            ray = rRay(Or,Dr,Sr, Tembok)
                
            point = [origin, ray[0]]
            path_ray.append(point)
                    
        except Exception as e:
            pass 
                
        bounce += 1

    c = 299792458
    lambdac = c / (2.4e9)
    RSS = 20 * log10((lambdac / (4 * pi)) * rssi)
    return round(-abs(RSS), 2)
    
def main () :
    t0 = time()
    
    file = open("RayTracing - 4 Ray.csv", "w")
    file.write("x, y, AP1, AP2, AP3, AP4\n")

    count = 0
    for i in range(0, 6) :
        for j in range (0,6) :
            x = j
            y = i
            z = 1
            
            Rx = [vec3(x,y,z), 0.05]

            AP1 = RayTrace (0, Rx)
            AP2 = RayTrace (1, Rx)
            AP3 = RayTrace (2, Rx)
            AP4 = RayTrace (3, Rx)
            
            print ("{},{},{},{},{},{}".format(x,y,AP1,AP2,AP3,AP4))

            file.write("{},{},{},{},{},{}\n".format(x,y,AP1,AP2,AP3,AP4))

            count += 1

            print ("Progress : {}%".format((count/36)*100))

    t1 = time() - t0

    file.write("Waktu : {}\n".format(t1))
    file.close()
    

main()
