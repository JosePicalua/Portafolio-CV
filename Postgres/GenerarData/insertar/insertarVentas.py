import json
import psycopg2
import random
from datetime import datetime, timedelta

# 📂 Cargar los datos desde el JSON
clientes_json_path = "GenerarData/json/clientes.json"
usuarios_json_path = "GenerarData/json/usuario.json"
productos_json_path = "GenerarData/json/productos.json"
provedor_json_path = "GenerarData/json/provedores.json"

def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error al cargar {file_path}: {e}")
        return []

clientes = load_json(clientes_json_path)
usuarios = load_json(usuarios_json_path)
productos = load_json(productos_json_path)
provedor = load_json(provedor_json_path)

fecha_inicio = datetime(2024, 3, 2)
fecha_actual = datetime.now()

# 🔗 Conectar a PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="empresa_sales",
        user="postgres",
        password="Josepicalua123.",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # 🔄 Insertar productos en la base de datos
    for producto in productos:
        clientes_aleatorio = random.choice(clientes)  # Selecciona un usuario aleatorio
        usuario_aleatorio = random.choice(usuarios)  # Selecciona un usuario aleatorio
        price_united = producto['price_publico']  # Usar el precio público del producto
        cantidad_united = random.randint(1, 10)  # Cantidad entre 1 y 10
        total_venta = round(price_united * cantidad_united, 2)
        metodo_pago = random.randint(1, 5)
        fecha_venta = fecha_inicio + timedelta(days=random.randint(0, (fecha_actual - fecha_inicio).days))
        fecha_venta_str = fecha_venta.strftime("%Y-%m-%d")
        id_caja = random.randint(1, 4)

        # Insertar en la tabla ventas y obtener el id_venta generado
        cursor.execute(
            "INSERT INTO ventas (id_cliente, id_usuario, id_producto, descripcion, price_united, cantidad_united, total_venta, metodo_pago, fecha_venta, id_caja) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_venta",
            (clientes_aleatorio["id_cliente"], usuario_aleatorio["id_usuario"], producto["id_producto"], producto["name_producto"], price_united, cantidad_united, total_venta, metodo_pago, fecha_venta_str, id_caja)
        )
        id_venta = cursor.fetchone()[0]

        # Insertar en la tabla detalle_ventas usando el id_venta generado
        cursor.execute(
            "INSERT INTO detalle_ventas (id_venta, id_producto, id_cliente, id_usuario, id_caja, total_venta, fecha_venta, metodo_pago) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (id_venta, producto["id_producto"], clientes_aleatorio["id_cliente"], usuario_aleatorio["id_usuario"], id_caja, total_venta, fecha_venta_str, metodo_pago)
        )

    conn.commit()
    print("✅ Productos insertados correctamente en PostgreSQL")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    cursor.close()
    conn.close()