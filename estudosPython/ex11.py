# Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
litros_tinta = area / 2

print(f"A área da parede é {area} m².")
print(f"A quantidade de tinta necessária é {litros_tinta} litros.")