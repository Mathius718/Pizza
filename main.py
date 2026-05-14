# main.py
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from estrilo import STYLESHEET
from login import VentanaLogin
from registro import VentanaRegistro
from ingredientes import VentanaIngredientes
from pago import VentanaPago
from confirmacion import VentanaConfirmacion
from error import VentanaError

class PizzeriaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana principal
        self.setWindowTitle('Pizzería Deliciosa - Sistema de Pedidos')
        self.move(500, 50)
        # Aumentamos la altura a 650 para que quepan las imágenes cómodamente
        self.resize(500, 650)

        # El QStackedWidget permite cambiar entre ventanas
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Inicializando todas las ventanas
        self.view_login = VentanaLogin()
        self.view_registro = VentanaRegistro() # Ventana de crear cuenta
        self.view_ingredientes = VentanaIngredientes()
        self.view_pago = VentanaPago()
        self.view_confirmacion = VentanaConfirmacion()
        self.view_error = VentanaError()

        # Añadiendo ventanas al Stack (Orden de índices)
        self.stack.addWidget(self.view_login)         # Índice 0
        self.stack.addWidget(self.view_ingredientes)  # Índice 1
        self.stack.addWidget(self.view_pago)          # Índice 2
        self.stack.addWidget(self.view_confirmacion)  # Índice 3
        self.stack.addWidget(self.view_error)         # Índice 4
        self.stack.addWidget(self.view_registro)      # Índice 5

        # Variables de control
        self.total_actual = 0
        
        # Desde Login
        self.view_login.login_exitoso.connect(self.ir_a_ingredientes)
        self.view_login.ir_a_registro_signal.connect(self.ir_a_registro) # Ir a registro
        
        # Desde Registro
        self.view_registro.volver_login.connect(self.ir_a_login)
        self.view_registro.usuario_registrado.connect(self.ir_a_login)
        
        # Flujo de pedido
        self.view_ingredientes.ir_a_pago.connect(self.ir_a_pago)
        self.view_pago.procesar_compra.connect(self.simular_procesamiento)
        
        # Post-compra
        self.view_confirmacion.nueva_orden.connect(self.ir_a_ingredientes)
        self.view_error.reintentar.connect(lambda: self.stack.setCurrentIndex(2)) # Vuelve a pago

    # Métodos de navegación
    def ir_a_login(self):
        self.stack.setCurrentIndex(0)

    def ir_a_registro(self):
        self.stack.setCurrentIndex(5)

    def ir_a_ingredientes(self):
        self.stack.setCurrentIndex(1)

    def ir_a_pago(self, total):
        self.total_actual = total
        self.view_pago.actualizar_total(total)
        self.stack.setCurrentIndex(2)

    def simular_procesamiento(self, metodo):
        # 75% de probabilidad de éxito
        exito = random.choice([True, True, True, False])
        
        if exito:
            self.view_confirmacion.mostrar_resumen(self.total_actual, metodo)
            self.stack.setCurrentIndex(3) # Va a Confirmación
        else:
            self.stack.setCurrentIndex(4) # Va a Error

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Aplicamos el estilo global desde estilos.py
    app.setStyleSheet(STYLESHEET)
    
    window = PizzeriaApp()
    window.show()
    
    sys.exit(app.exec_())