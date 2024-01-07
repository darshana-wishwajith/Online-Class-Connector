from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image
import json
import time

def delete() :
    class_name = entry_1.get()

    if not class_name :
        messagebox.showerror("Empty Error!", "Please enter a class name")
    
    else :

        answer = messagebox.askyesno(f"Do you want to delete '{class_name}' class ?", "Class details will be deleted!")
        if answer :
            with open("Data/user.json", 'r') as user :
                user_data = json.load(user)

            with open("Data/cls.json", 'r') as cls :
                classes = json.load(cls)
                del classes[class_name]

            with open("Data/cls.json", 'w') as cls :  
                json.dump(classes, cls)

            with open("Data\database.json" ,"r") as data :
                full = json.load(data)
            
            with open("Data\database.json" ,"w") as data :
                del full[user_data]["classes"][class_name]
                json.dump(full, data)
            
            label_2.config(fg = "green", text = ">>> Restart application for apply changes")
            messagebox.showinfo("Alert!", f"Your '{class_name}' class has been delete successfully!")
            import main
            main.label_2.config(fg = "green", text = ">>> Restart application for apply changes")

def add_class() :
    class_name = entry_1.get()
    link = entry_2.get()

    if not class_name or not link :
            label_2.config(text = ">>> Fill Class Name and link fields", fg = "red")
            messagebox.showerror("Empty Error!","Class Name or Link is empty")
            label_2.config(text = "")

    else:
        with open("Data/user.json", 'r') as user :
            user_data = json.load(user)

        with open("Data/cls.json", 'r') as cls :
            classes = json.load(cls)

        with open("Data/cls.json", 'w') as cls :
            classes[class_name] = link
            json.dump(classes, cls)

        with open("Data\database.json" ,"r") as data :
            full = json.load(data)
        
        with open("Data\database.json" ,"w") as data :
            full[user_data]["classes"][class_name] = link
            json.dump(full, data)

        label_2.config(fg = "green")
        label_2.config(fg = "green", text = ">>> Restart application for apply changes")
        messagebox.showinfo("Alert!","Class has been added successfully!")
        import main
        main.label_2.config(fg = "green", text = ">>> Restart application for apply changes")
            
#Window
root = Tk()
root.maxsize(600, 400)
root.minsize(600, 400)
root.title("Class Adder")
root.iconbitmap("occ.ico")

#intro label
label = Label(root, text = "Add your classes one by one", font = ("roboto", 25, "bold"), fg = "#e3521e").place(x = 70, y = 25)

#Class name frame and entry
label_2 = LabelFrame(root,text = "Class Name" , fg = "#2e2d2d", font = ("roboto", 12, "bold"), height = 50, width= 220).place(x = 193, y = 100)
entry_1 = Entry(root, font = ("roboto", 13, "italic"), fg = "green")
entry_1.place(x = 200, y = 120)
#link frame and entry
label_3 = LabelFrame(root,text = "Link" , fg = "#2e2d2d", font = ("roboto", 12, "bold"), height = 50, width= 220).place(x = 193, y = 160)
entry_2 = Entry(root, font = ("roboto", 13, "italic"), fg = "green")
entry_2.place(x = 200, y = 180)
#add button
button_1 = Button(root ,command = delete, text = "Delete", font = ("roboto", 15, "bold"), bg = "#e3521e", fg = "white", activebackground = "white", activeforeground= "#e3521e" , width = 10)
button_1.place(x = 310, y = 250)

button_2 = Button(root ,command  = add_class, text = "Add", font = ("roboto", 15, "bold"), bg = "#e3521e", fg = "white", activebackground = "white", activeforeground= "#e3521e" , width = 10)
button_2.place(x = 160, y = 250)

#Terminal Label
label_2 = Label(root, text = "", font = ("roboto",15,), fg = "green")
label_2.place(x = 160, y = 330)



if __name__ == "__main__" :
    root.mainloop()