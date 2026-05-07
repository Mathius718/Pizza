# estilos.py
STYLESHEET = """
QWidget {
    background-color: rgb(183, 21, 64); /* Fondo principal */
    color: white;
    font-family: Arial;
    font-size: 14px;
}
QPushButton {
    background-color: rgb(44, 58, 71); /* Color oscuro para botones */
    color: white;
    border-radius: 5px;
    padding: 10px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: rgb(255, 94, 87); /* Color de hover */
}
QPushButton:pressed {
    background-color: rgb(235, 59, 90); /* Color al presionar */
}
QLineEdit {
    background-color: white;
    color: rgb(44, 58, 71);
    padding: 8px;
    border-radius: 4px;
}
QRadioButton, QCheckBox {
    font-size: 16px;
    padding: 5px;
}
QLabel {
    font-size: 18px;
    font-weight: bold;
}
.SuccessLabel {
    color: rgb(5, 196, 107); /* Verde para éxito */
    font-size: 22px;
}
.ErrorLabel {
    color: rgb(255, 94, 87); /* Rojo claro para error */
    font-size: 22px;
}
"""