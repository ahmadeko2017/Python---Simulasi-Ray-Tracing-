from firebase import firebase
from datetime import datetime

def exportCSV() :
    global firebase
    firebase = firebase.FirebaseApplication("https://getrssi-default-rtdb.asia-southeast1.firebasedatabase.app/", None)
    CountData = firebase.get("/CountData", None)

    temp = ""
    for i in range(CountData) :
        try :
            temp += "{},".format(i+1) + firebase.get("/logData", "{}".format(i+1)) + "\n"
        except :
            pass
    now = datetime.now()
    current_time = now.strftime("Date[%d%m%Y] Time[%H%M%S]")
            
    file = open("{}.csv".format(current_time), "w")
    file.write("No,Time,AP 1,AP 2,AP 3,AP 4\n")
    file.write(temp)
    file.close()
    
exportCSV()
