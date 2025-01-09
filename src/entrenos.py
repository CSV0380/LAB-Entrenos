from datetime import datetime
from collections import namedtuple
import csv

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta):
    entrenos = []
    with open(ruta, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo = str(tipo)
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            ubicacion = str(ubicacion)
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = True if compartido == "S" else False # O bien: compartido = bool(compartido)
            entrenos.append(Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido))
    return entrenos



def tipos_de_entrenos(lista):
    res = set()
    for entreno in lista:
        res.add(entreno.tipo)
    return sorted(res)



def entrenos_duracion_superior(lista, numero):
    res = []
    for entreno in lista:
        if entreno.duracion > numero:
            res.append(entreno)
    return res



def suma_calorias(lista, fecha_inicio, fecha_final):
    fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y %H:%M")
    fecha_final = datetime.strptime(fecha_final, "%d/%m/%Y %H:%M")
    res = 0
    for entrenos in lista:
        if fecha_inicio <= entrenos.fechahora <= fecha_final:
            res += entrenos.calorias
    return res