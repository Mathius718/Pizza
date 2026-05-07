# error.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class VentanaError(QWidget):
    reintentar = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        mensaje = QLabel("¡Error al procesar la compra!")
        mensaje.setAlignment(Qt.AlignCenter)
        mensaje.setProperty("class", "ErrorLabel")

        sub_mensaje = QLabel("No se pudo conectar con el banco o saldo insuficiente.")
        sub_mensaje.setAlignment(Qt.AlignCenter)

        btn_volver = QPushButton("Reintentar Pago")
        btn_volver.clicked.connect(self.reintentar.emit)

        layout.addStretch()
        layout.addWidget(mensaje)
        layout.addWidget(sub_mensaje)
        layout.addWidget(btn_volver)
        layout.addStretch()

        self.setLayout(layout)