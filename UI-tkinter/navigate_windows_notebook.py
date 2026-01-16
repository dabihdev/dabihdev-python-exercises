import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabbed App")
root.geometry("400x300")

# Create the Tab Control
notebook = ttk.Notebook(root)

# Tab 1
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Home")
tk.Label(tab1, text="Welcome to the Home Tab").pack(pady=30)

# Tab 2
tab2 = tk.Frame(notebook)
notebook.add(tab2, text="Settings")
tk.Label(tab2, text="Adjust your preferences here").pack(pady=30)

notebook.pack(expand=1, fill="both")

root.mainloop()