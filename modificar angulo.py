from tkinter import *
from tkinter import messagebox
import random
base=460  
altura = 220
radio= 50

#funcion para modificar angulo
def modificar(angulo):
    c.itemconfig(arco, extent=angulo)
    
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
arco = c.create_arc(base/2 - radio, altura/2 - radio, base/2 + radio, altura/2 + radio, start=0, extent=0, fill="white", )
#frame de controles
frame_controles  = Frame(ventana_principal)
frame_controles.config(bg="cyan" , width=480, height=230)
frame_controles.place(x=10, y=270)

#barra deslizamiento
barra_deslizamiento = Scale(frame_controles, label="Angulo", from_=0, to=360, orient="horizontal", length=450, tickinterval= 90, command=modificar)
barra_deslizamiento.place(x=10, y=10)
ventana_principal.mainloop()