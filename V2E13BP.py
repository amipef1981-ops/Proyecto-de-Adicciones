import tkinter as tk   #importamos las librerias necesarias 
from tkinter import messagebox 
from tkinter import PhotoImage 

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
#funcion que se ejecuta al presionar el boton "Iniciar Test"
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
def iniciar_test():

    messagebox.showinfo("inicio del test", "Bienvenido al Test de Deteccion de Adicciones.\n\nPresiona OK para continuar.")
    ventanabienv.destroy()   # Cierra la pantalla de bienvenida (puedes cambiarlo por abrir otra ventana)


#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
#configuracion de la ventana principal
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
ventanabienv=tk.Tk()
ventanabienv.title("Test de Deteccion de Adicciones")
ventanabienv.geometry("600x400")
ventanabienv.configure(bg="#22098F")   # Color de fondo


# Centrar la ventana en pantalla
ancho_pantalla = ventanabienv.winfo_screenwidth()
alto_pantalla = ventanabienv.winfo_screenheight()
x = (ancho_pantalla // 2) - (600 // 2)
y = (alto_pantalla // 2) - (400 // 2)
ventanabienv.geometry(f"700x450+{x}+{y}")

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
#Elementos graficos
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Titulo principal
titulo =tk.Label(
    ventanabienv, 
    text="Bienvenido al Test de Deteccion de Adicciones ",
    font=("BBH Sans Bogle",18,"bold"),
    bg="#09CAEC",
    fg= "#151516",
    wraplength=550,
    justify= "center"
    )
titulo.pack(pady=30)

#imagen opcional (asegurate de tener una imagen en la misma carpeta)
try:
    imagen=PhotoImage(file= "adiccion.png") #remplaza por el nombre de tu imagen
    img_label=tk.Label(ventanabienv, image=imagen, bg= "#9611D8")
    img_label.pack(pady=10)
except Exception:
    aviso = tk. Label(ventanabienv, text="(no se encontro la imagen'salud.jpg')", bg="#5D5A5A", fg="gray" )
    aviso.pack()
    
#texto descriptivo
texto =tk.Label(
    ventanabienv,
    text=(
        "Este test tiene como objetivo detectar posibles indicadores de conductas adictivas.\n"
        "Responde con sinceridad a las preguntas que se te presentaran a continuacion.\n\n"
        "Tus respuestas seran confidenciales."
),
font=("BBH Sans Bogle",12),
bg="#656363",
fg="#424242",
wraplength=500,
justify="center",
)
texto.pack(pady=20)

#Boton para iniciar el test
boton_iniciar = tk.Button(
ventanabienv,
text="Iniciar Test",
font=("BBH Sans Bogle",14,"bold"),
bg= "#45BDF0",
fg="white",
relief="raised",
bd=3,
padx=20,
pady=10,
command= iniciar_test
)
boton_iniciar.pack(pady=20)

#ejecutar la interfaz
ventanabienv.mainloop()