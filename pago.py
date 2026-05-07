# pago.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup

class VentanaPago(QWidget):
    procesar_compra = pyqtSignal(str) # Emite el método de pago

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.lbl_total = QLabel("Total a Pagar: $0")
        self.lbl_total.setAlignment(Qt.AlignCenter)
        self.lbl_total.setStyleSheet("color: rgb(46, 213, 115); font-size: 20px;")
        
        layout.addWidget(self.lbl_total)
        layout.addWidget(QLabel("Selecciona tu método de pago:"))

        self.rb_tarjeta = QRadioButton("Tarjeta de Crédito / Débito")
        self.rb_tarjeta.setChecked(True)
        self.rb_efectivo = QRadioButton("Efectivo")
        self.rb_pago_movil = QRadioButton("Pago Móvil")

        self.grupo_pago = QButtonGroup()
        self.grupo_pago.addButton(self.rb_tarjeta)
        self.grupo_pago.addButton(self.rb_efectivo)
        self.grupo_pago.addButton(self.rb_pago_movil)

        layout.addWidget(self.rb_tarjeta)
        layout.addWidget(self.rb_efectivo)
        layout.addWidget(self.rb_pago_movil)

        btn_pagar = QPushButton("Pagar Ahora")
        btn_pagar.clicked.connect(self.ejecutar_pago)

        layout.addStretch()
        layout.addWidget(btn_pagar)

        self.setLayout(layout)

    def actualizar_total(self, total):
        self.lbl_total.setText(f"Total a Pagar: ${total}")

    def ejecutar_pago(self):
        metodo = self.grupo_pago.checkedButton().text()
        self.procesar_compra.emit(metodo)