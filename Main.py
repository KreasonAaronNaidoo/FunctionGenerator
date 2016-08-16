import Tkinter
from backend import backend

from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from ttk import Frame, Label, Entry, Button

class Example(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def update(self):

        bfreq = '{0:04b}'.format(int(self.inFrequency.get()))
        bvol = '{0:03b}'.format(int(self.inVoltage.get()))

        self.console.insert('1.0','\n')
        self.console.insert('1.0', backend(self.inPort.get()).update(bfreq, bvol))
        #cannot run this without the board present





    def initUI(self):

        self.parent.title("Function Generator")
        self.pack(fill=BOTH, expand=True)

        port = Frame(self)
        port.pack(fill=X)

        cport = Label(port, text="Communication Port", width=20)
        cport.pack(side=LEFT, padx=5, pady=5)

        self.inPort = Entry(port)
        self.inPort.pack(fill=X, padx=2, expand=True)

        freq = Frame(self)
        freq.pack(fill=X)

        frequency = Label(freq, text="Frequency Hz (0 - 16)", width=20)
        frequency.pack(side=LEFT, padx=5, pady=5)

        self.inFrequency = Entry(freq)
        self.inFrequency.pack(fill=X, padx=2, expand=True)

        vol = Frame(self)
        vol.pack(fill=X)

        voltage = Label(vol, text="Voltage V (0 - 8)", width=20)
        voltage.pack(side=LEFT, padx=5, pady=5)


        self.inVoltage = Entry(vol)
        self.inVoltage.pack(fill=X, padx=2, expand=True)


        up = Frame(self)
        up.pack(fill=X)

        updateb = Button(self, text="Update", command=lambda : self.update())
        updateb.pack(side=TOP, padx=5, pady=5)

        conlab = Frame(self)
        conlab.pack(fill=X)

        conlable = Label(conlab, text="Console Output", width=11)
        conlable.pack(side=TOP,padx=5, pady=5)

        con = Frame(self)
        con.pack(fill=BOTH, expand=True)

        self.console = Text(con)
        self.console.bind("<Key>", lambda e: "break")
        self.console.pack(fill=BOTH, pady=5, padx=5, expand=True)







def main():
    root = Tk()
    root.geometry("300x600+100+100") # hight, width, x, y
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()






