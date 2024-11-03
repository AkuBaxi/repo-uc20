# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar . Considere US$1,00 = R$3.27

money = float(input("Digite quanto de dinheiro em reais você tem: "))

cotacao = 3.27 
dolar = money/cotacao

print(f"Você pode comprar aproximadamente US${dolar:.2f} com R${money:.2f}.")
