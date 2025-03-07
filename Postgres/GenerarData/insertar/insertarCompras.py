import json
import psycopg2
import random
from datetime import datetime, timedelta
import json

# 📂 Cargar los datos desde el JSON
clientes_json_path = "Postgres/GenerarData/json/clientes.json"
usuarios_json_path = "Postgres/GenerarData/json/usuario.json"
productos_json_path = "Postgres/GenerarData/json/productos.json"
provedor_json_path = "Postgres/GenerarData/json/provedores.json"
    

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
        usuario_aleatorio = random.choice(usuarios) # Selecciona un usuario aleatorio
        price_unitario = round(random.uniform(10, 500), 2)  # Precio entre 10 y 500
        cantidad_united = random.randint(1, 10)  # Cantidad entre 1 y 10
        total_compra = round(price_unitario * cantidad_united, 2)
        fecha_compra = fecha_inicio + timedelta(days=random.randint(0, (fecha_actual - fecha_inicio).days))
        fecha_compra = fecha_compra.strftime("%Y-%m-%d")
        
        cursor.execute(
            "INSERT INTO compra ( id_provedor, id_usuario, id_producto, detalle_producto, fecha_compra, price_unitario, total_compra, cantidad_compra) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (producto["id_provedor"], usuario_aleatorio["id_usuario"], producto["id_producto"], producto["name_producto"], fecha_compra, price_unitario, total_compra, cantidad_united)
        )

    conn.commit()
    print("✅ Productos insertados correctamente en PostgreSQL")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    cursor.close()
    conn.close()
