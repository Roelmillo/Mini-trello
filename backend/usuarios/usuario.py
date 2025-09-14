from conexiones import conexion
#import pyodbc
import hashlib

# Obtener la conexión
conn = conexion.get_conexion()

class Usuario:
    def __init__(self, nombre, contrasena, idsubarea):
        self.nombre = nombre
        self.contrasena = contrasena
        self.idsubarea = idsubarea

    # Función de registro en BD
    def registrar_usuario_bd(self, conn):
        if conn:
            try:
                # Cifrar contraseña
                # cifrado = hashlib.sha256()
                # cifrado.update(self.contrasena.encode("utf8"))
                # INSERT en BD
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO usuarios (nombre, contraseña, id_subarea) VALUES (?,?,?)",
                    # (self.nombre, cifrado.hexdigest(), self.idsubarea)
                    (self.nombre, self.contrasena, self.idsubarea)
                )
                conn.commit()
                resultado = [cursor.rowcount, self]
                print(f"print de registrar_usuario_bd -resultado- ", resultado)
                print("¡Registro exitoso!")
                return resultado

            except Exception as ex:
                print(f"Error al registrar usuario: {str(ex)}")
                return False

            finally:
                cursor.close()
        return False

    # Función de login en BD
    def login_usuario_bd(self, conn):
        # Cifrar contraseña
        # cifrado = hashlib.sha256()
        # cifrado.update(self.contrasena.encode("utf8"))

        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM dbo.usuarios WHERE nombre = ? AND contraseña = ?",
                    # (self.nombre, cifrado.hexdigest())
                    (self.nombre, self.contrasena)
                )
                fila = cursor.fetchone()
                print(f"print de login_ususario_bd -fila- {fila}")
                if fila:
                    return {"id": fila[0], "nombre": fila[1], "id_subarea": fila[3]}
                else:
                    return None
            except Exception as ex:
                print(f"Error al iniciar sesión: {str(ex)}")
                return False
            finally:
                cursor.close()
        # return None
