nombre = input("Ingresa tu nombre: ")

edad =int(input("Ingresa tu edad: "))

nota1=int(input("Ingresa tu nota 1: "))

nota2=int(input("Ingresa tu nota 2: "))

nota3=int(input("Ingresa tu nota 3: "))

nota4=int(input("Ingresa tu nota 4: "))

import datetime


def conteo(func):
    def wrapper(*args):
        cantidad_parametros = len(args)

        if cantidad_parametros > 1:
            resultado = func(*args)
            print(f"La función '{func.__name__}' fue ejecutada.")
            return resultado
        else:
            print("Necesitas pasar más de un parámetro para ejecutar la función.")
            return None

    return wrapper


@conteo
def registrar_persona(edad, nombre):
    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    print(f"Nombre: {nombre}, Edad: {edad}, Hora: {hora}, Minuto: {minuto}")


@conteo
def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"La media de las notas es: {media:.2f}")
    return media



registrar_persona(edad, nombre)
calcular_media(nota1, nota2, nota3, nota4)
