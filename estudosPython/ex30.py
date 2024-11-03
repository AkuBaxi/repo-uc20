#Crie um programa que leia o número inteiro e mostre na tela se ele é PAR ou IMPAR

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é IMPAR.")