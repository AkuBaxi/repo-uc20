#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço do produto: "))
print("Formas de pagamento:")
print("1 - À vista dinheiro/cheque")
print("2 - À vista no cartão")
print("3 - Em até 2x no cartão")
print("4 - 3x ou mais no cartão")

opcao = int(input("Escolha a opção de pagamento (1/2/3/4): "))

if opcao == 1:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print(f"Preço final: R${preco_final:.2f} (10% de desconto)")
elif opcao == 2:
    desconto = preco * 0.05
    preco_final = preco - desconto
    print(f"Preço final: R${preco_final:.2f} (5% de desconto)")
elif opcao == 3:
    preco_final = preco
    print(f"Preço final: R${preco_final:.2f} (sem desconto)")
elif opcao == 4:
    juros = preco * 0.20
    preco_final = preco + juros
    print(f"Preço final: R${preco_final:.2f} (20% de juros)")
else:
    print("Opção inválida.")