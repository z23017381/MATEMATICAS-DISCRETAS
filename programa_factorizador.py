# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:44:49 2024

Escribe un programa que muestre todos los factores de un número entero n


@author: zS23017381
"""

def factores(n):
    for i in range(2, n + 1):
        while n % i == 0:
            print(i)
            n //= i
        if n == 0:
            break
        

try: 
    num = int(input("ingresa un numero: "))
    factores(num)
except Exception:
    print("ingresa un numero entero")