#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo sera formado:
#Equilatero: todos os lados são iguais
#Isóceles: dois lados são iguais
#Escaleno: todos os lados diferentes

def verifica_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if verifica_triangulo(lado1, lado2, lado3):
    print("Os lados formam um triângulo.")
    
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
        
    print(f"O tipo de triângulo formado é: {tipo}")
else:
    print("Os lados não formam um triângulo.")