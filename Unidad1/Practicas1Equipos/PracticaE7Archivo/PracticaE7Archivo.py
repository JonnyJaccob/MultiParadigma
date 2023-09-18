import csv
import os 

directorio_actual = os.path.dirname(os.path.abspath(__file__))

def DevolverRuta(name):
    return os.path.join(directorio_actual, name)

def Dicc_PorName(diccionario):
    diccionario_nuevo = {"Nombre": []}
    for elemento in diccionario:
        nombre = elemento.get('Nombre ', '')  
        diccionario_nuevo["Nombre"].append(nombre)  
    return diccionario_nuevo

def Crear_OrdenadoNumControl(lista_de_diccionarios):
    if not lista_de_diccionarios:
        return  # Salir si la lista está vacía

    # Ordenar la lista de diccionarios por el número de control
    lista_de_diccionarios_ordenada = sorted(lista_de_diccionarios, key=lambda x: int(x['Numero de control']))

    encabezado = list(lista_de_diccionarios_ordenada[0].keys())  # Tomar las llaves del primer diccionario

    with open(DevolverRuta('OrdenNumControl.csv'), mode='w', newline='', encoding='latin1') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=encabezado)
        writer.writeheader()

        for fila in lista_de_diccionarios_ordenada:
            writer.writerow({clave: fila[clave] for clave in encabezado})

def Crear_OrdenadoCalificacion(lista_de_diccionarios):
    if not lista_de_diccionarios:
        return  
    lista_de_diccionarios_ordenada = sorted(lista_de_diccionarios, key=lambda x: int(x['Calificacion']))

    encabezado = list(lista_de_diccionarios_ordenada[0].keys())  # Tomar las llaves del primer diccionario

    with open(DevolverRuta('OrdenCalif.csv'), mode='w', newline='', encoding='latin1') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=encabezado)
        writer.writeheader()

        for fila in lista_de_diccionarios_ordenada:
            writer.writerow({clave: fila[clave] for clave in encabezado})


archivo_csv = os.path.join(directorio_actual, 'Entrada.csv')
print(archivo_csv)
try:
    with open(archivo_csv,mode='r', encoding='latin1', errors='replace') as file:
        csv_reader = csv.DictReader(file)
        data = []

        for row in csv_reader:
            data.append(row)
    #print(data)
    #print(Dicc_PorName(data))
    
    diccionario_nuevo = Dicc_PorName(data)
    nombres = diccionario_nuevo["Nombre"]
    for nombre in nombres:
        print(nombre)

    Crear_OrdenadoNumControl(data)
    Crear_OrdenadoCalificacion(data)
except FileNotFoundError:
    print("El archivo csv no se encontro")
except Exception as e:
    print("Se produjo un error: ",str(e))

