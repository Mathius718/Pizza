# login.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from archivos import *
class VentanaLogin(QWidget):
    login_exitoso = pyqtSignal()
    ir_a_registro_signal = pyqtSignal() 

    def __init__(self):
        super().__init__()
        # Layout principal con espaciado elegante
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 20, 50, 20)
        layout.setSpacing(15)

        # 1. Título llamativo (Corregido a "Deliciosa")
        # Usamos <br> para que el nombre se vea grande y centrado en dos líneas
        self.titulo = QLabel("THE PIZZA LAB")
        self.titulo.setProperty("class", "TituloLogin")
        self.titulo.setAlignment(Qt.AlignCenter)
        
        # 2. Campos de entrada
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Nombre de usuario")
        
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Contraseña")
        self.pass_input.setEchoMode(QLineEdit.Password)

        # 3. Botón de Ingreso
        self.btn_login = QPushButton("INGRESAR")
        self.btn_login.setCursor(Qt.PointingHandCursor)
        self.btn_login.clicked.connect(self.verificar_login)

        # 4. Etiqueta para mensajes de error
        self.mensaje_error = QLabel("")
        self.mensaje_error.setProperty("class", "ErrorLabel")
        self.mensaje_error.setAlignment(Qt.AlignCenter)

        # 5. SECCIÓN INFERIOR: Crear nuevo usuario
        layout_registro = QHBoxLayout()
        
        lbl_pregunta = QLabel("¿No tienes cuenta?")
        lbl_pregunta.setStyleSheet("font-size: 13px; font-weight: normal; color: #f1f2f6;")
        
        self.btn_registro = QPushButton("Crear nuevo usuario")
        self.btn_registro.setProperty("class", "BotonEnlace")
        self.btn_registro.setCursor(Qt.PointingHandCursor)
        
        # CONEXIÓN CRÍTICA: Al hacer click, avisa a main.py
        self.btn_registro.clicked.connect(self.ir_a_registro_signal.emit)

        layout_registro.addStretch()
        layout_registro.addWidget(lbl_pregunta)
        layout_registro.addWidget(self.btn_registro)
        layout_registro.addStretch()

        # Armar el diseño final agregando los elementos al layout
        layout.addStretch()
        layout.addWidget(self.titulo)
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.mensaje_error)
        layout.addLayout(layout_registro)
        layout.addStretch()

        self.setLayout(layout)

    def verificar_login(self):
        """Valida que los campos no estén vacíos para entrar"""
        usuario = self.user_input.text()
        contra = self.pass_input.text()

        if usuario != "" and contra != "":

            if iniciarSesion(usuario, contra) == True:
                self.login_exitoso.emit()
            else:
                self.mensaje_error.setText("⚠️ Datos incompletos")
        else:
            self.mensaje_error.setText("")