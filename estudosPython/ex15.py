#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

custo_por_dia = 60.00
custo_por_km = 0.15

dias_alugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km_percorridos = float(input("Digite a quantidade de Km percorridos: "))

preco_total = (dias_alugados * custo_por_dia) + (km_percorridos * custo_por_km)

print(f"O preço total a pagar é: R${preco_total:.2f}")