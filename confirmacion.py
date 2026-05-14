# confirmacion.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class VentanaConfirmacion(QWidget):
    nueva_orden = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        mensaje = QLabel("¡Compra Procesada con Éxito!")
        mensaje.setAlignment(Qt.AlignCenter)
        mensaje.setProperty("class", "SuccessLabel")

        self.detalles = QLabel("")
        self.detalles.setAlignment(Qt.AlignCenter)

        btn_volver = QPushButton("Realizar Nueva Orden")
        btn_volver.clicked.connect(self.nueva_orden.emit)

        layout.addStretch()
        layout.addWidget(mensaje)
        layout.addWidget(self.detalles)
        layout.addWidget(btn_volver)
        layout.addStretch()

        self.setLayout(layout)

    def mostrar_resumen(self, total, metodo):
        self.detalles.setText(f"Pagaste ${total} usando {metodo}.\n¡Tu pizza está en el horno!")