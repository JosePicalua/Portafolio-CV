import json
import random
import os

# 📂 Ruta del archivo JSON
nombre_archivo = "Postgres/GenerarData/json/productos.json"

# 📂 Cargar los datos existentes si el archivo ya existe
if os.path.exists(nombre_archivo):
    with open(nombre_archivo, "r") as file:
        try:
            productos_generados = json.load(file)
        except json.JSONDecodeError:
            productos_generados = []  # Si el archivo está vacío o corrupto, iniciar con una lista vacía
else:
    productos_generados = []  # Si el archivo no existe, iniciar con una lista vacía

# 📂 Cargar los proveedores desde el JSON
with open("GenerarData/json/provedores.json", "r") as file:
    proveedores = json.load(file)

# 🔄 Función para generar un producto aleatorio
def generar_producto():
    nombres_productos = [
        "Laptop", "Mouse", "Teclado", "Monitor", "Impresora", "Auriculares", "Altavoces", "Webcam",
        "Disco Duro", "SSD", "Memoria RAM", "Tarjeta Gráfica", "Procesador", "Placa Base", "Fuente de Alimentación",
        "Ventilador", "Refrigeración Líquida", "Cable HDMI", "Cable USB", "Silla Gamer", "Escritorio",
        "Micrófono", "Router", "Módem", "Smartphone", "Tablet", "Cámara de Seguridad", "Reloj Inteligente",
        "Cargador", "Batería Externa", "Estabilizador", "Proyector", "Control Remoto", "Joystick", "Dron"
    ]
    
    price_united = round(random.uniform(10, 500), 2)  # Precio entre 10 y 500

    return {
        "id_producto": random.randint(1000, 9999),  # ID aleatorio
        "name_producto": random.choice(nombres_productos),  # Nombre aleatorio
        "id_provedor": random.choice(proveedores)["id_provedor"],  # ID de proveedor aleatorio
        "price_united": price_united,
        "price_publico": round(price_united * 1.2, 2)  # Precio público con un 20% de incremento
    }
# 📌 Generar 10 nuevos productos y agregarlos a la lista existente
productos_generados.extend([generar_producto() for _ in range(40)])

# 📂 Guardar los datos actualizados en el mismo archivo JSON
with open(nombre_archivo, mode="w") as file:
    json.dump(productos_generados, file, indent=4)  # Guardar con formato legible

print(f"✅ Datos agregados y guardados en: {nombre_archivo}")
