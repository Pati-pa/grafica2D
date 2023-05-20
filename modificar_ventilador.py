from tkinter import *
from tkinter import messagebox
import random
base=460  
altura = 220
radio= 50

#funcion para modificar angulo
def modificar(angulo): 
    angulo1 = int(angulo)+90
    angulo2 = int(angulo) +180
    angulo3 = int(angulo) + 270
    c.itemconfig(arco, start= angulo)
    c.itemconfig(arco1,start= angulo1)
    c.itemconfig(arco2,start= angulo2)
    c.itemconfig(arco3,start= angulo3)
ventana_principal = Tk()
ventana_principal.title("Grafica 2D")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="aquamarine2")
frame_grafica = Frame(ventana_principal)
frame_grafica.config(bg="green", width=480, height=250)
frame_grafica.place(x=10, y=10)

#Creación de canvas
c= Canvas(frame_grafica, width=base, height=altura)
c.config(bg="black")
c.place(x=10, y=10)
#arco
arco = c.create_arc(base/2 - radio, altura/2 - radio, base/2 + radio, altura/2 + radio, start=45, extent=45, fill="white" )
arco1 = c.create_arc(base/2 - radio, altura/2 - radio, base/2 + radio, altura/2 + radio, start=135, extent=45, fill="green")
arco2 = c.create_arc(base/2 - radio, altura/2 - radio, base/2 + radio, altura/2 + radio, start=225, extent=45, fill="blue")
arco3 = c.create_arc(base/2 - radio, altura/2 - radio, base/2 + radio, altura/2 + radio, start=315, extent=45, fill="cyan")
#Crear triangulo
tri= c.create_polygon(base/2,altura/2, base/2 -20, altura - 20, base/2 + 20,altura -20, fill="white", width="10")
#frame de controles
frame_controles  = Frame(ventana_principal)
frame_controles.config(bg="cyan" , width=480, height=230)
frame_controles.place(x=10, y=270)

#barra deslizamiento
barra_deslizamiento = Scale(frame_controles, label="Angulo", from_=0, to=360, orient="horizontal", length=450, tickinterval= 45, command=modificar)
barra_deslizamiento.place(x=10, y=10)
ventana_principal.mainloop()