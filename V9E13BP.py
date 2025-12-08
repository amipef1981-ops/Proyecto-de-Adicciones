class Pregunta: 
    def __init__(self, num_pregunta, texto, respuesta=None):
        self.num_pregunta = num_pregunta
        self.texto = texto
        self.respuesta = respuesta

opciones_respuesta = {
    0: "Nunca",
    1: "A veces",
    2: "Frecuentemente",
    3: "Siempre"
}

pregunta1 = Pregunta(1, "¿Juegas videojuegos más del tiempo que te gustaría?")
pregunta2 = Pregunta(2, "¿Te sientes ansioso o irritable cuando no puedes jugar videojuegos?")
pregunta3 = Pregunta(3, "¿Has descuidado tus responsabilidades (trabajo, escuela, familia) por jugar videojuegos?")
pregunta4 = Pregunta(4, "¿Te sientes culpable o avergonzado por el tiempo que pasas jugando videojuegos?")

cuestionario = [pregunta1, pregunta2, pregunta3, pregunta4]

# Para agregar respuestas a las preguntas
for pregunta in cuestionario:
    print(f"Pregunta {pregunta.num_pregunta}: {pregunta.texto}")
    print("Opciones de respuesta:") 
    for clave, valor in opciones_respuesta.items():
        print(f"{clave}: {valor}")
    while True:
        try:
            respuesta = int(input("Ingrese el número de su respuesta (0-3): "))
            if 0 <= respuesta <= 3:
                pregunta.respuesta = opciones_respuesta[respuesta]
                break
            else:
                print("Por favor, ingrese un número entre 0 y 3.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Para mostrar las respuestas
for pregunta in cuestionario:
    print(f"Pregunta {pregunta.num_pregunta}: {pregunta.texto} - Respuesta: {pregunta.respuesta}")