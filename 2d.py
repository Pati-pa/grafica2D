from tkinter import *
from tkinter import messagebox

base=460  
altura = 220

ventana_principal = Tk()
ventana_principal.title("Grafica 2D")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="aquamarine2")
frame_grafica = Frame(ventana_principal)
frame_grafica.config(bg="white", width=480, height=250)
frame_grafica.place(x=10, y=10)

#Creación de canvas
c= Canvas(frame_grafica, width=base, height=altura)
c.place(x=10, y=10)

#Lineas
"""linea1 = c.create_line(10,10, base - 10, 10, fill="red")
linea2 = c.create_line(base-10,10, base - 10,altura- 10, fill="red")
linea3 = c.create_line(10,altura -10, base- 10,altura- 10, fill="red")
linea4 = c.create_line(10,altura - 10, 10,10, fill="red")


linea7 = c.create_line(200,30, base - 150, 30, fill="red")
linea8 = c.create_line(base-150,30, base - 150,altura- 150, fill="red")
linea9= c.create_line(base-150,altura - 150, base- 100,altura- 150, fill="red")

texto1= c.create_text(base/2, altura/2, text="Hola baby", anchor="center", fill="green" , activefill="cyan", 
font=("Times new roman", "20", "bold"))

rect1= c.create_rectangle(30,30, 100,100, fill="blue", outline="green", width="10")
ventana_principal.mainloop()

poligono1 = c.create_polygon(0,0,base/2,altura/2,base, 0, fill="red", outline="blue")
poligono2 =c.create_polygon(0,altura,base/2,altura/2,base, altura, fill="green")
poligono3 =c.create_polygon(0,0,base/2,altura/2,0, altura, fill="khaki")

poligono1 = c.create_polygon((base/2)/2,0,base/2,(altura/2)/2,(base/2)/2,altura/2,0,(altura/2)/2, fill="cyan", outline="green")
poligono1 = c.create_polygon((base/4)*3,0,base,(altura/2)/2,(base/4)*3,altura/2,base/2,(altura/2)/2, fill="cyan", outline="green")
poligono1 = c.create_polygon((base/2)/2,altura/2,base/2,(altura/4)*3,(base/2)/2,altura,0,(altura/4)*3, fill="cyan", outline="green")
poligono1 = c.create_polygon((base/4)*3,altura/2,base,(altura/4)*3,(base/4)*3,altura,base/2,(altura/4)*3, fill="cyan", outline="green")"""
#poligono2 = c.create_polygon(base/2,altura/2,0,altura/2,120,altura, fill="red", outline="blue")

#elipse1= c.create_oval((base/2) -100, (altura/2)-100, (base/2) + 100,(altura/2) +100,  fill="orange")
arc1 = c.create_arc((base/2/2) +30 ,(altura/2) +30 , (base/2) -30 ,((altura/2)/2) -30,start= 45, extent= 280 ,fill="black" )
arc2 = c.create_arc((base/2)/2 -30, (altura/2) -30, (base/2) +30,(altura/4)*3 +30,start= 45, extent=300  ,fill="black" )
arc3 = c.create_arc((base/2) +30, altura/2 +30, (base/4)*3-30 ,(altura/2)/2-30 ,start= 45, extent=300  ,fill="blue" )
arc4 = c.create_arc((base/4)*3 -25, altura/2 -25, (base/2)+30 ,(altura/4)*3 +30,start= 45, extent=300  ,fill="green" )
ventana_principal.mainloop()