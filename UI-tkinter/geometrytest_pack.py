import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

# Default: Stacks vertically at the top
label1 = tk.Label(root, text="Label 1 (Default)", bg="red", fg="white")
label1.pack()

# Packs to the left side
label2 = tk.Label(root, text="Label 2 (Left)", bg="blue", fg="white")
label2.pack(side=tk.LEFT)

# Packs to the right side
label3 = tk.Label(root, text="Label 3 (Right)", bg="green", fg="white")
label3.pack(side=tk.RIGHT)

root.mainloop()