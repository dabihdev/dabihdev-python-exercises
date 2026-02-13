from tkinter import *

def show_selection():
    selected = []
    # Check each variable to see if it's "on" (1)
    if Checkbutton1.get() == 1:
        selected.append("Tutorial")
    if Checkbutton2.get() == 1:
        selected.append("Student")
    if Checkbutton3.get() == 1:
        selected.append("Courses")
    
    # Update the result_label text
    if selected:
        result_label.config(text="You selected: " + ", ".join(selected))
    else:
        result_label.config(text="Nothing selected")

root = Tk() 
root.geometry("350x300") 

w = Label(root, text='GeeksForGeeks', font=("Arial", 20)) 
w.pack() 

Checkbutton1 = IntVar() 
Checkbutton2 = IntVar() 
Checkbutton3 = IntVar() 

Button1 = Checkbutton(root, text="Tutorial", 
                    variable=Checkbutton1, 
                    onvalue=1, 
                    offvalue=0) 

Button2 = Checkbutton(root, text="Student", 
                    variable=Checkbutton2, 
                    onvalue=1, 
                    offvalue=0) 

Button3 = Checkbutton(root, text="Courses", 
                    variable=Checkbutton3, 
                    onvalue=1, 
                    offvalue=0) 
    
Button1.pack() 
Button2.pack() 
Button3.pack() 


# 1. The Submit Button
submit_btn = Button(root, text="Submit Selection", command=show_selection, bg="blue", fg="white")
submit_btn.pack(pady=10)

# 2. The Result Label
result_label = Label(root, text="", font=("Arial", 10, "italic"))
result_label.pack(pady=10)

mainloop()