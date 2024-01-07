from tkinter import *
from pynput.mouse import Controller
from threading import Thread

mouse = Controller()

class CoodsApp(Tk) :
    def __init__(self, size, title) :
        super(CoodsApp, self).__init__()

        self.geometry(size)
        self.title(title)
        self.iconbitmap("occ.ico")
        
        global disply
        disply = Label(self, text = "")
        disply.grid(column = 1, row = 1)

        self.mainloop()
    
    def get_coods() :
        while True :
            x, y = mouse.position
            print(f"X : {x}  Y : {y}")
            

    thread_1 = Thread(target = get_coods)
    thread_1.start()

coods = CoodsApp('300x400', 'Coods App')

