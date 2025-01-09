from entrenos import *

def prueba_lectura(ruta):
    print(f"Los tres primeros entrenos del archivo '{ruta}' son: \n {lee_entrenos(ruta)[:3]}")
    print()
    print(f"Los tres últimos entrenos del archivo '{ruta}' son: \n {lee_entrenos(ruta)[-3:]}")


entrenos = lee_entrenos("data\entrenos.csv")


def prueba_tipos(ruta):
    print(f"Los tipos de entrenos son: \n {tipos_de_entrenos(entrenos)}")


def prueba_duracion(numero):
    print(f"Los entrenos que duran más que {numero} son: \n {entrenos_duracion_superior(entrenos, numero)}")


def prueba_calorias(fecha_inicial, fecha_final):
    print(f"Las calorías quemadas entre las fechas {fecha_inicial} - {fecha_final} son:\n {suma_calorias(entrenos,fecha_inicial,fecha_final)}")



if __name__ == '__main__':
    #prueba_lectura("data\entrenos.csv")
    #prueba_tipos("data\entrenos.csv")
    #duracion = int(input("Dime la duración mínima del entreno: "))
    #prueba_duracion(duracion)
    prueba_calorias("9/7/2019 23:13", "19/7/2020 15:03")
