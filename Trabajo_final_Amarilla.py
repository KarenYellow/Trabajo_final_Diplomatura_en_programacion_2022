#Trabajo final de la diplomatura en programación impulsado por la iniciativa "Mujeres Tech", en este trabajo se realizará un sistema de gestión de altas y bajas 
#para un portal importante de busqueda de empleo.
#Nombre: Karen Amarilla
from cgitb import grey
from distutils.cmd import Command
import string
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showerror, showinfo

#Interfaz gráfica, en este caso se utilizará la libreria Tkinter.
master = Tk ()
master.config(background="lightpink")
master.title("SIGB - Sistema de Gestión de Bumeran ")
master.geometry("400x200")
master.resizable(0,0)
#Mensaje inicial
label1= Label (master, text="Bienvenido al Sistema de Gestión de Bumeran en Argentina")
label1.pack(pady=5)

#Alta:

class altas(Toplevel):

    def __init__(self,master = None):
        super().__init__(master = master)
        self.title("Altas de usuario")
        self.resizable(0,0)
        self.grab_set()     
        nombre = ""
        edad = ""
        self.nombre = Label(self, text="Nombre y apellido: ")
        self.nombre.pack(side="left")
        self.nombre = Entry(self)
        self.nombre.pack(side="left")

        self.edad= Label(self, text="Edad ")
        self.edad.pack(side="left")
        self.edad = Entry(self)
        self.edad.pack(side="left")

        self.dni= Label (self, text="DNI: ")
        self.dni.pack(side="left")
        self.dni= Entry (self)
        self.dni.pack(side="left")

        self.button_guardar = Button(self, text="Guardar", command=self.actualizar_datos)
        self.button_guardar.pack(side="left")

        self.button_cancelar = Button(self, text="Cancelar", command=self.destroy)
        self.button_cancelar.pack(side="left")

    def actualizar_datos(self):
        
        nombre = self.nombre.get()
        edad_text = self.edad.get()
        dni_text = self.dni.get ()

        nombre_edad_dni_requerido = (nombre.isspace() or nombre == "") and (edad_text.isspace() or edad_text == "") and (dni_text.isspace() or dni_text== "")

        nombre_requerido = (nombre.isspace() and not edad_text.isspace() and not dni_text.isspace()) or (nombre == "" and edad_text != "" and dni_text!= "") or (not nombre.isalpha())

        edad_requerido = (not nombre.isspace() and edad_text.isspace()) or (nombre != "" and edad_text == "") or (nombre != "" and edad_text<=str (17) or edad_text< str (100)) or (not edad_text.isdigit())

        dni_requerido = (dni_text.isspace() and not edad_text.isspace() and not nombre.isspace()) or (nombre!="" and edad_text!="" and dni_text=="") or (not dni_text.isdigit()) 

        mensaje = "Ingresar nombre, apellido, edad y DNI" if nombre_edad_dni_requerido else "Debe ingresar nombre y apellido (Revisar datos ingresados)" if nombre_requerido else "Debe ingresar edad o ingresar edad correcta (Mayor a 18 años / Menor de 100 años)" if edad_requerido else "Debe ingresar D.N.I. caso contrario revisar datos ingresados(Solo números)" if dni_requerido else None
        
        if mensaje:
            showerror("Campos requeridos", mensaje, parent=self)
        else:
            showinfo("Acción exitosa", "Los datos se han guardado correctamente", parent=self)
            contadores(1)
            self.destroy()    


#Variables globales para utilizar los contadores de altas y bajas de trabajadores.
lista_altas=[]
lista_bajas=[]
suma_altas=int(0)
suma_bajas=int(0)

def contadores(number):
    if number == 1:
        lista_altas.append(1)
    elif number == 2:
        lista_bajas.append(1)
    elif number == 3:
        suma_altas=sum(lista_altas)
        suma_bajas=sum(lista_bajas)
        reporte="Cantidad de altas cargadas: "+ str(suma_altas)+"\nCantidad de bajas cargadas: "+str(suma_bajas)
        showinfo("Reporte diario",reporte)

#Botones a utilizar por el usuario:

#Altas:
alta= Button(master, text="Alta")
alta.pack(side=TOP)
alta.bind("<Button>", lambda e: altas(master))
alta.pack(pady = 15)

#Bajas:
#boton2 = Button(root, text="Baja", bd=35, bg= "blue")
#boton2.pack()

#Reportes:
reporte= Button(master, text="Reportes")
reporte.pack(side=TOP)
reporte.bind("<Button>", lambda e: contadores(3))
reporte.pack(pady=15)


#Salida del programa
boton4 = Button(master, text="Salir", command=master.quit)
boton4.pack(pady=15)


mainloop()