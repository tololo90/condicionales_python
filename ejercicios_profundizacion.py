#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "tololo90"
__email__ = "tololo90@gmail.com"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    print("elija 2 numeros para calcular la diferencia entre ellos")

    numero_1 = int(input("ingrese el primer numero entero \n"))
    numero_2 = int(input("ingreso el segundo numero entero \n"))
    numero_3 = numero_1 - numero_2

    if(numero_3 > 0):
        print(f"la diferencia entre {numero_1} y {numero_2} es "
              f"{numero_3}, que es un numero positivo")
    elif(numero_3 < 0):
        print(f"la diferencia entre {numero_1} y {numero_2} es "
              f"{numero_3}, que es un numero negativo")
    else:
        print(f"la diferencia entre {numero_1} y {numero_2} es "
              f"{numero_3}")


def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    print("elija 3 numeros para verificar si son par o impar")
    numero_1 = int(input("ingrese el primer numero entero \n"))
    numero_2 = int(input("ingrese el segundo numero entero \n"))
    numero_3 = int(input("ingrese el tercer numero entero \n"))
    resultado_numero_1 = numero_1 % 2
    resultado_numero_2 = numero_2 % 2
    resultado_numero_3 = numero_3 % 2

    if(resultado_numero_1 == 0):
        print(f"{numero_1} es par")
    else:
        print(f"{numero_1} es impar")

    if(resultado_numero_2 == 0):
        print(f"{numero_2} es par")
    else:
        print(f"{numero_2} es impar")

    if(resultado_numero_3 == 0):
        print(f"{numero_3} es par")
    else:
        print(f"{numero_3} es impar")


def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al
    programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según
    la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    print("elija 2 numeros para operar entre ellos")
    numero_1 = int(input("ingrese un numero \n"))
    numero_2 = int(input("ingrese otro numero \n"))
    operacion = str(input("elija que operacion desea realizar entre ambos"
                          "numeros\n"
                          "suma (+)\nresta (-)\nmultiplicacion (*)\n"
                          "division (/)\npotencia (**)\n"))
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    division = int(numero_1 / numero_2)
    potencia = numero_1 ** numero_2

    if (operacion == "+"):
        print(f"{numero_1} + {numero_2} = {suma}")
    if (operacion == "-"):
        print(f"{numero_1} - {numero_2} = {resta}")
    if (operacion == "*"):
        print(f"{numero_1} * {numero_2} = {multiplicacion}")
    if (operacion == "/"):
        print(f"{numero_1} / {numero_2} = {division}")
    if (operacion == "**"):
        print(f"{numero_1} ** {numero_2} = {potencia}")


def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como
    quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3
    palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3
    palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    print("ingrese tres palabras para ordenarlas alfabeticamente\n"
          "y por cantidad de letras de mayor a menor")
    palabra_1 = str(input("primer palabra\n"))
    palabra_2 = str(input("segunda palabra\n"))
    palabra_3 = str(input("tercer palabra\n"))
    orden = int(input("¿como le gustaria ordenar las palabras?\n"
                      "ingrese 1 por orden alfabetico\n"
                      "ingrese 2 por cantidad de letras\n"))

    lista = (palabra_1, palabra_2, palabra_3)

    if(orden == 1):
        print(sorted(lista, reverse=True))
    if(orden == 2):
        print(sorted(lista, key=len, reverse=True))


def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    print("ingrese la temperatura maxima de los ultimos 3 dias")
    dia_1 = (int(input("dia 1\n")))
    dia_2 = (int(input("dia 2\n")))
    dia_3 = (int(input("dia 3\n")))
    temp_promedio = int((dia_1 + dia_2 + dia_3)/3)

    if(dia_1 >= dia_2 and dia_1 >= dia_3):
        print(f"{dia_1} es la temperatura mas alta")
    elif(dia_2 >= dia_1 and dia_2 >= dia_3):
        print(f"{dia_2} es la temperatura mas alta")
    else:
        print(f"{dia_3} es la temperatura mas alta")

    if(dia_1 <= dia_2 and dia_1 <= dia_3):
        print(f"{dia_1} es la temperatura mas baja")
    elif(dia_2 <= dia_1 and dia_2 <= dia_3):
        print(f"{dia_2} es la temperatura mas baja")
    else:
        print(f"{dia_3} es la temperatura mas baja")

    print(f"{temp_promedio} es la temperatura promedio")


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
