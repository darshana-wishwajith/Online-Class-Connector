from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import json
import time
import requests
import webbrowser


#main Window
root = Tk()
root.maxsize(600, 400)
root.minsize(600, 400)
root.title("Online Class Connector")
root.iconbitmap("occ.ico")

def connect():
    try:
        with open("Data/cls.json", "r") as log :
            data = json.load(log)
            
        url = data[f'{subject}']

        if subject == "Select" :
            messagebox.showwarning("Select Error", "Please Select a class")
        
        else:
            response = requests.get(url)

            if response.status_code == 200 :
                label_2.config(text = ">>> You are Connected !")
                answer = messagebox.askokcancel("Connected!", f"joining to \"{subject}\" class ?")
                label_2.config(text = "" ,fg = "green")
                if answer :
                    webbrowser.open(url)

    except :
        label_2.config(text = ">>> Somthing went wrong !" ,fg = "red")
        messagebox.showerror("Unidentified Error!","Select another class or check your internet connection")
        label_2.config(text = "" ,fg = "green")

def select (event) :
    global subject
    subject = combobox_1.get()

def add() :
    import add

#Intro label
label_1 = Label(root, text = "You can select your class\n and connect it", font = ("roboto",30, "bold"), fg = "#e3521e").place(x = 55, y = 5)
#Terminal Label
label_2 = Label(root, text = "", font = ("roboto",15,), fg = "green")
label_2.place(x = 160, y = 320)
#Subject menu
options = []
with open("Data/cls.json", 'r') as file :
    data = json.load(file)
    subjects = data.keys()

    for subject in subjects:
        options.append(subject)

combobox_1 = ttk.Combobox(root, values = options , state = 'readonly')
current = combobox_1.current(0)
combobox_1.bind("<<ComboboxSelected>>", select)
combobox_1.place(x = 190, y = 150, width = 200)
    
button_1 = Button(root, command = connect, text = "Connect", font = ("roboto", 15, "bold"), bg = "#e3521e", fg = "white", activebackground = "white", activeforeground = "#e3521e" , width = 10)
button_1.place(x = 150, y = 230)

button_2 = Button(root, command = add, text = "Add Class", font = ("roboto", 15, "bold"), bg = "#e3521e", fg = "white", activebackground = "white", activeforeground = "#e3521e" , width = 10)
button_2.place(x = 300, y = 230)


if __name__ == "__main__" :
    root.mainloop()
