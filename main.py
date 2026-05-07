# main.py
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from estrilo import STYLESHEET
from login import VentanaLogin
from ingredientes import VentanaIngredientes
from pago import VentanaPago
from confimacion import VentanaConfirmacion
from error import VentanaError

class PizzeriaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # creando el nombre de la ventana principal y tamaño (De tu código)
        self.setWindowTitle('Pizzería - Sistema de Pedidos')
        self.move(500, 70)
        self.resize(500, 400)

        # El QStackedWidget permite cambiar entre ventanas en el mismo espacio
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Inicializando todas las ventanas
        self.view_login = VentanaLogin()
        self.view_ingredientes = VentanaIngredientes()
        self.view_pago = VentanaPago()
        self.view_confirmacion = VentanaConfirmacion()
        self.view_error = VentanaError()

        # Añadiendo ventanas al Stack
        self.stack.addWidget(self.view_login)         # Índice 0
        self.stack.addWidget(self.view_ingredientes)  # Índice 1
        self.stack.addWidget(self.view_pago)          # Índice 2
        self.stack.addWidget(self.view_confirmacion)  # Índice 3
        self.stack.addWidget(self.view_error)         # Índice 4

        # Variables de control
        self.total_actual = 0

        # Conectando las señales (navegación entre pantallas)
        self.view_login.login_exitoso.connect(self.ir_a_ingredientes)
        self.view_ingredientes.ir_a_pago.connect(self.ir_a_pago)
        self.view_pago.procesar_compra.connect(self.simular_procesamiento)
        self.view_confirmacion.nueva_orden.connect(self.ir_a_ingredientes)
        self.view_error.reintentar.connect(lambda: self.stack.setCurrentIndex(2)) # Vuelve a pago

    def ir_a_ingredientes(self):
        self.stack.setCurrentIndex(1)

    def ir_a_pago(self, total):
        self.total_actual = total
        self.view_pago.actualizar_total(total)
        self.stack.setCurrentIndex(2)

    def simular_procesamiento(self, metodo):
        # Simulamos que a veces falla la compra aleatoriamente (30% de probabilidad de error)
        exito = random.choice([True, True, True, False])
        
        if exito:
            self.view_confirmacion.mostrar_resumen(self.total_actual, metodo)
            self.stack.setCurrentIndex(3) # Va a Confirmación
        else:
            self.stack.setCurrentIndex(4) # Va a Error

if __name__ == "__main__":
    # creando un objeto de aplicación
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLESHEET)
    
    # creando un objeto de ventana principal
    window = PizzeriaApp()
    
    # dar a la ventana el comando para mostrarse
    window.show()
    
    # deja la aplicación abierta hasta que se presione el botón salir
    sys.exit(app.exec_())