# Guia Completo de Exceções em Python

## Sumário
1. [Introdução às Exceções](#introdução-às-exceções)
2. [Tratamento de Exceções Específicas](#tratamento-de-exceções-específicas)
3. [Código Interativo de Demonstração](#código-interativo-de-demonstração)

## Introdução às Exceções

Em Python, exceções são eventos que ocorrem durante a execução de um programa que interrompem o fluxo normal de instruções. O tratamento adequado de exceções é fundamental para criar programas robustos e confiáveis.

## Tratamento de Exceções Específicas

### 1. ValueError
Ocorre quando uma função recebe um argumento com o tipo correto, mas valor inadequado.

```python
# Exemplo completo de ValueError
try:
    # Tentando converter uma letra em número
    numero = int("abc")
except ValueError as e:
    print("Erro: Não é possível converter 'abc' em número")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: solicitar um novo valor
    numero = 0  # Valor padrão em caso de erro
```

### 2. TypeError
Acontece quando uma operação é realizada em um objeto de tipo inadequado.

```python
# Exemplo completo de TypeError
try:
    # Tentando concatenar string com número
    texto = "Idade: "
    numero = 25
    resultado = texto + numero
except TypeError as e:
    print("Erro: Não é possível concatenar texto com número diretamente")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: converter o número para string
    resultado = texto + str(numero)
```

### 3. IndexError
Ocorre ao tentar acessar um índice que não existe em uma sequência.

```python
# Exemplo completo de IndexError
try:
    # Tentando acessar um índice inexistente
    lista = [1, 2, 3]
    elemento = lista[10]
except IndexError as e:
    print(f"Erro: A lista só tem {len(lista)} elementos (índices 0 a {len(lista)-1})")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: usar o último elemento disponível
    elemento = lista[-1]  # Pega o último elemento
```

### 4. KeyError
Acontece ao tentar acessar uma chave que não existe em um dicionário.

```python
# Exemplo completo de KeyError
try:
    # Tentando acessar uma chave inexistente
    dicionario = {"nome": "João", "idade": 25}
    endereco = dicionario["endereço"]
except KeyError as e:
    print("Erro: Chave 'endereço' não encontrada no dicionário")
    print(f"Chaves disponíveis: {list(dicionario.keys())}")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: usar um valor padrão
    endereco = "Não informado"
```

### 5. FileNotFoundError
Ocorre quando tentamos abrir um arquivo que não existe.

```python
# Exemplo completo de FileNotFoundError
try:
    # Tentando abrir um arquivo inexistente
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError as e:
    print("Erro: O arquivo solicitado não foi encontrado")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: criar o arquivo
    with open("arquivo_inexistente.txt", "w") as arquivo:
        arquivo.write("Novo arquivo criado")
    conteudo = "Arquivo criado pois não existia"
```

### 6. ZeroDivisionError
Acontece quando tentamos dividir um número por zero.

```python
# Exemplo completo de ZeroDivisionError
try:
    # Tentando dividir por zero
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print("Erro: Não é possível dividir por zero")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: usar um valor muito grande ou retornar None
    resultado = float('inf')  # Infinito
```

### 7. AttributeError
Ocorre ao tentar acessar um atributo ou método que não existe.

```python
# Exemplo completo de AttributeError
try:
    # Tentando acessar um método inexistente
    texto = "Hello"
    texto.capitalizar()  # Método correto seria capitalize()
except AttributeError as e:
    print("Erro: O método 'capitalizar' não existe para strings")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: usar o método correto
    texto = texto.capitalize()
```

### 8. NameError
Acontece quando tentamos usar uma variável que não foi definida.

```python
# Exemplo completo de NameError
try:
    # Tentando usar uma variável não definida
    print(variavel_nao_definida)
except NameError as e:
    print("Erro: A variável não foi definida anteriormente")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: definir a variável com valor padrão
    variavel_nao_definida = None
```

### 9. OverflowError
Ocorre quando uma operação produz um número muito grande.

```python
# Exemplo completo de OverflowError
try:
    # Tentando calcular um número muito grande
    import math
    resultado = math.exp(1000)
except OverflowError as e:
    print("Erro: O resultado é grande demais para ser representado")
    print(f"Mensagem de erro original: {e}")
    # Tratamento do erro: usar um valor limite máximo
    resultado = float('inf')
```

### Combinando Múltiplas Exceções

Às vezes, queremos tratar diferentes exceções de maneiras diferentes:

```python
try:
    # Código que pode gerar diferentes tipos de erro
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError as e:
    print("Erro: Por favor, digite apenas números")
except ZeroDivisionError as e:
    print("Erro: O número não pode ser zero")
except Exception as e:
    print("Erro inesperado:", e)
else:
    print("Operação realizada com sucesso!")
finally:
    print("Execução finalizada")
```

## Boas Práticas no Tratamento de Exceções

1. **Seja Específico**
   - Capture apenas as exceções que você espera
   - Evite usar `except:` sem especificar o tipo de exceção

2. **Use o else**
   - O bloco `else` é executado quando nenhuma exceção ocorre
   - Útil para separar o código que pode gerar exceções do código que só deve executar em caso de sucesso

3. **Use o finally**
   - O bloco `finally` sempre é executado, independente de ter ocorrido exceção ou não
   - Útil para limpeza de recursos (fechar arquivos, conexões de banco de dados, etc.)

4. **Não Silencie Exceções**
   - Sempre faça algo significativo ao capturar uma exceção
   - No mínimo, registre o erro em um log

5. **Crie Exceções Personalizadas**
```python
class MeuErroPersonalizado(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# Uso
try:
    raise MeuErroPersonalizado("Algo deu errado!")
except MeuErroPersonalizado as e:
    print(f"Erro personalizado: {e}")
```

## Conclusão

O tratamento adequado de exceções é uma parte crucial da programação em Python. Cada tipo de exceção tem seu propósito específico e entender como tratá-las apropriadamente ajuda a criar código mais robusto e confiável.

Lembre-se:
- Exceções não são necessariamente ruins - elas são ferramentas para lidar com situações excepcionais
- O tratamento adequado de exceções torna seu código mais resiliente
- Use exceções para melhorar a legibilidade e manutenibilidade do código
- Sempre documente como e por que você está tratando cada exceção
