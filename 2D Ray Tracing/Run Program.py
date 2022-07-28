from vec3 import vec3
from Tembok import *
from numpy import array,pi,cos, sin, zeros
from graphics import *

Rasio = 11.3/16.5
Lebar_Jend = 600
Panjang_Jend = Lebar_Jend * Rasio

win = GraphWin("Visualisasi X Y", Panjang_Jend, Lebar_Jend)
win.setCoords(-3,-6.5,8.3,10)
win.setBackground("white")

polygon = [Point(-2.33,-5.736),
           Point(-1.38,-5.736),
           Point(-1.38,-4.596),
           Point(-.93,-4.596),
           Point(-.93,-5.076),
           Point(6.20,-5.076),
           Point(6.20,-4.616),
           Point(6.45,-4.616),
           Point(6.45,-1.276),
           Point(7.66,-1.276),
           Point(7.66,2.034),
           Point(6.23,2.034),
           Point(6.23,2.464),
           Point(7.66,2.464),
           Point(7.66,9.364),
           Point(-2.33,9.364)]
           

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

def drawLine (path_ray, color, win) :
    for linee in path_ray :
        line = Line(linee[0],linee[1])
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

def poly(polygon,win) :
    poly = Polygon(polygon)
    poly.setFill("white")
    poly.draw(win)

def RayTrace (n, color) :
    temp = 0
    for deg in range(0,720,1) :
        deg = deg/180 * pi/2
        x = cos (deg)
        y = sin (deg)

        AP_D = vec3(x,y,0).norm()

        ray = [AP_O[n], AP_D,AP_S]

        bounce = 0
        path_ray = []
        while bounce <= 2 :

            per_tembok = Berpotongan (Ruang, ray)
            
            x_origin = ray[0].x
            y_origin = ray[0].y
            
            PerpRx = perRx(ray,Rx)
            Tembok = Ruang[per_tembok]
            PerpTb = sRay(ray, Tembok)
            
            if PerpRx :
                if PerpRx > PerpTb :
                    break
                
                ray[2] = ray[2] + PerpRx

                if abs(temp - ray[2]) < .5 :
                    break
                
                point = [Point(x_origin,y_origin), Point(Rx[0].x, Rx[0].y)]
                path_ray.append(point)
                drawLine (path_ray, color, win)
                temp = ray[2]
                break
            
            ray = rRay(ray, Tembok)
            
            point = [Point(x_origin,y_origin), Point(ray[0].x, ray[0].y)]
            path_ray.append(point)   
            
            bounce += 1
    
rect = Rectangle(Point(5.5,-5.45), Point(6.4,-6.1))
rect.setFill("green")
rect.draw(win)

Pos_X = entry(1.5,-5.75, win)
Pos_Y = entry(4.5,-5.75, win)
txtX = text (0, -5.75, "STA X", win)
txtB = text (3, -5.75, "STA Y", win)

poly(polygon,win)

def main (Rx) :
    poly(polygon,win)
    
    AP = 1
    for AP_o in AP_O :
        Circle(Point(Rx[0].x,Rx[0].y),.1).draw(win)
        Text(Point(AP_o.x,AP_o.y-.5),"AP {}".format(AP)).draw(win)
        AP += 1

    for batas in AOI :
        Line(Point(batas[0].x,batas[0].y),Point(batas[0].x+batas[1].x*batas[3],batas[0].y+batas[1].y*batas[3])).draw(win)

    RayTrace (0, "red")
    RayTrace (1, "green")
    RayTrace (2, "blue")
    RayTrace (3, "orange")
    
while True :
    mouse = win.getMouse()
    if 5.5 < mouse.getX() < 6.4 :
        if -5.45 > mouse.getY() > -6.1 :
            Rx = [vec3(float(Pos_X.getText()),float(Pos_Y.getText()), 1), 0.1]
            main(Rx)
    else :
        Rx = [vec3(float(mouse.getX()),float(mouse.getY()), 1), 0.1]
        main(Rx)
