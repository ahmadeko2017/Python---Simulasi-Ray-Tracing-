from vec3 import vec3
from Tembok import *
from numpy import array,pi,cos, sin, zeros
from graphics import *
from perhitungan import *

Rasio = 22 / 18
Lebar_Jend = 600
Panjang_Jend = Lebar_Jend * Rasio

win = GraphWin("Visualisasi X Y", Panjang_Jend, Lebar_Jend)
win.setCoords(-11.5,-6,11,13)
win.setBackground("white")

reset = [[-10.3, 3.45],
         [2.9, -4.25],
         [10.32, 0.28],
         [10.26, 5.55],
         [-1.63, 12.33],
         [-10.3, 7]]

AP_O = [vec3(-.5,-.5,1),
        vec3(5.5,-.5,1),
        vec3(-.5,5.5,1),
        vec3(5.5,5.5,1)]
AP_S = 0

x = 5
y = 1
AP_D = vec3(x,y,0).norm()

ray = [AP_O[0], AP_D,AP_S] 

x = 3
y = 3
STA_O = vec3(x,y,.05)

Rx = [STA_O, 1]

def lineAP (line, win) :
    x = line.x
    y = line.y
    z = line.z

    iso0 = isometrik (x,y,z)
    iso1 = isometrik (x,y,0)
    Line(Point(iso0[0], iso0[1]), Point(iso1[0], iso1[1])).draw(win)
    
def drawLine (path_ray, color, win) :
    for linee in path_ray :
        x1 = linee[0].x
        y1 = linee[0].y
        z1 = linee[0].z
        x2 = linee[1].x
        y2 = linee[1].y
        z2 = linee[1].z

        A = isometrik(x1,y1,z1)
        B = isometrik(x2,y2,z2)
        line = Line(Point(A[0],A[1]), Point(B[0], B[1]))
        line.setFill(color)
        line.draw(win)
        
def entry (x,y,win) :
    entry = Entry(Point(x,y), 5)
    entry.setText("0")
    entry.draw(win)
    return entry

def text (x, y, txt, win) :
    text = Text(Point(x,y), txt)
    text.draw(win)

def textAP (pos, AP, win) :
    x = pos.x
    y = pos.y
    z = 0
    iso = isometrik(x,y,z)
    Text(Point(iso[0],iso[1]),AP).draw(win)

def polyRUANG(polygon,win) :
    pol1 = []
    pol2 = []
    for i in polygon :
        iso1 = isometrik(i[0],i[1],0)
        pol1.append(Point(iso1[0], iso1[1]))
        iso2 = isometrik(i[0],i[1],3)
        pol2.append(Point(iso2[0], iso2[1]))
        Line(Point(iso1[0], iso1[1]), Point(iso2[0], iso2[1])).draw(win)
    poly1 = Polygon(pol1)
    poly2 = Polygon(pol2)
    poly1.draw(win)
    poly2.draw(win)

def poly(polygon, win) :
    pol = []
    for i in polygon :
        pol.append(Point(i[0], i[1]))
    poly = Polygon(pol)
    poly.setFill("white")
    poly.setOutline("white")
    poly.draw(win)

def circ(circle, win) :
    x = circle.x
    y = circle.y
    z = circle.z
    iso = isometrik(x,y,z)
    
    Circle(Point(iso[0],iso[1]),.1).draw(win)

def RayTrace (n, color) :
    #for teta in range (1,180)
    for deg in range(1,720,1) :    
        deg = (deg/180 * pi)/2
        x = cos (deg)
        y = sin (deg)

        AP_D = vec3(x,y,0).norm()

        ray = [AP_O[n], AP_D,AP_S]

        bounce = 0
        path_ray = []
        while bounce <= 1 :
            per_tembok = Berpotongan (Ruang, ray)
            
            origin = ray[0]
            
            PerpRx = perRx(ray,Rx)
            Tembok = Ruang[per_tembok]
            PerpTb = rRay(ray, Tembok)
            
            if PerpRx :
                if PerpRx > PerpTb[2] :
                    break
                ray[2] = ray[2] + PerpRx
                point = [origin, Rx[0]]
                path_ray.append(point)
                drawLine (path_ray, color, win)
                break
            
            ray = rRay(ray, Tembok)
            
            point = [origin, ray[0]]
            path_ray.append(point)   
            
            bounce += 1
    
rect = Rectangle(Point(-10,-3), Point(-8,-4))
rect.setFill("green")
rect.draw(win)

Pos_X = entry(-8,0, win)
Pos_Y = entry(-8,-1, win)
Pos_Z = entry(-8,-2, win)
txtX = text (-10, 0, "STA X", win)
txtY = text (-10, -1, "STA Y", win)
txtZ = text (-10, -2, "STA Z", win)

polyRUANG(polygon,win)

def main (Rx) :
    
    polyRUANG(polygon,win)
    
    RayTrace (0, "red")
    RayTrace (1, "green")
    RayTrace (2, "blue")
    RayTrace (3, "orange")

    AP = 1
    for AP_o in AP_O :
        circ(AP_o, win)
        lineAP(AP_o, win)
        textAP(AP_o, "AP {}".format(AP), win)
        AP += 1
        
    circ(Rx[0], win)
    lineAP(Rx[0], win)
    textAP(Rx[0], "STA", win)
    
while True :
    mouse = win.getMouse()
    if -10 < mouse.getX() < -8 :
        if -3 > mouse.getY() > -4 :
            poly(reset, win)
            Rx = [vec3(float(Pos_X.getText()),float(Pos_Y.getText()), float(Pos_Z.getText())), 0.1]
            main(Rx)
