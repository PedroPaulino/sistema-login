# Importando Bibliotecas #

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Criando Janela #

root = Tk()
root.title("Hope Tech - Access Dashboard")
root.geometry("600x300")
root.resizable(width=False, height=False)

# Design #

mainframe = ttk.Frame(root, padding = "30 30 12 12")
mainframe.grid(column=0, row=0,sticky=(N, W, E, S), pady="60")
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=0)

username = StringVar()
username_entry = ttk.Entry(mainframe, width = 70, textvariable = username)
username_entry.grid(column=3, row=1, sticky=(W,S), pady= "20")

password = StringVar()
password_entry = ttk.Entry(mainframe, width = 70, textvariable = username)
password_entry.grid(column=3, row=2, sticky=(W,S))

ttk.Label(mainframe, text="Username").grid(column=2, row=1, sticky=(W, S), pady= "20")
ttk.Label(mainframe, text="Password").grid(column=2, row=2, sticky=(W, S))



root.mainloop()


