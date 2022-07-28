import time

f = 2.4

t0 = time.time()

Ruang = [["pintu", 1.99, 0.0047 * f**1.0718],
         ["jendela", 6.27, 0.0043 * f**1.1925],
         ["lantai", 6.27, 0.0326 * f**0.8095],
         ["dinding", 5.31, 0.0326 * f**0.8095],
         ["plafon", 1.5,0.0005 * f**1.1634 ]]

def getPK (Ruang) :
    for i in Ruang :
        if i[0] == "plafon" :
            perm = i[1]
            kond = i[2]
    return perm, kond
