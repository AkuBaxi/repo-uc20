#Crie um programa que leie uma frase qualquer e diga se ela é um palindromo desconsiderando os espaços.

frase = input("Digite uma frase: ")
frase_sem_espacos = frase.replace(" ", "").lower()
if frase_sem_espacos == frase_sem_espacos[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")