import sqlite3 as sql
from model.producto import *
from colorama import Fore, Style # type: ignore

nombre_db = "inventario.db"

def crear_tabla_producto():
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT,
            precio REAL,
            cantidad INTEGER,
            categoria TEXT)"""
    )
    conn.commit()
    print(f"{Fore.BLUE}\nSe creó la tabla con exito.\n{Style.RESET_ALL}")
    conn.close()

def registrar_producto(producto):
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute(
                "INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria) VALUES (?, ?, ?, ?, ?)",
                (producto.nombre, producto.descripcion, producto.precio, producto.cantidad, producto.categoria),
            )
    conn.commit()
    conn.close()

def buscar_producto_por_nombre(nombre):
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def buscar_producto_por_campo(campo, valor):
    campos_validos = ["id", "nombre", "categoria"]
    if campo not in campos_validos:
        raise ValueError(f"Campo '{campo}' no es válido")
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM productos WHERE {campo} = ?", (valor,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def buscar_producto_por_id(id):
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def buscar_productos():
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def actualizar_producto(cantidad, id):
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute("UPDATE productos Set cantidad = ? WHERE id = ?", (cantidad, id))
    cambios = cursor.rowcount
    conn.commit()
    conn.close()
    return cambios

def eliminar_producto_por_id(id):
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    eliminados = cursor.rowcount
    conn.commit()
    conn.close()
    return eliminados

def listar_productos_bajo_stock(stock):
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad < ?", (stock,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def listar_productos_por_categoria(categoria):
    conn = sql.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos where categoria = ?", (categoria,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados