# estilos.py
STYLESHEET = """
QWidget {
    background-color: rgb(183, 21, 64);
    color: white;
    font-family: 'Segoe UI', Arial, sans-serif;
}

/* Título de bienvenida */
.TituloLogin {
    font-size: 32px;
    font-weight: 800;
    color: #ffda79;
    margin-bottom: 20px;
}

QLineEdit {
    background-color: white;
    color: #2d3436;
    padding: 12px;
    border-radius: 8px;
    border: 2px solid transparent;
    font-size: 14px;
}

QLineEdit:focus {
    border: 2px solid #ffda79;
}

QPushButton {
    background-color: #2c3a47;
    color: white;
    border-radius: 8px;
    padding: 12px;
    font-weight: bold;
    font-size: 15px;
}

QPushButton:hover {
    background-color: #ff5e57;
}

/* Estilo para el enlace de "Crear cuenta" */
.BotonEnlace {
    background-color: transparent;
    color: #ffda79;
    text-decoration: underline;
    font-size: 13px;
    font-weight: normal;
}

.BotonEnlace:hover {
    color: white;
    background-color: transparent;
}

.ErrorLabel {
    color: #fab1a0;
    font-size: 14px;
    font-weight: bold;
}
"""