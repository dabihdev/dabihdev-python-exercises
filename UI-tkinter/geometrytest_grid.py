import tkinter as tk

root = tk.Tk()
root.title("Grid Example")

# Create a Label and an Entry for a username field
user_label = tk.Label(root, text="Username:")
user_label.grid(row=0, column=0)
user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1)

# Create a Label and an Entry for a password field
pass_label = tk.Label(root, text="Password:")
pass_label.grid(row=1, column=0)
pass_entry = tk.Entry(root, show="*")
pass_entry.grid(row=1, column=1)

# Add a button
login_button=tk.Button(root, text="Login")
login_button.grid(row=2, column=0)

# Configure the columns to resize when the window is resized
root.grid_columnconfigure(1, weight=1)

root.mainloop()