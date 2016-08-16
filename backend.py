import serial as ser
from time import sleep


class backend:

    def __init__(self, port):

        mySerial = ser.Serial(str(port), 4800)

        sleep(2)

    def update(self, freq, vol):

        self.mySerial.write(str(freq + vol + 'p'))
        sleep(2)


        return self.mySerial.readline()


