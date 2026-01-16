# HIDE AND SHOW

import tkinter as tk

def go_to_page2():
    frame1.pack_forget()  # Hide page 1
    frame2.pack(fill="both", expand=True)  # Show page 2

def go_to_page1():
    frame2.pack_forget()  # Hide page 2
    frame1.pack(fill="both", expand=True)  # Show page 1

root = tk.Tk()
root.geometry("300x200")

# --- PAGE 1 ---
frame1 = tk.Frame(root, bg="lightblue")
tk.Label(frame1, text="This is Page 1", bg="lightblue").pack(pady=20)
tk.Button(frame1, text="Next Page", command=go_to_page2).pack()
frame1.pack(fill="both", expand=True) # Start with Page 1 visible

# --- PAGE 2 ---
frame2 = tk.Frame(root, bg="lightgreen")
tk.Label(frame2, text="This is Page 2", bg="lightgreen").pack(pady=20)
tk.Button(frame2, text="Back", command=go_to_page1).pack()

root.mainloop()