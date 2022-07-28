FP = open ("FingerPrint.csv","r")
FP_data = []
for i in FP :
    temp = i[:-1].split(",")
    FP_data.append(temp)
FP.close()

DT = open ("DataTest.csv","r")
DT_data = []
for i in DT :
    temp = i[:-1].split(",")
    DT_data.append(temp)
DT.close()

PR = open ("Predic.csv","w")
PR.write("x,y,x_predic,y_predic\n")


def Euclidean (DT, FP) :
    return ((DT[0] - FP[0]) ** 2 + (DT[1] - FP[1]) ** 2 + (DT[2] - FP[2]) ** 2 + (DT[3] - FP[3]) ** 2) ** .5
    

for Baris_DT in range (1,45) :
    DT = []
    for Kolom_DT in range (2,6) :
        DT.append(float(DT_data [Baris_DT][Kolom_DT]))
    E = []
    for Baris_FP in range (1,37) :
        FP = []
        for Kolom_FP in range (2,6) :
            FP.append(float(FP_data [Baris_FP][Kolom_FP]))
        E.append([Euclidean(DT, FP), FP_data [Baris_FP][0], FP_data [Baris_FP][1]])
    E_min = min(E)
    x = float(DT_data [Baris_DT][0])
    y = float(DT_data [Baris_DT][1])
    x_predic = float(E_min[1])
    y_predic = float(E_min[2])
    
    PR.write("{},{},{},{},{}\n".format(x, y, x_predic, y_predic, ((x-x_predic) ** 2 + (y-y_predic) ** 2) ** .5))

PR.close()
    

