The **GenerateData folder** has main functions from which it is derived as follows:
1.generate {
contains files called generateProducts.py that generate random data acquired from a .json file for the actual data ingestion without altering the order or duplicating, generating new data and saving it in a .json to proceed to insert it into the insert folder
}

2.insert {
contains .py files that perform functions of generating random data with main labels from json files to comply with real data, not to duplicate and to carry out continuous management of "real" data
}

3.json {
contains .json files that comply with customer, product, supplier and user data for the random creation of the other missing data in the tables
}

--------------------------------------------------------------------------------------------

La **CARPETA GenerarData** tiene principales funciones de en el cual se deriva asi
1.generar {
    contiene archivos llamado generarProductos.py que generan datos aleatorios adquiridos de un archivo .json para la ingesta real de datos sin alterar el orden o duplicar, generando nuevos datos y guardado en un .json para proseguir a inserta en la carpeta insertar
}

2.insertar{
    contiene archivos .py que cumple funciones de generar datos ramdos con etiquetas principales de archivos json para complir con datos reales, no duplicar y llevar un manejo continuo de datos "reales"
}

3.json{
    contiene archivos .json que cumple con datos de clientes, productos, provedores y usuarios para la creacion aleaotira de los demas datos faltantes en las tablas
}


4. el archivo generar.py contiene los datos de gnerar todo incluido a traves de input