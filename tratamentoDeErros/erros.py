def demonstrar_valor_error():
    """Demonstra ValueError ao tentar converter texto em número"""
    try:
        numero = int("abc")
    except ValueError as e:
        print("\nValorError detectado!")
        print("Causa: Tentativa de converter 'abc' em número")
        print(f"Erro original: {e}")

def demonstrar_type_error():
    """Demonstra TypeError ao tentar concatenar tipos incompatíveis"""
    try:
        resultado = "texto" + 42
    except TypeError as e:
        print("\nTypeError detectado!")
        print("Causa: Tentativa de concatenar string com número")
        print(f"Erro original: {e}")

def demonstrar_index_error():
    """Demonstra IndexError ao acessar índice inexistente"""
    try:
        lista = [1, 2, 3]
        elemento = lista[10]
    except IndexError as e:
        print("\nIndexError detectado!")
        print(f"Causa: Tentativa de acessar índice 10 em uma lista de {len(lista)} elementos")
        print(f"Erro original: {e}")

def demonstrar_key_error():
    """Demonstra KeyError ao acessar chave inexistente em dicionário"""
    try:
        dicionario = {"nome": "João", "idade": 25}
        valor = dicionario["endereço"]
    except KeyError as e:
        print("\nKeyError detectado!")
        print("Causa: Tentativa de acessar chave 'endereço' que não existe no dicionário")
        print(f"Chaves disponíveis: {list(dicionario.keys())}")
        print(f"Erro original: {e}")

def demonstrar_file_not_found_error():
    """Demonstra FileNotFoundError ao tentar abrir arquivo inexistente"""
    try:
        arquivo = open("arquivo_inexistente.txt", "r")
    except FileNotFoundError as e:
        print("\nFileNotFoundError detectado!")
        print("Causa: Tentativa de abrir arquivo que não existe")
        print(f"Erro original: {e}")

def demonstrar_zero_division_error():
    """Demonstra ZeroDivisionError ao tentar dividir por zero"""
    try:
        resultado = 10 / 0
    except ZeroDivisionError as e:
        print("\nZeroDivisionError detectado!")
        print("Causa: Tentativa de divisão por zero")
        print(f"Erro original: {e}")

def demonstrar_attribute_error():
    """Demonstra AttributeError ao tentar acessar método inexistente"""
    try:
        texto = "Hello"
        texto.metodo_inexistente()
    except AttributeError as e:
        print("\nAttributeError detectado!")
        print("Causa: Tentativa de acessar método que não existe em string")
        print(f"Erro original: {e}")

def demonstrar_name_error():
    """Demonstra NameError ao usar variável não definida"""
    try:
        print(variavel_nao_definida)
    except NameError as e:
        print("\nNameError detectado!")
        print("Causa: Tentativa de usar variável que não foi definida")
        print(f"Erro original: {e}")

def demonstrar_overflow_error():
    """Demonstra OverflowError com operação matemática muito grande"""
    try:
        import math
        resultado = math.exp(1000)
    except OverflowError as e:
        print("\nOverflowError detectado!")
        print("Causa: Resultado matemático muito grande para ser representado")
        print(f"Erro original: {e}")

def menu_principal():
    """Exibe o menu principal e gerencia a seleção do usuário"""
    while True:
        print("\n=== DEMONSTRAÇÃO DE EXCEÇÕES PYTHON ===")
        print("\nEscolha um erro para demonstrar:")
        print("1. ValueError (converter texto inválido para número)")
        print("2. TypeError (operação entre tipos incompatíveis)")
        print("3. IndexError (acessar índice inexistente)")
        print("4. KeyError (acessar chave inexistente em dicionário)")
        print("5. FileNotFoundError (abrir arquivo inexistente)")
        print("6. ZeroDivisionError (dividir por zero)")
        print("7. AttributeError (acessar método inexistente)")
        print("8. NameError (usar variável não definida)")
        print("9. OverflowError (número muito grande)")
        print("0. Sair")

        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
            
            if opcao == 0:
                print("\nEncerrando o programa...")
                break
                
            funcoes = {
                1: demonstrar_valor_error,
                2: demonstrar_type_error,
                3: demonstrar_index_error,
                4: demonstrar_key_error,
                5: demonstrar_file_not_found_error,
                6: demonstrar_zero_division_error,
                7: demonstrar_attribute_error,
                8: demonstrar_name_error,
                9: demonstrar_overflow_error
            }
            
            if opcao in funcoes:
                funcoes[opcao]()
                input("\nPressione ENTER para continuar...")
            else:
                print("\nOpção inválida! Por favor, escolha um número entre 0 e 9.")
                
        except ValueError:
            print("\nPor favor, digite apenas números!")

if __name__ == "__main__":
    menu_principal()