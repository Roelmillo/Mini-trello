import pyodbc

# Función para obtener la conexión
def get_conexion():
    try:
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER= DESKTOP-KOPIFS3,1433;"  #PC escritorio
            # "SERVER= DESKTOP-9BPI07G,1433;"    #notebook
            "DATABASE=TR_Oper;"
            "UID=operadmin;"
            "PWD=operadmin1234"
            )
        # return conexion
        print("✅ Conexión exitosa a la base de datos.")
        # cursor = conexion.cursor()

        # cursor.execute("SELECT @@version;")
        # row = cursor.fetchone()
        # print("Versión de SQL Server:", row[0])

        # cursor.execute("SELECT * FROM dbo.usuarios;")
        #columnas
        # columnas = [column[0] for column in cursor.description]
        # print(" | ".join(columnas))
        # print("-" * 50)
        #filas
        # for row in cursor.fetchall():
        #     print(" | ".join(str(item) for item in row))
        return conexion
    except Exception as e:
        print("❌ Error en la conexión o consulta:", e)
    # finally:
    #     # Esto se ejecuta siempre, aunque haya error
    #     if cursor:
    #         cursor.close()
    #     if conexion:
    #         conexion.close()
    #     print("Conexión cerrada ✅")
# Llamar a la función para probar la conexión
# get_conexion()