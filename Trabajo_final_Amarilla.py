#Trabajo final de la diplomatura en programación impulsado por la iniciativa "Mujeres Tech", en este trabajo se realizará un sistema de gestión de altas y bajas 
#para un portal importante de busqueda de empleo.
#Nombre: Karen Amarilla

from tkinter import *
import time
#Interfaz gráfica, en este caso se utilizará la libreria Tkinter.
root=Tk()
root.title("SIGB - Sistema de Gestión de Bumeran ")
root.geometry("800x500")
root.resizable(0,0)
#Mensaje inicial
label1= Label (root, text="Bienvenido al Sistema de Gestión de Bumeran")
label1.pack()

#Botones a utilizar por el usuario:

#Altas:
boton2 = Button(root, text="Alta", bd=5, bg= "green")
boton2.pack()

#Bajas:
boton3 = Button(root, text="Baja", bd=5, bg= "green")
boton3.pack()

#Reportes:

boton4 = Button(root, text="Reportes", bd=5, bg= "green")
boton4.pack()

#Salida del programa
#boton5 = Button(root, text="cerra2", command=root.iconify)
#boton5.pack()

root.mainloop()