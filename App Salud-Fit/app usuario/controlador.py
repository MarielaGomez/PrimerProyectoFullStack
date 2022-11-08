
from config import obtener_conexion


# Entities:
from models.entities.User import User


def insertar_usuario(nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO user(username, dni, email) VALUES (%s, %s, %s)",
                       (nombre, descripcion, precio))
    conexion.commit()
    conexion.close()


def obtener_usuarios():
    conexion = obtener_conexion()
    datos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, username, dni, email FROM user")
        datos = cursor.fetchall()
    conexion.close()
    return datos


def eliminar_usuario(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM user WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    datos = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, username, dni, email, nombres, apellido, direccion, numeracion FROM user WHERE id = %s", (id,))
        datos = cursor.fetchone()
    conexion.close()
    return datos






def actualizar_usuario(username, dni, email, nombres, apellido, direccion, numeracion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE user SET username = %s, dni = %s, email = %s, nombres = %s, apellido = %s, direccion = %s, numeracion = %s   WHERE id = %s",
                       (username, dni, email, nombres, apellido, direccion, numeracion, id))
    conexion.commit()
    conexion.close()


