from tkinter import *
import time

root=Tk()
root.title("SIGB")
root.geometry("800x500")

label1= Label (root, text="Bienvenido al Sistema de Gestión de Bumeran")
label1.pack()

boton2 = Button(root, text="Altas")
boton2.pack()

#oao

boton5 = Button(root, text="cerra2", command=root.iconify)
boton5.pack()
root.mainloop()