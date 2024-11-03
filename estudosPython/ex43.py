#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5 : Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#Entre 25 até 30: Sobrepeso
#Entre 30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = "Abaixo do peso"
elif 18.5 <= imc < 25:
    status = "Peso ideal"
elif 25 <= imc < 30:
    status = "Sobrepeso"
elif 30 <= imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade mórbida"

print(f"Seu IMC é: {imc:.2f}")
print(f"Status: {status}")