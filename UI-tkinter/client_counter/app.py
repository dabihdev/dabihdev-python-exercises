# 1. IMPORTA LE LIBRERIE
import tkinter as tk

# 2. SEZIONE FUNZIONI (CHE SONO I COMANDI CHE AGISCONO SUL PROGRAMMA DA DIETRO LE QUINTE)
def next_client():
    """Increments the client number and updates the label."""
    current_number = int(client_number_label.cget("text"))
    next_number = current_number + 1
    client_number_label.config(text=str(next_number))


# 3. SEZIONE GRAFICA (QUELLO CHE VEDI SULLO SCHERMO)

# Create the main window
root = tk.Tk() # initializes window
root.title("Client Counter") # set window title
root.geometry("400x300") # set window dimensions
root.configure(bg="white") # set window background

# Use a frame to center the content
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True)

# "CLIENTE NUMERO:" label
title_label = tk.Label(main_frame, text="CLIENTE NUMERO:", font=("Arial", 16), bg="white")
title_label.pack()

# Client number label
client_number_label = tk.Label(main_frame, text="1", font=("Arial", 48, "bold"), bg="white")
client_number_label.pack()

# "prossimo" button
next_button = tk.Button(main_frame, text="prossimo", font=("Arial", 14), command=next_client,
                        padx=20, pady=10, relief="solid", borderwidth=2)
next_button.pack()


# 4. SEZIONE MAINLOOP
# Start the application
root.mainloop()