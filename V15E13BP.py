import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np

# Datos de las preguntas y respuestas
preguntas = [
    {"pregunta": "1.¿Dedicas mucho tiempo a la semana al jugar videojuegos?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "2.¿Te sientes ansioso o irritado cuando no puedes jugar?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "3.¿Has descuidado actividades importantes, como trabajo, escuela o relaciones sociales para jugar?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "4.¿Te sientes culpable o avergonzado por la cantidad de tiempo que pasas jugando?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "5.¿Has intentado reducir o controlar el tiempo que pasas jugando, pero no has podido?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "6.¿Te sientes estresado o abrumado cuando no estas jugando?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "7.¿Has experimentado problemas de sueño o fatiga debido a la cantidad de tiempo que pasas jugando?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "8.¿Has perdido interés en actividades que antes disfrutabas debido a los videojuegos?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "9.¿Te sientes mas cómodo jugando que interactuando con personas en la vida real?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
    {"pregunta": "10.¿Has mentido sobre la cantidad de tiempo que pasas jugando a amigos o familiares?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
]

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfica de respuestas")
        self.setGeometry(100, 100, 800, 600)

        # Crear una lista para almacenar las respuestas
        self.respuestas = [0] * len(preguntas)

        # Crear un widget para la gráfica
        self.plot = pg.PlotWidget()

        # Crear un gráfico de barras
        self.bar = pg.BarGraphItem(x=np.arange(1, len(preguntas)+1), height=self.respuestas, width=0.6, brush='b')
        self.plot.addItem(self.bar)
        self.plot.setXRange(1, len(preguntas)+1)

        # Crear un formulario para ingresar las respuestas
        self.formulario = pg.QtWidgets.QFormLayout()
        for i, pregunta in enumerate(preguntas):
            label = pg.QtWidgets.QLabel(pregunta["pregunta"])
            combo = pg.QtWidgets.QComboBox()
            combo.addItems(pregunta["respuestas"])
            combo.currentIndexChanged.connect(lambda index, i=i: self.actualizar_respuesta(i, index))
            self.formulario.addRow(label, combo)

        # Agregar el formulario al formulario principal
        self.layout = pg.QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.formulario)
        self.layout.addWidget(self.plot)

        # Crear un widget para el formulario principal
        self.widget = pg.QtWidgets.QWidget()
        self.widget.setLayout(self.layout)

        # Agregar el widget al formulario principal
        self.setCentralWidget(self.widget)

    def actualizar_respuesta(self, i, index):
        self.respuestas[i] = index
        self.bar.setOpts(height=self.respuestas)
        self.plot.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())