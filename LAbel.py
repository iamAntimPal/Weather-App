def btn():
     print("hello world")

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Label as Button")

# Define a label styled as a button
label_button = tk.Label(root, text="Button Label", bg="lightgray", fg="black", padx=20, pady=10, relief="raised", bd=2)

# Place the label in the window
label_button.pack(pady=20)

# Run the main loop
root.mainloop()
