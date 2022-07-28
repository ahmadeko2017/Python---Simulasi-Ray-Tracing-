from Rmodel import tworaymodel, fspl
import matplotlib.pyplot as plt

c = 3e8
f = 2.4e9
zt = 1
er =  30
omega = .15

print ('x,y,AP1,AP2,AP3,AP4')

for i in range (6) :
    for j in range (6) :
        # AP1
        xt = -.5
        yt = -.5
        xr = i
        yr = j
        AP1 = tworaymodel(f, zt, er, omega, xt,yt,xr,yr).horizontal()

        # AP2
        xt = 5.5
        yt = -.5
        AP2 = tworaymodel(f, zt, er, omega, xt,yt,xr,yr).horizontal()

        # AP3
        xt = -.5
        yt = 5.5
        AP3 = tworaymodel(f, zt, er, omega, xt,yt,xr,yr).horizontal()

        # AP4
        xt = 5.5
        yt = 5.5
        AP4 = tworaymodel(f, zt, er, omega, xt,yt,xr,yr).horizontal()
        
        print ('%i,%i,%.2f,%.2f,%.2f,%.2f'%(i,j,AP1,AP2,AP3,AP4))
