##################################################################################################################################################################
#Trabajo final de la diplomatura en programación impulsado por la iniciativa "Mujeres Tech", en este trabajo se realizará un sistema de gestión de altas y bajas##
#para un portal importante de busqueda de empleo.                                                                                                               ##
#Nombre: Karen Amarilla                                                                                                                                         ##
##################################################################################################################################################################
#Análisis:                                                                                                                                                      ##
#Datos solicitados: Nombre, Edad, DNI, motivo de baja                                                                                                           ##
#Operaciones a realizar: Cantidad de altas y bajas de trabajadores (Sumas), Minimo y máximo de edad de las Altas realizadas(Mediante acumuladores).             ##
#Salida= Cantidad de altas y bajas de trabajadores, minimo y máximo de edad de Altas realizadas.                                                                ##
##################################################################################################################################################################
#Prueba de escritorio:                                                                                                                                          ##
#                                                                                                                                                               ##
#                                                                                                                                                               ##
#                                                                                                                                                               ##
#                                                                                                                                                               ##
#                                                                                                                                                               ##
##################################################################################################################################################################
from cgitb import grey
from distutils.cmd import Command
import string
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showerror, showinfo

#Variables globales para utilizar los contadores de altas y bajas de trabajadores.
lista_altas=[]
lista_bajas=[]
suma_altas=int(0)
suma_bajas=int(0)

#Interfaz gráfica, en este caso se utilizará la libreria Tkinter.
master = Tk ()
master.config(background="lightpink")
master.title("SIGB - Sistema de Gestión de Bumeran ")
master.geometry("400x300")
master.resizable(0,0)
#Mensaje inicial
label1= Label (master, text="Bienvenido al Sistema de Gestión de Bumeran en Argentina")
label1.pack(pady=5)

#definición del class altas:
class altas(Toplevel):
    #Se define las caracteristicas de la ventana, junto con los datos a ingresar:
    def __init__(self,master = None):
        super().__init__(master = master)
        self.title("Altas de usuario")
        self.resizable(0,0)
        self.grab_set()     
        nombre = ""
        edad = ""
        dni = ""
        #Ingreso del nombre completo
        self.nombre = Label(self, text="Nombre y apellido: ")
        self.nombre.pack(side="left")
        self.nombre = Entry(self)
        self.nombre.pack(side="left")
        #Ingreso de la edad 
        self.edad= Label(self, text="Edad ")
        self.edad.pack(side="left")
        self.edad = Entry(self)
        self.edad.pack(side="left")
        #Ingreso del dni
        self.dni= Label (self, text="DNI: ")
        self.dni.pack(side="left")
        self.dni= Entry (self)
        self.dni.pack(side="left")
        #Botón de guardado
        self.button_guardar = Button(self, text="Guardar", command=self.actualizar_datos)
        self.button_guardar.pack(side="left")
        #Botón de cancelado
        self.button_cancelar = Button(self, text="Cancelar", command=self.destroy)
        self.button_cancelar.pack(side="left")
    
    def actualizar_datos(self):
        nombre_obtenido = self.nombre.get()
        edad_text = self.edad.get()
        dni_text = self.dni.get ()
        validacion_dni=len(dni_text)
        #Validaciones
        nombre_edad_dni_requerido = (nombre_obtenido.isspace() or nombre_obtenido == "") and (edad_text.isspace() or edad_text == "") and (dni_text.isspace() or dni_text== "")
        nombre_requerido = (nombre_obtenido == "" and edad_text!="" and dni_text!= "") or (not nombre_obtenido.istitle())
        edad_requerido = (not nombre_obtenido.isspace() and edad_text.isspace()) or (nombre_obtenido != "" and edad_text == "") or (nombre_obtenido != "" and edad_text<=str (17) or edad_text< str (100)) or (not edad_text.isdigit())
        dni_requerido = (dni_text.isspace() and not edad_text.isspace() and not nombre_obtenido.isspace()) or (nombre_obtenido!="" and edad_text!="" and dni_text=="") or (not dni_text.isdigit()) or (validacion_dni< 8 )
        #Mensajes de error según las validaciones
        mensaje = "Ingresar nombre, apellido, edad y DNI" if nombre_edad_dni_requerido else "Debe ingresar nombre y apellido (Revisar datos ingresados, recordar que nombre y apellido debe comenzar con máyusculas" if nombre_requerido else "Debe ingresar edad o ingresar edad correcta (Mayor a 18 años / Menor de 100 años)" if edad_requerido else "Debe ingresar D.N.I. caso contrario revisar datos ingresados(Solo números)" if dni_requerido else None
        #If para mostrar el error o la acción exitosa
        if mensaje:
            showerror("Campos requeridos", mensaje, parent=self)
        else:
            showinfo("Acción exitosa", "Los datos se han guardado correctamente", parent=self)
            contadores(1,edad_text)
            self.destroy()    

