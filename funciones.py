import numpy
import os
import time
os.system("cls")

guarderia = numpy.zeros((2,5), int)
lista_ruts = []
lista_nombres = []
lista_nombres_mascotas = []
lista_identificador = []
lista_dias = []
lista_reserva = []
lista_filas = []
lista_columnas = []

contador = 0



def mostrar_menu():
    print("""
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir """)

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut (sin puntos ni dígito verificador)"))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! el rut debe estar entre 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_nombre_mascota():
    while True:
        nombre_m = input("ingrese el nombre de su mascota")
        if len(nombre_m.strip()) >= 3 and nombre_m.isalpha():
            return nombre_m
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS  LETRAS")

def validar_dias():
    while True:
        try:
            dias_mascota = int(input("ingrese la cantidad de dias que se quedará su mascota"))
            if dias_mascota >= 1:
                return dias_mascota
            else:
                print("ERROR! DEBE INGRESAR UNA CANTIDAD DE DÍAS VALIDA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")
    
def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese el número fila(1-2): "))
            if fila >= 1 and fila <= 2:
                return fila
            else:
                print("ERROR! FILA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")           

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese el número de la columna(1-5): "))
            if columna >= 1 and columna <= 5:
                return columna
            else:
                print("ERROR! COLUMNA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def ver_habitacion():
    print("\t          HABITACIÓN")
    contador + 1
    for x in range(2):
        print(f"piso {x+1}", end=" ")
        for y in range(5):
            print(f"habitación{contador} {x}{y}", end=" ")
        print()

def reservar_habitacion():
    print("\t         HABITACIÓN")
    contador + 1
    lista_reserva = []
    for x in range(2):
        print(f"piso {x+1}", end=" ")
        for y in range(5):
            print(f"habitación{x}{y}", end=" ")
        print()


def datos_guardados():
    rut = validar_rut()
    nombre = validar_nombre()
    nombre_mascota = validar_nombre_mascota()
    dias = validar_dias()

    guarderia = ver_habitacion()
    reserva = reservar_habitacion()

    lista_ruts.append(rut)
    lista_nombres.append(nombre)
    lista_nombres_mascotas.append(nombre_mascota)
    lista_dias.append(dias)

   
def buscar_mascota():
    rut = validar_rut
    lista_ruts.index(rut)
    
    
















