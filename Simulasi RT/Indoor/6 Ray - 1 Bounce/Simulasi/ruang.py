f = 2.4

class pintu :
    def __init__ (self, awal, akhir) :
        self.awal = awal
        self.akhir = akhir
        self.Perm = 1.99
        self.Kond = 0.0047 * f**1.0718

class jendela :
    def __init__ (self, awal, akhir) :
        self.awal = awal
        self.akhir = akhir
        self.Perm = 6.27
        self.Kond = 0.0043 * f**1.1925
    
class lantai :
    def __init__(self):
        self.Perm = 5.31
        self.Kond = 0.0326 * f**0.8095

class dinding :
    def __init__ (self, awal, akhir) :
        self.awal = awal
        self.akhir = akhir
        self.Perm = 3.75
        self.Kond = 0.038

class plafon :
    def __init__ (self) :
        self.Perm = 1.5
        self.Kond = 0.0005 * f**1.1634
