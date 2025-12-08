import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QTabWidget, QPushButton, QMessageBox, QMenuBar, QPlainTextEdit, QStackedWidget, QVBoxLayout, QAction, QLineEdit
from PyQt5.QtCore import *

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(100,100,400,300)
        self.tabs=QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tab_registro=QWidget()
        self.tab_test=QWidget()
        self.tab_rest=QWidget()
        self.tabs.addTab(self.tab_registro,"Registro")
        self.tabs.addTab(self.tab_test,"Test")
        self.tabs.addTab(self.tab_rest,"Resultados")
        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()

    def crear_pestana_registro(self):
        layout = QGridLayout()
        self.lb_num_control = QLabel("Num_Control")
        self.txt_num_control = QLineEdit()
        self.lb_alumno = QLabel("Alumno")
        self.txt_alumno = QLineEdit()
        self.lb_semestre = QLabel("Semestre")
        self.txt_semestre = QLineEdit()
        self.lb_grupo = QLabel("Grupo")
        self.txt_grupo = QLineEdit()
        self.btn_registrar = QPushButton("Registrar")
        layout.addWidget(self.lb_num_control,0,0)
        layout.addWidget(self.txt_num_control,0,1)
        layout.addWidget(self.lb_alumno,1,0)
        layout.addWidget(self.txt_alumno,1,1)
        layout.addWidget(self.lb_semestre,2,0)
        layout.addWidget(self.txt_semestre,2,1)
        layout.addWidget(self.lb_grupo,3,0)
        layout.addWidget(self.txt_grupo,3,1)
        layout.addWidget(self.btn_registrar,4,1)
        self.btn_registrar.clicked.connect(self.registrar)
        self.tab_registro.setLayout(layout)

    def crear_pestana_test(self):
        layout = QGridLayout()
        self.preguntas = [
           {"pregunta": "1.¿Dedicas mucho tiempo a la semana al jugar videojuegos?", "respuestas": ["", "Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "2.¿Te sientes ansioso o irritado cuando no puedes jugar?", "respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "3.¿Has descuidado actividades importantes, como trabajo, escuela o relaciones sociales para jugar?", "respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "4.¿Te sientes culpable o avergonzado por la cantidad de tiempo que pasas jugando?","respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "5.¿Has intentado reducir o controlar el tiempo que pasas jugando, pero no has podido?", "respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "6.¿Te sientes estresado o abrumado cuando no estas jugando?", "respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "7.¿Has experimentado problemas de sueño o fatiga debido a la cantidad de tiempo que pasas jugando?", "respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "8.¿Has perdido interés en actividades que antes disfrutabas debido a los videojuegos?", "respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "9.¿Te sientes mas cómodo jugando que interactuando con personas en la vida real?", "respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
            {"pregunta": "10.¿Has mentido sobre la cantidad de tiempo que pasas jugando a amigos o familiares?", "respuestas": ["Nunca", "A veces", "Frecuentemente", "Siempre"]},
        ]
        self.index_pregunta = 0
        self.lb_pregunta = QLabel(self.preguntas[self.index_pregunta]["pregunta"])
        self.btn_respuesta1 = QPushButton(self.preguntas[self.index_pregunta]["respuestas"][1])
        self.btn_respuesta2 = QPushButton(self.preguntas[self.index_pregunta]["respuestas"][2])
        self.btn_respuesta3 = QPushButton(self.preguntas[self.index_pregunta]["respuestas"][3])
        self.btn_respuesta4 = QPushButton(self.preguntas[self.index_pregunta]["respuestas"][4])
        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_respuestas = [self.btn_respuesta1, self.btn_respuesta2, self.btn_respuesta3, self.btn_respuesta4]

        layout.addWidget(self.lb_pregunta, 0, 0, 1, 4)
        layout.addWidget(self.btn_respuesta1, 1, 0)
        layout.addWidget(self.btn_respuesta2, 1, 1)
        layout.addWidget(self.btn_respuesta3, 1, 2)
        layout.addWidget(self.btn_respuesta4, 1, 3)
        layout.addWidget(self.btn_siguiente, 2, 0, 1, 4)

        self.btn_respuesta1.clicked.connect(lambda: self.seleccionar_respuesta(self.btn_respuesta1))
        self.btn_respuesta2.clicked.connect(lambda: self.seleccionar_respuesta(self.btn_respuesta2))
        self.btn_respuesta3.clicked.connect(lambda: self.seleccionar_respuesta(self.btn_respuesta3))
        self.btn_respuesta4.clicked.connect(lambda: self.seleccionar_respuesta(self.btn_respuesta4))
        self.btn_siguiente.clicked.connect(self.siguiente_pregunta)

        self.tab_test.setLayout(layout)

    def crear_pestana_resultados(self):
        layout= QGridLayout()
        etiqueta3= QLabel("Resultados")
        layout.addWidget(etiqueta3,0,0)
        self.tab_rest.setLayout(layout)

    def registrar(self):
        num_control = self.txt_num_control.text()
        alumno = self.txt_alumno.text()
        semestre = self.txt_semestre.text()
        grupo = self.txt_grupo.text()
        # Aquí puedes agregar código para guardar los datos en una base de datos o archivo
        QMessageBox.information(self, "Éxito", "Registro exitoso")

    def seleccionar_respuesta(self, btn):
        for b in self.btn_respuestas:
            b.setStyleSheet("")
        btn.setStyleSheet("background-color: blue; color: white")

    def siguiente_pregunta(self):
        self.index_pregunta += 1
        if self.index_pregunta < len(self.preguntas):
            self.lb_pregunta.setText(self.preguntas[self.index_pregunta]["pregunta"])
            self.btn_respuesta1.setText(self.preguntas[self.index_pregunta]["respuestas"][0])
            self.btn_respuesta2.setText(self.preguntas[self.index_pregunta]["respuestas"][1])
            self.btn_respuesta3.setText(self.preguntas[self.index_pregunta]["respuestas"][2])
            self.btn_respuesta4.setText(self.preguntas[self.index_pregunta]["respuestas"][3])
            for b in self.btn_respuestas:
                b.setStyleSheet("")
        else:
            QMessageBox.information(self, "Fin del test", "Se han terminado las preguntas")
            self.btn_siguiente.setEnabled(False)
            self.btn_respuesta1.setEnabled(False)
            self.btn_respuesta2.setEnabled(False)
            self.btn_respuesta3.setEnabled(False)
            self.btn_respuesta4.setEnabled(False)

app= QApplication(sys.argv)
window=Principal()
window.show()
sys.exit(app.exec_())