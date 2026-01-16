# The Toplevel widget creates a completely separate window that lives alongside your main
# root window.
# This is best for settings menus, alerts, or secondary tools.

import tkinter as tk

def open_new_window():
    # Create the secondary window
    new_window = tk.Toplevel(root)
    new_window.title("Secondary Window")
    new_window.geometry("300x200")
    
    tk.Label(new_window, text="This is a separate window!").pack(pady=20)
    tk.Button(new_window, text="Close", command=new_window.destroy).pack()

root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

tk.Label(root, text="Main Application").pack(pady=20)
tk.Button(root, text="Open New Window", command=open_new_window).pack()

root.mainloop()