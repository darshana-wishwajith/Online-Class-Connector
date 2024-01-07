from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image
import json
import time

#login
def login() :
    exs = False
    username = entry_1.get()
    password = entry_2.get()
    
    with open("Data/database.json", "r") as js :
        data = json.load(js)

        if not username or not password :
            label_5.config(text = ">>> Fill username and password fields")
            messagebox.showerror("Empty Error!","Username or password is empty")
            label_5.config(text = "")
            
        else:
            
            for key in data :
                check1 = data[key]['username']
                check2 = data[key]['password']

                if username == check1 and password == check2:
                    with open("data/cls.json", "w") as log :
                        login = data[key]["classes"]

                        json.dump(login, log)

                    with open("Data/user.json", 'w') as file:
                        json.dump(key, file)

                    exs = True

            if exs == True :
                time.sleep(1)
                entry_1.config(fg = "green")
                label_5.config(text = f">>> Your Login has been succesfully!", fg = "green")
                messagebox.showinfo("Notify!", "Login Sucsessful")
                label_5.config(text = "", fg = "red")
                entry_1.config(fg = "green")
                root.destroy()
                import main
                    
            else:
                entry_1.config(fg = "red")
                entry_2.config(fg = "red")
                label_5.config(text = ">>> Check your username and password!")
                messagebox.showerror("Validation Error!", "Username or password is incorrect")
                label_5.config(text = "")
                entry_1.delete(0,END)
                entry_2.delete(0, END)
                entry_1.config(fg = "green")
                entry_2.config(fg = "green")
                
#swich to login window

def signup_window():
    answer = messagebox.askyesno("Quiz!", "Do you want to create an account ?")
    if answer == True :
        time.sleep(1)
        root.destroy()
        import reg
        print("*"*10, 'registration window opened',"*"*10)

#rootistration Window
root = Tk()
root.maxsize(600, 400)
root.minsize(600, 400)
root.title("login")
root.iconbitmap("occ.ico")

#rootistration window image
img = Image.open("img.jpg")
resized_img = img.resize((300,400), Image.ANTIALIAS)
new_img= ImageTk.PhotoImage(resized_img)

#Sign up label
label = Label(root, text = "Log In", font = ("roboto", 50, "bold"), fg = "#e3521e").place(x = 340, y = 5)

#image label
label_1= Label(root, image = new_img).place(x = 0, y = 0)

#Username frame and entry
label_2 = LabelFrame(root,text = "Username" , fg = "#2e2d2d", font = ("roboto", 12, "bold"), height = 50, width= 220).place(x = 345, y = 100)
entry_1 = Entry(root, font = ("roboto", 13, "italic"), fg = "green")
entry_1.place(x = 352, y = 120)

#Password frame and entry
label_3 = LabelFrame(root,text = "Password" , fg = "#2e2d2d", font = ("roboto", 12, "bold"), height = 50, width= 220).place(x = 345, y = 160)
entry_2 = Entry(root, font = ("roboto", 13, "italic"), fg = "green")
entry_2.place(x = 352, y = 180)

#rootister button
button_1 = Button(root, command = login, text = "Login", font = ("roboto", 15, "bold"), bg = "#e3521e", fg = "white", activebackground = "white", activeforeground = "#e3521e" , width = 10)
button_1.place(x = 385, y = 230)

#or label
label_4 = Label(root, text = "or", font = ("roboto", 20, "bold"), fg = "#2e2d2d").place(x = 435, y = 275)

#rootn button
button_2 = Button(root, command = signup_window, text = "Register", font = ("roboto", 10, "bold"), bg = "white", fg = "#e3521e", activebackground = "#e3521e", activeforeground= "white" , width = 10)
button_2.place(x = 405, y = 320)

#Terminal
label_5 = Label(root, text = "", font = ("roboto", 10, "bold"), fg = "red")
label_5.place(x = 320, y = 365)


if __name__ == "__main__" :
    root.mainloop()
