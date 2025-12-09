# importar las librerias
import tkinter as tk
def mostrar_ventana2():
    ventana1.withdraw() # esta funcion sirve para que oculte la ventana 1
    ventana2.deiconify() # muestre la ventana 2
def regresar():
    ventana2.withdraw()
    ventana1.deiconify()

# creacion de ventana 1
ventana1 = tk.Tk()
label1= tk.Label(ventana1, text="Esta es la ventana número 1")
ventana1.geometry("600x400")
label1.pack()
btn1= tk.Button(ventana1, text="ir a la ventana 2", command= mostrar_ventana2)
btn1.pack()
ventana1.configure(bg="#F8933A")
titulo = tk.Label(
    ventana1,
    text="hola!!! bienvenido a esta ventana ",
    font=("BBH Sans Bogle",18,"bold"),
    bg="#ECE109",
    fg="#151516",
    wraplength=550,
    justify="center"
    )
titulo.pack(pady=30)

# creacion de ventana 2
ventana2 = tk.Tk()
label2= tk.Label(ventana2, text="Esta es la ventana número 2")
ventana2.geometry("300x300")
label2.pack()
btn2= tk.Button(ventana2, text="ir a la ventana numero 1", command= regresar )
btn2.pack()
ventana2.configure(bg="#008F09")
titulo = tk.Label(
    ventana2,
    text="gracias por visitarnos :) ",
    font=("BBH Sans Bogle",18,"bold"),
    bg="#008CAEC",
    fg="#151516",
    wraplength=550,
    justify="center"
    )
titulo.pack(pady=30)
ventana2.withdraw()


#creacion de ventanas (lanzar la interfaz)
ventana1.mainloop()