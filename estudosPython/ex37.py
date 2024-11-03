#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

numero = int(input("Digite um número inteiro: "))
print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
opcao = int(input("Digite a opção (1/2/3): "))

if opcao == 1:
    print(f"{numero} em binário é: {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} em octal é: {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} em hexadecimal é: {hex(numero)[2:]}")
else:
    print("Opção inválida! Por favor, escolha 1, 2 ou 3.")