#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome_completo = input("Digite seu nome completo: ")

# O nome com todas as letras maiúsculas
print("Nome em maiúsculas:", nome_completo.upper())

# O nome com todas as letras minúsculas
print("Nome em minúsculas:", nome_completo.lower())

# Quantas letras ao todo (sem considerar espaços)
total_letras = len(nome_completo.replace(" ", ""))
print("Total de letras (sem espaços):", total_letras)

# Quantas letras tem o primeiro nome
primeiro_nome = nome_completo.split()[0]
quantidade_primeiro_nome = len(primeiro_nome)
print("Quantidade de letras do primeiro nome:", quantidade_primeiro_nome)