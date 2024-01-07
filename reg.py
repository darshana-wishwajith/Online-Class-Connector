from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image
import json
import time

#Register Function
def register() :
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
            
            for one in data :
                check = data[one]['username']
                if username == check :
                    exs = True
            if exs == True :
                entry_1.config(fg = "red")
                label_5.config(text = f">>> Already have an account for '{username}'")
                messagebox.showerror("Same Username Error!", "Username already exists")
                label_5.config(text = "")
                entry_1.delete(0,END)
                entry_1.config(fg = "green")
                    
            else:

                if len(username) < 4 :
                    entry_1.config(fg = "red")
                    label_5.config(text = ">>> Enter a memorable username")
                    messagebox.showerror("Username Error!", "Username must least 4 characters")
                    label_5.config(text = "")
                    entry_1.delete(0,END)
                    entry_1.config(fg = "green")
                        

                if len(password) < 4 :
                    entry_2.config(fg = "red")
                    label_5.config(text = ">>> Enter a strong password")
                    messagebox.showerror("Password Error!", "Password must least 4 characters")
                    label_5.config(text = "")
                    entry_2.delete(0,END)
                    entry_2.config(fg = "green")
                    
                else:
                    if exs == False:
                        time.sleep(2)
                        with open("Data/database.json", "r") as js :
                            data = json.load(js)
                            keys = list(data.keys())
                            last = keys[-1]
                            number = last[-1]
                            num = int(number) + 1

                            data[f"user{str(num)}"] = {"username" : username, "password" : password, "classes" : {"Select" : "link"}}

                        with open("Data/database.json", "w") as js :
                            json.dump(data, js)
                        
                        label_5.config(text = ">>> Your Signup has been succesfully!", fg = "green")
                        messagebox.showinfo("Notify!", "Sign Up Sucsessful")
                        label_5.config(text = "", fg = "red")
                        entry_1.delete(0,END)
                        entry_2.delete(0,END)

#swich to login window

def login_window():
    answer = messagebox.askyesno("Quiz!", "have already an account ?")
    if answer == True :
        time.sleep(1)
        root.destroy()
        import logi


#rootistration Window
root = Tk()
root.maxsize(600, 400)
root.minsize(600, 400)
root.title("Registration")
root.iconbitmap("occ.ico")

#rootistration window image
img = Image.open("img.jpg")
resized_img = img.resize((300,400), Image.ANTIALIAS)
new_img= ImageTk.PhotoImage(resized_img)

#Sign up label
label = Label(root, text = "Sign Up", font = ("roboto", 50, "bold"), fg = "#e3521e").place(x = 340, y = 5)

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
#Register button
button_1 = Button(root, command = register ,text = "Register", font = ("roboto", 15, "bold"), bg = "#e3521e", fg = "white", activebackground = "white", activeforeground= "#e3521e" , width = 10)
button_1.place(x = 385, y = 230)
#or label
labe_4 = Label(root, text = "or", font = ("roboto", 20, "bold"), fg = "#2e2d2d").place(x = 435, y = 275)

#login button
button_2 = Button(root, command = login_window, text = "Login", font = ("roboto", 10, "bold"), bg = "white", fg = "#e3521e", activebackground = "#e3521e", activeforeground = "white" , width = 10)
button_2.place(x = 405, y = 320)
#Terminal
label_5 = Label(root, text = "", font = ("roboto", 10, "bold"), fg = "red")
label_5.place(x = 320, y = 365)



if __name__ == "__main__" :
    root.mainloop()
    
