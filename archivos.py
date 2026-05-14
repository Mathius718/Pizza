import os
ARCHIVOS = "usuarios.txt"

def registrarUsuarios(usuario, contrasena):
    if usuario == "" or contrasena == "":
        print('Error: los campos no pueden estar vacios.')
        return False
    with open(ARCHIVOS, 'a', encoding='utf-8') as archivo:
        archivo.write(f'{usuario},{contrasena}\n')
    
    print(f"Exito: Usuario '{usuario}' registrado correctamente")

def iniciarSesion(usuario, contrasena):
    if not os.path.exists(ARCHIVOS):
        print('Error: Base de datos no encontrada. Registrate primero.')
        return False
    with open(ARCHIVOS, 'r', encoding='utf-8') as archivo:
        lineas= archivo.readlines()

        for linea in lineas:
            datos = linea.strip().split(',')
            if len(datos) == 2:
                userGuardado= datos[0]
                passGuardado= datos[1]

                if userGuardado == usuario and passGuardado == contrasena:
                    print(f"Bienvenido de nuevo, {usuario}!")
                    return True
                
print('Error: Usuario o contraseña incorrectos.')
