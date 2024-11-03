#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 20 anos: Sênior
#Acima: Master

from datetime import datetime

ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Junior"
elif idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"

print(f"Categoria: {categoria}")