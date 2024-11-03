#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente  de um triangulo retângulo,
#calcule e mostre o comprimento da hipotenusa

import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print(f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")