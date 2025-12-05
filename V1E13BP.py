import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("esta es mi primera ventana")
ventana.geometry("300x400")

ttk.Label(ventana, text="APLICA METODOLOGIAS AGILES PARA EL DESARROLLO DE SOFTWARE").grid(column=0, row=1)
ttk.Label(ventana, text="EQUIPO1").grid(column=0, row=2)
ttk.Label(ventana, text="DAFNE").grid(column=0, row=3)

ventana.resizable(0,0)
ventana.mainloop()