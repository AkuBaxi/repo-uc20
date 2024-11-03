# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

numero = int(input("Digite um número inteiro: "))

print(f"Tabuada do {numero}:")
for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")