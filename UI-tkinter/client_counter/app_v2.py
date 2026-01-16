import tkinter as tk

def next_client():
    """Increments the client number and updates the label."""
    current_number = int(client_number_label.cget("text"))
    next_number = current_number + 1
    client_number_label.config(text=str(next_number))

def cancel_client():
    """Decreases the client number and updates the label."""
    current_number = int(client_number_label.cget("text"))
    if current_number > 1:
        next_number = current_number - 1
        client_number_label.config(text=str(next_number))

def reset_client():
    """Resets the client number to 1."""
    client_number_label.config(text="1")

# Create the main window
root = tk.Tk()
root.title("Client Counter")
root.geometry("400x300")
root.configure(bg="white")

# Use a frame to center the content
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True)

# "CLIENTE NUMERO:" label
title_label = tk.Label(main_frame, text="CLIENTE NUMERO:", font=("Arial", 16), bg="white")
title_label.pack(pady=(20, 10))

# Client number label
client_number_label = tk.Label(main_frame, text="1", font=("Arial", 48, "bold"), bg="white")
client_number_label.pack(pady=10)

# Frame for buttons to keep them on the same line
button_frame = tk.Frame(main_frame, bg="white")
button_frame.pack(pady=20)

# "prossimo" button
next_button = tk.Button(button_frame, text="prossimo", font=("Arial", 14), command=next_client,
                        padx=10, pady=5, relief="solid", borderwidth=2)
next_button.pack(side="left", padx=5)

# "cancel" button
cancel_button = tk.Button(button_frame, text="cancel", font=("Arial", 14), command=cancel_client,
                          padx=10, pady=5, relief="solid", borderwidth=2)
cancel_button.pack(side="left", padx=5)

# "reset" button
reset_button = tk.Button(button_frame, text="reset", font=("Arial", 14), command=reset_client,
                         padx=10, pady=5, relief="solid", borderwidth=2)
reset_button.pack(side="left", padx=5)

# Start the application
root.mainloop()