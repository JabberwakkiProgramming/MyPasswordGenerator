import random
import tkinter as tk
from tkinter import ttk

# ----- generate password -----
def generate_password(event=None):
    import random
    import string

    text = length_entry.get()
    if text == "" or not text.isdigit():
        result_label.config(text="")
        return

    length = int(text)

    # require at least 8 chars for all rules
    if length < 8:
        result_label.config(text="Min length = 8")
        return

    # required character sets
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    number = random.choice(string.digits)
    special = random.choice("!@#$%&*?")

    # put required ones in list
    password_list = [lowercase, uppercase, number, special]

    # all possible characters
    all_chars = string.ascii_letters + string.digits + "!@#$%&*?"

    # fill remaining length
    for i in range(length - 4):
        password_list.append(random.choice(all_chars))

    # shuffle so pattern isn't predictable
    random.shuffle(password_list)

    # convert list → string
    password = "".join(password_list)

    result_label.config(text=password)

    # auto copy
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

    status_label.config(text=">> Secure Password Generated & Copied <<")

# ----- copy password -----
def copy_password():
    password = result_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
    status_label.config(text=">> Secure Password Copied <<")

# ----- window -----
window = tk.Tk()
window.title("My Password Generator")
window.geometry("450x320")
window.configure(bg="black")

# ---- STYLE FIX ----
style = ttk.Style()
style.theme_use("clam")  # important: allows custom colors

style.configure(
    "Hacker.TButton",
    background="black",
    foreground="blue",
    bordercolor="blue",
    focusthickness=3,
    focuscolor="none",
    font=("Club Type Medium", 12, "bold"),
    padding=6
)

style.map(
    "Hacker.TButton",
    background=[("active", "black")],
    foreground=[("active", "blue")]
)

# Title
title_label = tk.Label(window, text="MY PASSWORD GENERATOR",
                       font=("Club Type Medium", 16, "bold"),
                       fg="blue", bg="black")
title_label.pack(pady=15)

# Length input
length_label = tk.Label(window, text="Enter password length:",
                        font=("Club Type Medium", 12),
                        fg="blue", bg="black")
length_label.pack()

length_entry = tk.Entry(window, font=("Club Type Medium", 12),
                        bg="black", fg="blue",
                        insertbackground="blue",
                        justify="center")
length_entry.pack(pady=5)
length_entry.bind("<Return>", generate_password)

# Hacker buttons (fixed)
generate_button = ttk.Button(window, text="GENERATE",
                             style="Hacker.TButton",
                             command=generate_password)
generate_button.pack(pady=10)

copy_button = ttk.Button(window, text="COPY",
                         style="Hacker.TButton",
                         command=copy_password)
copy_button.pack(pady=5)

# Result
result_label = tk.Label(window, text="",
                        font=("Club Type Medium", 14),
                        fg="blue", bg="black")
result_label.pack(pady=10)

status_label = tk.Label(window, text="",
                        font=("Club Type Medium", 10),
                        fg="blue", bg="black")
status_label.pack()

window.mainloop()
