#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezez aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input("Digite uma frase: ")
quantidade_a = frase.count('A') + frase.count('a')
primeira_posicao = frase.lower().find('a')
ultima_posicao = frase.lower().rfind('a')
print("Quantidade de 'A':", quantidade_a)
print("Primeira posição:", primeira_posicao)
print("Última posição:", ultima_posicao)