from Tkinter import *
from ttk import *
from backend import backend
import sys
import glob
import serial


class Example(Frame):


    def __init__(self, parent):

        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

        self.connected = FALSE

    def connect(self):

        self.con = backend(self.portvar.get())
        self.console.insert(INSERT, "Connected to Board"+"\n")
        self.connected = TRUE

    def update(self):

        if (self.connected == TRUE):


            freq = float(self.inFrequency.get())
            vol = float(self.inVoltage.get())

            if (freq < 30 and freq <= 25000 and vol >= 0 and vol <= 13): #zeroing the values

                steps = (255.0/13.0)*vol

                f_freq = str(int(round(freq))).zfill(5)
                f_steps = str(int(round(steps))).zfill(3)



                self.console.insert(INSERT, f_freq + f_steps +'p'+"\n")
                self.console.insert(INSERT, self.con.update(f_freq, f_steps)+"\n")
                self.console.see(END)

            elif (freq >= 30 and freq <= 25000 and vol >+ 0 and vol <= 13):

                steps = (255.0/13.0)*vol

                f_freq = str(int(round(freq))).zfill(5)
                f_steps = str(int(round(steps))).zfill(3)



                self.console.insert(INSERT, f_freq + f_steps +'p'+"\n")
                self.console.insert(INSERT, self.con.update(f_freq, f_steps)+"\n")
                self.console.see(END)

            else:
                self.console.insert(INSERT, "Invalid Entry" + "\n")


        else:
            self.console.insert(INSERT, "Please connect to a COM  port" + "\n")

    def serial_ports(self):

        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]

        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')

        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')

        else:
            raise EnvironmentError('Unsupported platform')

        result = []

        for port in ports:

            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)

            except (OSError, serial.SerialException):
                pass

        return result

    def clear(self):



        if (self.connected == TRUE):
            self.inFrequency.delete(0, END)
            self.inFrequency.insert(END,'0')

            self.inVoltage.delete(0, END)
            self.inVoltage.insert(END,'0')

            self.update()
        else:
            self.console.insert(INSERT, "Please connect to a COM  port" + "\n")

    def initUI(self):

        self.parent.title("Function Generator")
        self.pack(fill=BOTH, expand=True)

        blank = Frame(self)
        blank.pack(fill=X)

        bblank = Label(blank, text="                ", width=20)
        bblank.pack(side=LEFT, padx=5, pady=5)

        port = Frame(self)
        port.pack(fill=X)

        cport = Label(port, text="Communication Port", width=20)
        cport.pack(side=LEFT, padx=5, pady=5)

        self.portvar = StringVar()
        self.portvar.set("a")

        mylist = list(self.serial_ports())
        self.inPort = OptionMenu(port, self.portvar, "COM Port", *mylist)
        self.inPort.pack(fill=X, padx=2, expand=True)

        connectFrame = Frame(self)
        connectFrame.pack(fill=X)

        connectButton = Button(connectFrame, text="Connect", command=lambda: self.connect())
        connectButton.pack(side=RIGHT, padx=60, pady=5)

        freq = Frame(self)
        freq.pack(fill=X)

        frequency = Label(freq, text="Frequency [30 - 25000] Hz", width=20)
        frequency.pack(side=LEFT, padx=5, pady=5)

        self.inFrequency = Entry(freq)
        self.inFrequency.pack(fill=X, padx=2, expand=True)

        vol = Frame(self)
        vol.pack(fill=X)

        voltage = Label(vol, text="Voltage [0 - 13] V", width=20)
        voltage.pack(side=LEFT, padx=5, pady=5)

        self.inVoltage = Entry(vol)
        self.inVoltage.pack(fill=X, padx=2, expand=True)

        up = Frame(self)
        up.pack(fill=X)

        updateb = Button(up, text="Update", command=lambda : self.update())
        updateb.pack(side=LEFT, padx=60, pady=5)

        clearb = Button(up, text="Zero", command=lambda : self.clear())
        clearb.pack(side=RIGHT, padx=60, pady=5)

        conlab = Frame(self)
        conlab.pack(fill=X)

        conlable = Label(conlab, text="Console Output", width=11)
        conlable.pack(padx=5, pady=5)

        con = Frame(self)
        con.pack(fill=BOTH, expand=True)

        self.console = Text(con)
        self.console.bind("<Key>", lambda e: "break")
        self.console.pack(fill=BOTH, pady=5, padx=5, expand=True)







def main():

    root = Tk()
    root.geometry("400x600+100+100") # hight, width, x, y
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()






