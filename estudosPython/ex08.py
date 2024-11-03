#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input("Digite o valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"{metros} metros é igual a:")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")