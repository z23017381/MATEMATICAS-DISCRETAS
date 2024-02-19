# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:19:27 2024

escribe un programa que indique si un numero es primo

@author: zS23017381
"""

numero = int(input("ingrese un valor: "))

for r in range(2, numero + 1):
    primo = True 
    for i in range(2, (r//2)+1):
        if (r % i == 0 ):
            primo = False
            break
    if (primo):
        print(f"(r)")
        
        
        