#Definición del class de bajas:
class bajas (Toplevel):
    #Se define las caracteristicas de la ventana, junto con los datos a ingresar:
    def __init__(self,master = None):
        super().__init__(master = master)
        self.title("bajas de usuario")
        self.resizable(0,0)
        self.grab_set()

        #variables:
        nombre = ""
        motivo = ""

        #Ingreso de los nombres
        self.nombre = Label(self, text="Nombre y apellido: ")
        self.nombre.pack(side="left")
        self.nombre = Entry(self)
        self.nombre.pack(side="left") 

        #Ingreso de motivo de baja:
        self.motivo = Label(self, text="Motivo de la baja")
        self.motivo.pack(side="left")
        self.motivo = Entry(self)
        self.motivo.pack(side="left") 

        #Botón de guardado
        self.button_guardar = Button(self, text="Guardar", command=self.actualizar_datos)
        self.button_guardar.pack(side="left")

        #Botón de cancelado
        self.button_cancelar = Button(self, text="Cancelar", command=self.destroy)
        self.button_cancelar.pack(side="left")

    def actualizar_datos(self):
        nombre_obtenido = self.nombre.get()
        motivo_obtenido = self.motivo.get()

        #Validaciones:
        nombre_motivo_requerido=(nombre_obtenido.isspace() and motivo_obtenido.isspace()) or (nombre_obtenido=="" and motivo_obtenido=="" )
        nombre_requerido=(nombre_obtenido=="" and motivo_obtenido!="") or (not nombre_obtenido.istitle())
        motivo_requerido=(nombre_obtenido!="" and motivo_obtenido=="") or (not motivo_obtenido.islower())

        #mensaje
        mensaje="Ingresar nombre, apellido y motivo de baja" if nombre_motivo_requerido else "Debe ingresar nombre y apellido (Revisar datos ingresados, recordar que nombre y apellido debe comenzar con máyusculas" if nombre_requerido else "Ingresar motivo de baja, caso contrario revise datos ingresados" if motivo_requerido else None

        #If para mostrar el error o la acción exitosa
        if mensaje:
            showerror("Campos requeridos", mensaje, parent=self)
        else:
            showinfo("Acción exitosa", "Los datos se han guardado correctamente", parent=self)
            contadores(2,0)
            self.destroy()    

#Contador de trabajadores dados de Alta o baja
min_edad=[30]
max_edad=[30]
min_final=int(0)
max_final=int(0)
reporte2=str("")

def contadores(number,age):
    global reporte2
    if number == 1:
        lista_altas.append(1)
        if int(age)>=30:
            max_edad.append(int(age))
        else:
            if int(age)<=30:
                min_edad.append(int(age))

        min_final=min(min_edad)
        max_final=max(max_edad)
        reporte2="\nTrabajador de mayor edad: "+ str(max_final)+"\nTrabajador de menor edad: "+str(min_final)
    elif number == 2:
        lista_bajas.append(1)
    elif number == 3:
        suma_altas=sum(lista_altas)
        suma_bajas=sum(lista_bajas)
        reporte="Cantidad de altas cargadas: "+ str(suma_altas)+"\nCantidad de bajas cargadas: "+str(suma_bajas)+str(reporte2)
        showinfo("Reporte diario", reporte)

#Botones a utilizar por el usuario:
#Altas:
alta= Button(master, text="Alta")
alta.pack(side=TOP)
alta.bind("<Button>", lambda e: altas(master))
alta.pack(pady = 15)

#Bajas:
baja = Button(master, text="Baja")
baja.pack(side=TOP)
baja.bind("<Button>", lambda e: bajas(master))
baja.pack(pady = 15)

#Reportes:
reporte= Button(master, text="Reportes")
reporte.pack(side=TOP)
reporte.bind("<Button>", lambda e: contadores(3,0))
reporte.pack(pady=15)

#Salida del programa
boton4 = Button(master, text="Salir", command=master.quit)
boton4.pack(pady=15)

mainloop()