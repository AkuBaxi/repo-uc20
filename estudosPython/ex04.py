#Faça um programa que leia algo pelo teclado e mostre na tela do seu tipo primitivo e todas as informações possíveis sobre ele

valor = input("Digite algo: ")

# Verificação do tipo primitivo
if valor.isdigit():
    print("O valor é um número inteiro.")
elif valor.replace('.', '', 1).isdigit():
    print("O valor é um número real.")
elif valor.isalpha():
    print("O valor é uma string.")
else:
    print("O valor é de um tipo desconhecido.")

# Informações adicionais
print("Tipo primitivo:", type(valor))
print("Tamanho:", len(valor))
print("Maiúsculas:", valor.upper())
print("Minúsculas:", valor.lower())
print("Título:", valor.title())
print("Invertido:", valor[::-1])