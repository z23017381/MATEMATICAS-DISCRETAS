# -*- coding: utf-8 -*-
"""
Creado el viernes 9 de febrero del 2024

Autor: zS23017381

Escribe un programa que genere un numero aleatorio y adivine el numero
entre el 1 y 100 y adivina el número

"""

import random

numero = random.randrange(10)


print (numero)

while True:
    valor = int (input("Adivina el numero: "))   
    if valor == numero:
            print ("Adivinaste")
            break
        
        
    