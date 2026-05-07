# login.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaLogin(QWidget):
    login_exitoso = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        titulo = QLabel("Bienvenido a la Pizzería")
        titulo.setAlignment(Qt.AlignCenter)
        
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuario (ej. amilcar)")
        
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Contraseña")
        self.pass_input.setEchoMode(QLineEdit.Password)

        btn_login = QPushButton("Ingresar")
        btn_login.clicked.connect(self.verificar_login)

        self.mensaje_error = QLabel("")
        self.mensaje_error.setProperty("class", "ErrorLabel")
        self.mensaje_error.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_input)
        layout.addWidget(btn_login)
        layout.addWidget(self.mensaje_error)
        layout.addStretch()

        self.setLayout(layout)

    def verificar_login(self):
        # Lógica simple de login
        if self.user_input.text() != "" and self.pass_input.text() != "":
            self.mensaje_error.setText("")
            self.login_exitoso.emit()
        else:
            self.mensaje_error.setText("Por favor, ingresa los datos.")