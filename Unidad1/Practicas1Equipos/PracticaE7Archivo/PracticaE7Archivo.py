import csv
import os 

directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_csv = os.path.join(directorio_actual, 'Entrada.csv')
print(archivo_csv)
try:
    with open(archivo_csv,mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = []

        for row in csv_reader:
            data.append(row)
    print(data)
    
except FileNotFoundError:
    print("El archivo csv no se encontro")
except Exception as e:
    print("Se produjo un error: ",str(e))
