from conexiones import conexion
import pyodbc

conexion = conexion.get_conexion()
cursor = conexion.cursor()

class Ticket:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def insert_ticket(self, titulo, descripcion=None, documentos=None, multimedia=None, id_tablero=None, id_estado=None, id_responsable=None):
        """
        Inserta un nuevo ticket en la tabla.
        """
        if not conexion:
            print("No hay conexión a la base de datos.")
            return

        insert_query = """
        INSERT INTO tickets (titulo, descripcion, documentos, multimedia, id_tablero, id_estado, id_responsable)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        try:
            cursor.execute(insert_query, titulo, descripcion, documentos, multimedia, id_tablero, id_estado, id_responsable)
            conexion.commit()
            print("Ticket insertado exitosamente.")
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error al insertar el ticket: {sqlstate}")
            conexion.rollback()

    def mostrar_tickets(self):
        """
        Obtiene todos los tickets de la tabla.
        """
        if not conexion:
            print("No hay conexión a la base de datos.")
            return None

        select_query = "SELECT * FROM tickets;"
        try:
            cursor.execute(select_query)
            tickets = cursor.fetchall()
            return tickets
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error al obtener los tickets: {sqlstate}")
            return None
