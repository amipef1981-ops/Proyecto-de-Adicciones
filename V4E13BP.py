import tkinter as tk
from tkinter import ttk

#configuracion de colores 
COLOR_FONDO="#06D0EA"
COLOR_MENU="#06ED4F"
COLOR_TEXTO="#FDFCFC"
FUENTE_TITULO=("Arial",16,"bold")
FUENTE_TEXTO=("Arial",12)

  #ventana prinipal
root= tk.Tk ()
root.title("Bienestar Total")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

#frame del menu lateral
menu_frame= tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left",fill="y")

#contenido del frame
contenido_frame=tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# definir las funciones cambiar pagina

def mostrar_pagina(nombre):  
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# ventana de bienvenida 
def pagina_bienvenida():
    tk.Label(contenido_frame, text="🚑 Bienvenido al software de deteccion de adicciones a la tecnologia", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="Te ofrecemos informacion y ayuda", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, text="📝 Registro de usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    for campo in ["Nombre", "Edad", "Correo"]:
        tk.Label(contenido_frame, text=f"{campo}", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5)
 
def pagina_test():
    tk.Label(contenido_frame, text="🧠 Test de Bienestar", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Responde las siguientes preguntas para ver si tienes una adiccion.", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="Iniciar Test").pack(pady=20)

def pagina_resultados():
    tk.Label(contenido_frame, text="Resultados generales", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Estos son tus resultados finales", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="Siguiente").pack(pady=20)

def pagina_sintomas_señales():
    tk.Label(contenido_frame, text="Sintomas y Señales", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Sintomas", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    tk.Label(contenido_frame, text="Señales", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="Siguiente").pack(pady=20)

def pagina_historias_inspiradoras():
    tk.Label(contenido_frame, text="Historias Inspiradoras", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Te presentamos algunas historias para poder motivarte", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="Siguiente").pack(pady=20)

def pagina_ayuda():
    tk.Label(contenido_frame, text="Ayuda", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Te presentamos numeros, paginas web y mas...", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="Siguiente").pack(pady=20)


#diccionario de paginas
paginas ={
    "Bienvenida":pagina_bienvenida,
    "Registro":pagina_registro,
    "Test":pagina_test,
    "Resultados":pagina_resultados,
    "Sintomas y Señales":pagina_sintomas_señales,
    "Historias Inspiradoras":pagina_historias_inspiradoras,
    "Ayuda":pagina_ayuda,
    
}

#botones del menu lateral

for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="salir", command=root.quit).pack(side="bottom", pady=10)

#mostrar ventana
pagina_bienvenida()

root.mainloop()