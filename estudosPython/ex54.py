#Crie um programa que leia o ano de nascimento de 7 pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maioridade = 18
nao_maiores = 0
maiores = 0

for i in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i + 1}: "))
    idade = 2023 - ano_nascimento
    if idade < maioridade:
        nao_maiores += 1
    else:
        maiores += 1

print(f"Quantidade de pessoas que ainda não atingiram a maioridade: {nao_maiores}")
print(f"Quantidade de pessoas que já são maiores: {maiores}")