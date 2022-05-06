""" *****************************************
    Universidad del Valle de Guatemala
    Teoría de Probabilidades sección 10
    Miembros:
    Alejandro Gómez - 20347
    Diego Córdova - 20212
    Cristian Aguirre - 20231
    Paola de León - 20361
    Paola Contreras - 20213
    Marco Jurado - 20308
    ***************************************** """

from numpy.random import *

# Imports para el título
import time
import sys

variablemenu = 0

# Funcion para verificar si lo ingresado es un numero
def verificarNum(input):
    try:
        val = float(input)
        return val
    except ValueError:
        try:
            val = int(input)
            return val
        except ValueError:
            print("¡Solamente números!")


def Ejercicio1():
    opciones = ["Carro", "Cabra"]
    probabilidades = [2 / 3, 1 / 3]
    probabilidades2 = [1 / 3, 2 / 3]

    x = choice(
        a=opciones, size=100000, replace=True, p=probabilidades
    )  # no cambia de puerta
    y = choice(
        a=opciones, size=100000, replace=True, p=probabilidades2
    )  # si cambia de puerta

    Carro1 = list(x).count("Carro")
    Cabra1 = list(x).count("Cabra")
    print("\nCaso: cambia puerta")
    print(f"probCarro: {Carro1}\nprobCabra: {Cabra1} \n")
    porCarro1 = round(((list(x).count("Carro") / len(x)) * 100), 2)
    porCarro2 = round(((list(x).count("Cabra") / len(x)) * 100), 2)
    print(f"probCarro: {porCarro1}%\nprobCabra: {porCarro2}%\n")

    Carro2 = list(y).count("Carro")
    Cabra2 = list(y).count("Cabra")
    print("Caso: mantiene puerta")
    print(f"probCarro: {Carro2}\nprobCabra: {Cabra2}\n")
    porCarro3 = round(((list(y).count("Carro") / len(y)) * 100), 2)
    porCarro4 = round(((list(y).count("Cabra") / len(y)) * 100), 2)
    print(f"probCarro: {porCarro3}%\nprobCabra: {porCarro4}%\n")


def Ejercicio2():

    opciones = random(size=3)
    x = choice(a=opciones, size=1000000, replace=True)

    print(x)


# --------------- Main -------------------

Bienvenida = "\n----- Bienvenido al Lab 8 ----\n"


# Se imprime el titulo de forma ¡chilerisima!
for i in Bienvenida:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)

# Mensaje de despedida
def bye():
    print("¡Gracias por usar el programa!!")


dict_menu = {
    1: Ejercicio1,
    2: Ejercicio2,
    3: bye,
}

while variablemenu != 3:
    variablemenu = input(
        "\nIngrese una opcion\n1. Ejercicio 1\n2. Ejercicio 2\n3. ¡Salir!-> "
    )
    variablemenu = verificarNum(variablemenu)
    accion = dict_menu[variablemenu]
    accion()
