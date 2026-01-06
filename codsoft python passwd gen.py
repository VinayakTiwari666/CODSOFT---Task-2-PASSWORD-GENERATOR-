import random
import string
import tkinter as tk
# fxn part 
def gen_pass():
    val =length.get()

    if val == "":
        result.config(text="Please enter length ! ")
        return

    if not val.isdigit():
        result.config(text="Enter numbers only ! ")
        return

    l = int(val)

    if l<=0:
        result.config(text=" ERROR ! Length must be greater than 0")
        return
    if l>50:
        result.config(text=" ERROR ! Max length of 50 Exceeded")
        return
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"
    pwd = ""
    for i in range(l):
        pwd += random.choice(chars)
    result.config(text=pwd)
def copy_passwd():
    pwd = result.cget("text")
    if pwd != "":
        root.clipboard_clear()
        root.clipboard_append(pwd)
# GUI part
root = tk.Tk()
root.title("Password Generator")
root.geometry("380x300")#window
root.resizable(False, False)
tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 16, "bold")
).pack(pady=10)
tk.Label(root, text="Enter Password Length", font=("Arial", 11)).pack()
length = tk.Entry(root, font=("Arial", 12), justify="center")
length.pack(pady=5)
tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 11),
    bg="green",
    fg="black",
    width=22,
    command=gen_pass
).pack(pady=10)
tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 11),
    bg="lightblue",
    fg="black",
    width=22,
    command=copy_passwd
).pack(pady=5)
result = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    wraplength=330
)
result.pack(pady=10)
root.mainloop()



