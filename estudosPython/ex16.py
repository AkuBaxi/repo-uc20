#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#ex:
#Digite um número 6.127
#O número 6.127 tem a parte inteira 6.

import math

numero = float(input("Digite um número: "))
parte_inteira = math.floor(numero)

print(f"O número {numero} tem a parte inteira {parte_inteira}.")