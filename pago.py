# pago.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtGui import QPixmap

class VentanaPago(QWidget):
    procesar_compra = pyqtSignal(str) # Emite el método de pago

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.lbl_total = QLabel("Total a Pagar: $0")
        self.lbl_total.setAlignment(Qt.AlignCenter)
        self.lbl_total.setStyleSheet("color: rgb(46, 213, 115); font-size: 24px; margin-bottom: 10px;")
        
        layout.addWidget(self.lbl_total)
        
        instruccion = QLabel("Selecciona tu método de pago:")
        instruccion.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(instruccion)

        # Grupo de botones para asegurar que solo se elija uno
        self.grupo_pago = QButtonGroup()

        # --- OPCIONES DE PAGO CON ICONOS ---
        # 1. Tarjeta (Asegúrate de tener una imagen llamada tarjeta.jpg o similar)
        self.rb_tarjeta = self.crear_fila_pago(layout, "Tarjeta de Crédito / Débito", "tarjeta.png", True)
        self.grupo_pago.addButton(self.rb_tarjeta)

        # 2. Efectivo
        self.rb_efectivo = self.crear_fila_pago(layout, "Efectivo", "plata.png")
        self.grupo_pago.addButton(self.rb_efectivo)

        # 3. Pago Móvil
        self.rb_pago_movil = self.crear_fila_pago(layout, "Pago Móvil", "pago.png")
        self.grupo_pago.addButton(self.rb_pago_movil)

        # Botón de acción
        btn_pagar = QPushButton("Pagar Ahora")
        btn_pagar.clicked.connect(self.ejecutar_pago)

        layout.addStretch()
        layout.addWidget(btn_pagar)
        self.setLayout(layout)

    def crear_fila_pago(self, layout_principal, texto, ruta_img, marcado=False):
        """Función auxiliar para crear una fila con imagen y botón de radio"""
        fila = QHBoxLayout()
        
        # Icono
        label_img = QLabel()
        pixmap = QPixmap(ruta_img).scaled(35, 35, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_img.setPixmap(pixmap)
        label_img.setFixedWidth(40) # Mantiene alineados los botones de radio
        
        # Radio Button
        rb = QRadioButton(texto)
        if marcado:
            rb.setChecked(True)
        
        fila.addWidget(label_img)
        fila.addWidget(rb)
        fila.addStretch()
        
        layout_principal.addLayout(fila)
        return rb

    def actualizar_total(self, total):
        self.lbl_total.setText(f"Total a Pagar: ${total}")

    def ejecutar_pago(self):
        metodo = self.grupo_pago.checkedButton().text()
        self.procesar_compra.emit(metodo)