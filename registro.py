# registro.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaRegistro(QWidget):
    usuario_registrado = pyqtSignal()
    volver_login = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 20, 50, 20)
        layout.setSpacing(15)

        titulo = QLabel("CREAR CUENTA")
        titulo.setProperty("class", "TituloLogin") # Reutilizamos el estilo amarillo
        titulo.setAlignment(Qt.AlignCenter)

        self.nuevo_user = QLineEdit()
        self.nuevo_user.setPlaceholderText("Elige un nombre de usuario")

        self.nueva_pass = QLineEdit()
        self.nueva_pass.setPlaceholderText("Crea una contraseña")
        self.nueva_pass.setEchoMode(QLineEdit.Password)

        btn_registrar = QPushButton("REGISTRARSE")
        btn_registrar.clicked.connect(self.finalizar_registro)

        btn_volver = QPushButton("Volver al Login")
        btn_volver.setProperty("class", "BotonEnlace")
        btn_volver.clicked.connect(self.volver_login.emit)

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(self.nuevo_user)
        layout.addWidget(self.nueva_pass)
        layout.addWidget(btn_registrar)
        layout.addWidget(btn_volver)
        layout.addStretch()

        self.setLayout(layout)

    def finalizar_registro(self):
        if self.nuevo_user.text() != "" and self.nueva_pass.text() != "":
            # Aquí podrías guardar los datos en un archivo o base de datos
            print(f"Usuario {self.nuevo_user.text()} registrado con éxito")
            self.usuario_registrado.emit()
        else:
            print("Error: Campos vacíos")