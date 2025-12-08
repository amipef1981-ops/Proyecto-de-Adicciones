import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import V11E13BP

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro")

        self.lb_num_control = QLabel("Num_Control")
        self.lb_alumno = QLabel("Alumno")
        self.lb_semestre = QLabel("Semestre")
        self.lb_grupo = QLabel("Grupo")
        self.txt_num_control = QLineEdit()
        self.txt_alumno = QLineEdit()
        self.txt_semestre = QLineEdit()
        self.txt_grupo = QLineEdit()
        self.btn_registrar = QPushButton("Registrar")

        layout = QGridLayout()
        layout.addWidget(self.lb_num_control, 0, 0)
        layout.addWidget(self.txt_num_control, 0, 1)
        layout.addWidget(self.lb_alumno, 1, 0)
        layout.addWidget(self.txt_alumno, 1, 1)
        layout.addWidget(self.lb_semestre, 2, 0)
        layout.addWidget(self.txt_semestre, 2, 1)
        layout.addWidget(self.lb_grupo, 3, 0)
        layout.addWidget(self.txt_grupo, 3, 1)
        layout.addWidget(self.btn_registrar, 4, 1)

        self.btn_registrar.clicked.connect(self.registrar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def registrar(self):
        num_control = self.txt_num_control.text()
        alumno = self.txt_alumno.text()
        semestre = self.txt_semestre.text()
        grupo = self.txt_grupo.text()

        if not num_control or not alumno or not semestre or not grupo:
            QMessageBox.warning(self, "Error", "Por favor, llena todos los campos")
            return

        try:
            num_control = int(num_control)
        except ValueError:
            QMessageBox.warning(self, "Error", "El número de control debe ser un número entero")
            return

        # Crea un objeto Alumno con los datos ingresados
        alumno_obj = V11E13BP.Alumno(num_control, alumno, semestre, grupo)

        # Aquí puedes agregar código para guardar el alumno en una base de datos o archivo
        QMessageBox.information(self, "Éxito", "Alumno registrado con éxito")

app = QApplication(sys.argv)
window = Principal()
window.show()
sys.exit(app.exec_())
   