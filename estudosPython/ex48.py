#Faça um programa que calcule a soma de todos os números impares que são multiplos de 3 e que esteja entre 1 e 500.

soma = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i

print(f"A soma de todos os números ímpares que são múltiplos de 3 entre 1 e 500 é: {soma}")