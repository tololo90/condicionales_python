#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "tololo90"
__email__ = "tololo90@gmail.com"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if (numero_1 > numero_2):
        print(f"{numero_1} es mayor que {numero_2}")
    elif (numero_2 > numero_1):
        print(f"{numero_2} es mayor que {numero_1}")
    else:
        print("los  dos numeros son iguales")
    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    if (numero_1 > 0):
        print(f"{numero_1} es positivo")
    elif (numero_1 < 0):
        print(f"{numero_1} es negativo")
    else:
        print (f"el numero es {numero_1}")

    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición
    if (numero_1 > 0 and numero_1 < 100):
        print(f"el numero {numero_1} es mayor que 0 y menor que 100")
    else:
        print((f"el numero {numero_1} no cumple las dos condiciones: "
                "ser mayor que 0 y menor que cien"))
    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición
    if (numero_1 < 10 or numero_2 > -2):
        print(("se cumplen una o dos de las dos condiciones: "
              f"{numero_1} es menor a diez o {numero_2} es mayor a -2"))
    else:
        print(f"{numero_1} no es menor a 10 y no es mayor a -2")


def ej2():

    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    if (texto_1 > texto_2):
        print(f"{texto_1} es mayor que {texto_2}")
    elif (texto_2 > texto_1):
        print(f"{texto_2} es mayor que {texto_1}")
    else:
        print("las palabras son iguales")
    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    letras_1 = len(texto_1)
    letras_2 = len(texto_2)

    if (letras_1 > letras_2):
        print(f"{texto_1} tiene mas letras que {texto_2}")
    elif (texto_2 > texto_1):
        print(f"{texto_2} tiene mas letras que {texto_1}")
    else:
        print(f"{texto_1} tiene la misma cantidad"
              f" de letras que {texto_2}")

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    primer_letra = texto_1[0]
    primer_letra_2 = texto_2[0]
    if(primer_letra > primer_letra_2):
        print(f"{primer_letra} es mayor a {primer_letra_2}")
    elif(primer_letra_2 > primer_letra):
        print(f"{primer_letra_2} es mayor a {primer_letra}")
    else:
        print(f"{primer_letra} es igual a {primer_letra_2}")

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    if(copia_texto_1 == texto_1):
        print(f"{copia_texto_1} es igual a {texto_1}")
    else:
        print(F"{copia_texto_1} no es igual a {texto_1}")
    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    if(copia_texto_1 != texto_2):
        print(f"{copia_texto_1} no es igual a {texto_2}")
    else:
        print(f"{copia_texto_1} es igual a {texto_2}")


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"
    if(numero_1 > 5):
        if(numero_2 > 0):
            print("resp=1")
        else:
            print("resp=2")
    else:
        if(numero_2 > 5):
            print("resp=3")
        else:
            print("resp=4")

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if(puntaje >= 90):
        print("A")
    elif(puntaje >= 80):
        print("B")
    elif(puntaje >= 70):
        print("C")
    elif(puntaje >= 60):
        print("D")
    else:
        print("F")


def ej4():
    # Ejemplos variables de texto

    texto_1 = '9'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda
    if(texto_1 > texto_2):
        print(f"{texto_1} es mayor que {texto_2}")
    elif(texto_2 > texto_1):
        print(f"{texto_2} es mayor que {texto_1}")
    else:
        print(f"{texto_1} es igual a {texto_2}")
    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    convertir_1 = int(texto_1)
    convertir_2 = int(texto_2)

    if(convertir_1 > convertir_2):
        print(f"{convertir_1} es mayor que {convertir_2}")
    elif(convertir_2 > convertir_1):
        print(f"{convertir_2} es mayor que {convertir_1}")
    else:
        print(f"{convertir_1} es igual a {convertir_2}")

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
