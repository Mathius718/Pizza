# ingredientes.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup, QCheckBox

class VentanaIngredientes(QWidget):
    ir_a_pago = pyqtSignal(int) # Emite el costo total

    def __init__(self):
        super().__init__()
        self.line = QVBoxLayout()

        titulo = QLabel("Selecciona el Tamaño y los Ingredientes")
        titulo.setAlignment(Qt.AlignCenter)
        self.line.addWidget(titulo)

        # --- LÓGICA BASADA EN TU CÓDIGO ORIGINAL ---
        # creando objetos de botón de radio para el tamaño
        self.radio_button_1 = QRadioButton('Pequeña ($5)')
        self.radio_button_1.setChecked(True)
        self.radio_button_2 = QRadioButton('Mediana ($8)')
        self.radio_button_3 = QRadioButton('Familiar ($12)')

        # crear un grupo de botones de radio
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1, id=5)
        self.button_group.addButton(self.radio_button_2, id=8)
        self.button_group.addButton(self.radio_button_3, id=12)

        # colocar los botones de radio en la layout vertical
        self.line.addWidget(self.radio_button_1)
        self.line.addWidget(self.radio_button_2)
        self.line.addWidget(self.radio_button_3)

        # Ingredientes extra
        self.line.addWidget(QLabel("Ingredientes Extra ($2 c/u):"))
        self.chk_queso = QCheckBox("Doble Queso")
        self.chk_pepperoni = QCheckBox("Pepperoni")
        self.chk_champinones = QCheckBox("Champiñones")
        
        self.line.addWidget(self.chk_queso)
        self.line.addWidget(self.chk_pepperoni)
        self.line.addWidget(self.chk_champinones)

        # creando un objeto botón y establecer una etiqueta en esta
        self.button = QPushButton('Confirmar Ingredientes y Ver Total')
        
        # crear un campo donde se mostrará el texto sobre el botón seleccionado (costo)
        self.title = QLabel("Costo actual: $5")
        self.title.setAlignment(Qt.AlignCenter)

        # colocar el botón y titulo en el centro de la layout
        self.line.addWidget(self.title)
        self.line.addWidget(self.button)

        self.setLayout(self.line)

        # vincular eventos
        self.button_group.buttonClicked.connect(self.actualizar_costo_en_vivo)
        self.chk_queso.stateChanged.connect(self.actualizar_costo_en_vivo)
        self.chk_pepperoni.stateChanged.connect(self.actualizar_costo_en_vivo)
        self.chk_champinones.stateChanged.connect(self.actualizar_costo_en_vivo)
        
        # vincular el clic de un botón a una llamada a una función
        self.button.clicked.connect(self.procesar_orden)

    def calcular_total(self):
        # Extrae el ID del botón que funciona como el precio base
        total = self.button_group.checkedId()
        if self.chk_queso.isChecked(): total += 2
        if self.chk_pepperoni.isChecked(): total += 2
        if self.chk_champinones.isChecked(): total += 2
        return total

    # una función que cambia la información (texto) sobre los botones seleccionados
    def actualizar_costo_en_vivo(self):
        total = self.calcular_total()
        self.title.setText(f"Costo actual: ${total}")

    def procesar_orden(self):
        total = self.calcular_total()
        self.ir_a_pago.emit(total)