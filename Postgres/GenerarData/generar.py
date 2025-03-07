import json
import psycopg2
import random
from datetime import datetime, timedelta

# 📂 Cargar los datos desde los archivos JSON
def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error al cargar {file_path}: {e}")
        return []

clientes = load_json("Postgres/GenerarData/json/clientes.json")
usuarios = load_json("Postgres/GenerarData/json/usuario.json")
productos = load_json("Postgres/GenerarData/json/productos.json")
provedores = load_json("Postgres/GenerarData/json/provedores.json")

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

    opcion = input("Seleccione una opción: 1 = Ventas, 2 = Compras, 3 = Productos: ")

    if opcion == "1":  # Insertar Ventas
        for producto in productos:
            cliente_aleatorio = random.choice(clientes)
            usuario_aleatorio = random.choice(usuarios)
            price_united = producto['price_publico']
            cantidad_united = random.randint(1, 10)
            total_venta = round(price_united * cantidad_united, 2)
            metodo_pago = random.randint(1, 5)
            fecha_venta = fecha_inicio + timedelta(days=random.randint(0, (fecha_actual - fecha_inicio).days))
            fecha_venta_str = fecha_venta.strftime("%Y-%m-%d")
            id_caja = random.randint(1, 4)

            cursor.execute(
                """INSERT INTO ventas (id_cliente, id_usuario, id_producto, descripcion, price_united, cantidad_united, total_venta, metodo_pago, fecha_venta, id_caja)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_venta""",
                (cliente_aleatorio["id_cliente"], usuario_aleatorio["id_usuario"], producto["id_producto"], producto["name_producto"],
                 price_united, cantidad_united, total_venta, metodo_pago, fecha_venta_str, id_caja)
            )
            

        print("✅ Ventas insertadas correctamente en PostgreSQL")

    elif opcion == "2":  # Insertar Compras
        for producto in productos:
            usuario_aleatorio = random.choice(usuarios)
            price_unitario = round(random.uniform(10, 500), 2)
            cantidad_united = random.randint(1, 10)
            total_compra = round(price_unitario * cantidad_united, 2)
            fecha_compra = fecha_inicio + timedelta(days=random.randint(0, (fecha_actual - fecha_inicio).days))
            fecha_compra_str = fecha_compra.strftime("%Y-%m-%d")

            cursor.execute(
                """INSERT INTO compra (id_provedor, id_usuario, id_producto, detalle_producto, fecha_compra, price_unitario, total_compra, cantidad_compra)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (producto["id_provedor"], usuario_aleatorio["id_usuario"], producto["id_producto"], producto["name_producto"], fecha_compra_str, price_unitario, total_compra, cantidad_united)
            )

        print("✅ Compras insertadas correctamente en PostgreSQL")

    elif opcion == "3":  # Insertar Productos
        for producto in productos:
            cursor.execute(
                "INSERT INTO productos (id_producto, name_producto, id_provedor) VALUES (%s, %s, %s)",
                (producto["id_producto"], producto["name_producto"], producto["id_provedor"])
            )

        print("✅ Productos insertados correctamente en PostgreSQL")
    else:
        print("❌ Opción no válida. Inténtelo de nuevo.")

    conn.commit()

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    cursor.close()
    conn.close()