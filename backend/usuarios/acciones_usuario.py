from conexiones.conexion import get_conexion
from usuarios import usuario as user

class Acciones:
    def registro(self):
        conn = get_conexion()
        #Función para registrar un nuevo usuario.
        nombre = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")
        id_subarea = int(input("Ingrese subarea: "))
        
        usuario = user.Usuario(nombre,contrasena,id_subarea)
        registro = usuario.registrar_usuario_bd(conn)
        print(f"print de registro -registro- {registro}")
        if registro [0] >=1:
            print(f"Perfecto {registro[1].nombre} te registraste exitosamente")
        else:
            print("Error, no te pudiste registrar correctamente")
        
    def login(self):
        #Función para iniciar sesión de un usuario.
        conn = get_conexion()
        if conn:
            try:
                nombre = input("Ingrese su nombre de usuario: ")
                contrasena = input("Ingrese su contraseña: ")
                
                usuario = user.Usuario(nombre,contrasena, '')
                login_res = usuario.login_usuario_bd(conn)
                print(f"print de login -login_res-{login_res}")
                if login_res is not None:
                    print(f"¡Bienvenido, {login_res['nombre']}! Has iniciado sesión con éxito.")
                else:
                    print(f"Usuario o contraseña incorrectos.{login_res}")

            except Exception as e:
                print("Error inesperado en login")
                print(f"Error: {type(e).__name__} - {e}")
            finally:
                if conn is not None:
                    conn.close()         