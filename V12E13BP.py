import sys
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QApplication, QLabel, QLineEdit, QPushButton, QGroupBox, QVBoxLayout, QRadioButton, QMessageBox
from V12E13BP import Pregunta

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test de adicción a los videojuegos")

        self.index = 0
        self.respuestas = []
        self.crearCuestionario()
        self.maximo = len(self.cuestionario)

        self.lb_num_pregunta = QLabel(str(self.cuestionario[self.index].num_pregunta))
        self.lb_texto = QLabel(self.cuestionario[self.index].texto)
        self.btn_siguiente = QPushButton("Siguiente")

        self.grupo = QGroupBox("Seleccione una opción")
        vbox = QVBoxLayout()
        self.nunca = QRadioButton("Nunca")
        self.aveces = QRadioButton("A veces")
        self.frec = QRadioButton("Frecuentemente")
        self.siempre = QRadioButton("Siempre")
        vbox.addWidget(self.nunca)
        vbox.addWidget(self.aveces)
        vbox.addWidget(self.frec)
        vbox.addWidget(self.siempre)
        self.grupo.setLayout(vbox)

        layout = QGridLayout()
        layout.addWidget(self.lb_num_pregunta, 0, 0)
        layout.addWidget(self.lb_texto, 1, 0)
        layout.addWidget(self.grupo, 2, 0)
        layout.addWidget(self.btn_siguiente, 3, 0)

        self.btn_siguiente.clicked.connect(self.siguiente)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def crearCuestionario(self):
        # Creación de objetos pregunta
        pregunta1 = Pregunta(1, "¿Pasas mucho tiempo a la semana al jugar videojuegos?")
        pregunta2 = Pregunta(2, "¿Te sientes ansioso o irritado cuando no puedes jugar?")
        pregunta3 = Pregunta(3, "¿Has descuidado actividades importantes, como trabajo, escuela o relaciones sociales para jugar?")
        pregunta4 = Pregunta(4, "¿Te sientes culpable o avergonzado por la cantidad de tiempo que pasas jugando?")
        pregunta5 = Pregunta(5, "¿Has intentado reducir o controlar el tiempo que pasas jugando, pero no has podido?")
        pregunta6 = Pregunta(6, "¿Te sientes estresado o abrumado cuando no estas jugando?")
        pregunta7 = Pregunta(7, "¿Has experimentado problemas de sueño o fatiga debido a la cantidad de tiempo que pasas jugando?")
        pregunta8 = Pregunta(8, "¿Has perdido interés en actividades que antes disfrutabas debido a los videojuegos?")
        pregunta9 = Pregunta(9, "¿Te sientes mas cómodo jugando que interactuando con personas en la vida real?")
        pregunta10 = Pregunta(10, "¿Has mentido sobre la cantidad de tiempo que pasas jugando a amigos o familiares?")

        self.cuestionario = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10]

    def siguiente(self):
        if self.verifica_respuesta() != -1:
            if self.index < self.maximo - 1:
                self.index += 1
                self.lb_num_pregunta.setText(str(self.cuestionario[self.index].num_pregunta))
                self.lb_texto.setText(self.cuestionario[self.index].texto)
                self.nunca.setChecked(False)
                self.aveces.setChecked(False)
                self.frec.setChecked(False)
                self.siempre.setChecked(False)
            else:
                QMessageBox.information(self, "Fin del test", "Gracias por completar el test")
                self.close()

    def verifica_respuesta(self):
        if self.nunca.isChecked():
            self.respuestas.append(0)
            return 0
        elif self.aveces.isChecked():
            self.respuestas.append(1)
            return 1
        elif self.frec.isChecked():
            self.respuestas.append(2)
            return 2
        elif self.siempre.isChecked():
            self.respuestas.append(3)
            return 3
        else:
            QMessageBox.warning(self, "Error", "Seleccione una opción")
            return -1

app = QApplication(sys.argv)
window = Principal()
window.show()
sys.exit(app.exec_())