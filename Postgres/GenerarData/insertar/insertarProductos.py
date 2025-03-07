import json
import psycopg2

# 📂 Cargar los datos desde el JSON
with open("GenerarData/json/productos.json", "r", encoding="utf-8") as file:
    productos = json.load(file)

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
        cursor.execute(
            "INSERT INTO productos (id_producto, name_producto, id_provedor) VALUES (%s, %s, %s)",
            (producto["id_producto"], producto["name_producto"], producto["id_provedor"])
        )

    conn.commit()
    print("✅ Productos insertados correctamente en PostgreSQL")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    cursor.close()
    conn.close()
