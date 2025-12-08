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
        layout= QGridLayout()
        etiqueta2= QLabel("Test")
        layout.addWidget(etiqueta2,0,0)
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

app= QApplication(sys.argv)
window=Principal()
window.show()
sys.exit(app.exec_())