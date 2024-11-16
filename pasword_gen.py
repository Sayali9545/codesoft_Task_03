import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 1:
            messagebox.showerror("Error", "Password length should be at least 1.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        plabel.config(text=password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

win = tk.Tk()
win.title("Password Generator")

f1=("Algerian",12,"bold","italic")
tk.Label(win, text="Password Length:",fg='black',bg='beige',font=f1).grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(win,font=f1,bg='beige')
length_entry.grid(row=0, column=1, padx=10, pady=10)

genbutton = tk.Button(win, text="Generate Password", command=generate_password,bg='beige',fg='black',font=f1)
genbutton.grid(row=1, column=0, columnspan=2, pady=10)

plabel = tk.Label(win, text="", font=f1, fg="black",bg='beige')
plabel.grid(row=2, column=0, columnspan=2, pady=10)

win.configure(bg='pink')
win.mainloop()