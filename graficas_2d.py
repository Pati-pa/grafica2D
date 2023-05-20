from tkinter import *
from tkinter import messagebox
import random
base=460  
altura = 220

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

#graficación

for i in range(10):
    x = random.randint(0, base-20)
    y = random.randint(0,altura-20)
    color = "#"
    for caracter in range(6):
        color = color + random.choice("123456789ABCDEF")
    circulo = c.create_oval(x,y,x+20, y+20 , fill=color)

ventana_principal.mainloop()