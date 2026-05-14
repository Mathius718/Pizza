# ingredientes.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup, QCheckBox
from PyQt5.QtGui import QPixmap

class VentanaIngredientes(QWidget):
    ir_a_pago = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.line = QVBoxLayout()

        titulo = QLabel("Selecciona el Tamaño y los Ingredientes")
        titulo.setAlignment(Qt.AlignCenter)
        self.line.addWidget(titulo)

        # --- SECCIÓN DE TAMAÑOS CON IMÁGENES ---
        self.button_group = QButtonGroup()
        
        # Diccionario para configurar tamaños rápido (Nombre: [Precio, Archivo])
        tamanos = {
            'Pequeña ($5)': [5, 'pizzapequeña.png'],
            'Mediana ($8)': [8, 'pizzamediana.png'],
            'Familiar ($12)': [12, 'pizza.png']
        }

        for texto, datos in tamanos.items():
            fila = QHBoxLayout()
            img_label = QLabel()
            pixmap = QPixmap(datos[1]).scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            img_label.setPixmap(pixmap)
            
            rb = QRadioButton(texto)
            if datos[0] == 5: rb.setChecked(True) # Pequeña por defecto
            self.button_group.addButton(rb, id=datos[0])
            
            fila.addWidget(img_label)
            fila.addWidget(rb)
            fila.addStretch()
            self.line.addLayout(fila)

        self.line.addWidget(QLabel("Ingredientes Extra ($2 c/u):"))

        # --- SECCIÓN DE INGREDIENTES CON IMÁGENES ---
        # Doble Queso
        self.chk_queso = self.crear_fila_ingrediente("pizzadequeso.png", "Doble Queso")
        # Pepperoni
        self.chk_pepperoni = self.crear_fila_ingrediente("pizzapepperoni.png", "Pepperoni")
        # Champiñones
        self.chk_champinones = self.crear_fila_ingrediente("pizzadechampiñon.png", "Champiñones")

        # Botón y Total
        self.title = QLabel("Costo actual: $5")
        self.title.setAlignment(Qt.AlignCenter)
        self.button = QPushButton('Confirmar Ingredientes y Ver Total')

        self.line.addWidget(self.title)
        self.line.addWidget(self.button)
        self.setLayout(self.line)

        # Conexiones
        self.button_group.buttonClicked.connect(self.actualizar_costo_en_vivo)
        self.chk_queso.stateChanged.connect(self.actualizar_costo_en_vivo)
        self.chk_pepperoni.stateChanged.connect(self.actualizar_costo_en_vivo)
        self.chk_champinones.stateChanged.connect(self.actualizar_costo_en_vivo)
        self.button.clicked.connect(self.procesar_orden)

    def crear_fila_ingrediente(self, ruta_img, nombre):
        fila = QHBoxLayout()
        img = QLabel()
        img.setPixmap(QPixmap(ruta_img).scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        chk = QCheckBox(nombre)
        fila.addWidget(img)
        fila.addWidget(chk)
        fila.addStretch()
        self.line.addLayout(fila)
        return chk

    def calcular_total(self):
        total = self.button_group.checkedId()
        if self.chk_queso.isChecked(): total += 2
        if self.chk_pepperoni.isChecked(): total += 2
        if self.chk_champinones.isChecked(): total += 2
        return total

    def actualizar_costo_en_vivo(self):
        self.title.setText(f"Costo actual: ${self.calcular_total()}")

    def procesar_orden(self):
        self.ir_a_pago.emit(self.calcular_total())