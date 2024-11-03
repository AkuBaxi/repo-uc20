#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos.

total_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(4):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    total_idade += idade

    if sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = total_idade / 4

print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Nome do homem mais velho: {homem_mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")