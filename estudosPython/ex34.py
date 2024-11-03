#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input("Digite o salário do funcionário: "))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"O aumento é: R$ {aumento:.2f}")
print(f"O novo salário é: R$ {novo_salario:.2f}")