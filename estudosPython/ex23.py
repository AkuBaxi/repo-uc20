#Faça um programa que leia um número e mostre na tela cada um dos digitos separados.
#EX:
#Digite um número: 1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1

numero = input("Digite um número: ")
numero = numero.zfill(4)
milhar = numero[0]
centena = numero[1]
dezena = numero[2]
unidade = numero[3]
print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)