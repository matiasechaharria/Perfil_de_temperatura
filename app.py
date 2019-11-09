import serial
import time
import datetime
import os
import csv


chanel1="28F49CA801000038"
chanel2="2807ADA80100005A"
chanel3="280DB9A8010000F6"
chanel4="28C6AAA8010000A3"
chanel5="282DB4A8010000AC"
chanel6="28EBA0A8010000E2"
chanel7="2877A2A8010000AD"
chanel8="286AACA80100001E"
chanel9="28039BA80100009E"

def read_usb_port():
    """Lee el puerto usb y guarda los datos"""
    for i in range(9):
        value=ser.readline()
        print (value)
        sensor=value[(16):(33)]
        print(sensor)
        valor=value[(41):(47)]
        print(valor)
        #cambio los "." por las "," para que el excel lea bien el datos
        value=value.replace(".",",")
        print(value)

        if sensor.strip() == chanel1 :
            val1=value[(41):(47)]
        elif( sensor.strip() ==chanel2):
            val2=value[(41):(47)]
        elif(sensor.strip() == chanel3 ):
            val3=value[(41):(47)]
        elif(sensor.strip()==chanel4):
            val4=value[(41):(47)]
        elif(sensor.strip()==chanel5):
            val5=value[(41):(47)]
        elif(sensor.strip()==chanel6):
            val6=value[(41):(47)]
        elif(sensor.strip()==chanel7):
            val7=value[(41):(47)]
        elif(sensor.strip()==chanel8):
            val8=value[(41):(47)]
        elif(sensor.strip()==chanel9):
            val9=value[(41):(47)]

    value2=[str(datetime.datetime.now().time()),val1,val2,val3,val4,val5,val6,val7,val8,val9]
    write_data_excel(value2)


def writeData(value):
    # Get the current data
    today = datetime.date.today()

    # Open log file 2012-6-23.log and append
    #with open(str(today)+'.log', 'ab') as f:

    with open(mesureDir+"/" +str(today)+'.log', 'ab') as f:

        f.write(value)
        # Write our integer value to our log

        f.write('\n')
        # Add a newline so we can retrieve the data easily later, could use spaces too.


def create_excel():
    """Guardo las medicion en un cvs"""
    #Creo el excel de las mediciones
    exists = os.path.exists(mesureDir+"/"+"mediciones")
    if not exists:
    #if not os.path.exists(mesureDir+"/"+"mediciones"):
        with open(mesureDir+"/"+'mediciones.csv', mode='w') as file:
            file_writer=csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['time stamp','Chanel 1', 'Chanel 2','Chanel 3', 'Chanel 4','Chanel 5', 'Chanel 6','Chanel 7', 'Chanel 8','Chanel 9'])
        file.close()

def write_data_excel(value):
    #Guardo las mediciones en el excel
    #with open('mediciones.csv', mode='a') as file:
    with open(mesureDir+"/"+'mediciones.csv', mode='a') as file:
        file_writer=csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(value)
    file.close()


if not os.path.exists("mediciones"):
    os.makedirs("mediciones")

now = datetime.datetime.now()
nowAux = str(now)
folder = nowAux[0:10]

if not os.path.exists("mediciones/"+ folder):
    os.makedirs("mediciones/"+ folder)
    print ("Carpeta creada:"+ "mediciones/"+ folder)

print ("Nombre de proyecto")
medicion = raw_input("Respeta el formato: ")

if not os.path.exists("mediciones/"+ folder+"/"+ medicion):
    os.makedirs("mediciones/"+ folder+"/"+ medicion)
    print ("Carpeta creada:"+"mediciones/"+ folder+"/"+ medicion)

mesureDir= "mediciones/"+ folder+"/"+ medicion
print (mesureDir)


try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except:
    print("error al abriri el puerto")
    exit(0);

create_excel()


while True:
    value=ser.readline()
    print (value)
    if value.strip() == "sincro":
        read_usb_port()


#     #value = int(value) #This is likely where you will get 'duff' data and catch it.
#     #writeData(value[(23+2):(23+7)]) # Write the data to a log file
#     writeData(value) # Write the data to a log file
