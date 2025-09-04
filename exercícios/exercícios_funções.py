
# 1. Crie uma função chamada `saudacao` que imprime na tela a mensagem **"Olá, bem-vindo ao Python!"**. 
# Em seguida, chame a função no programa.

def saudacao():
   print("Olá, tudo bem?") # o ideal é usar o return para passar a informação que a função pretende

saudacao()

# 2. Crie uma função chamada `dobro` que recebe um número como parâmetro e retorna o dobro desse número.
# Teste chamando a função com diferentes valores.

num1 = int(input("Digite um número: "))

def dobro(num):
      return num*2

print("O dobro do número indicado é", (dobro(num1)))
   
# 3. Crie uma função chamada `soma` que receba dois números e retorne a soma deles. 
# Depois, use a função para somar **10 + 20**.

numb1 = int(input(""))


# 4. Crie uma função chamada `mensagem` que receba um nome como parâmetro e exiba a mensagem:
#    "Olá, \[nome]!"
#    Caso o nome não seja informado, mostre "Olá, visitante!".


# 5. Crie uma função chamada `operacoes` que receba dois números e retorne **a soma, a subtração e a multiplicação** deles.


# 6. Crie uma função chamada `media` que receba uma quantidade variável de números e retorne a média deles.
   # Teste com 3, 5 e 7 valores diferentes.


# 7. Crie uma função chamada `dados_pessoais` que receba informações de uma pessoa (nome, idade, cidade, etc.) usando `**kwargs` 
# e imprima cada dado em uma linha.
   # Exemplo de chamada:

   #```python
   # dados_pessoais(nome="Ana", idade=25, cidade="Recife")
   #```


# 8. Crie uma função chamada `calculadora` que tenha dentro dela outras funções (`somar`, `subtrair`, `multiplicar`, `dividir`).
   # A função principal deve permitir escolher a operação e retornar o resultado.

'''
9. Crie uma função chamada `aplicar_operacao` que receba dois números e uma função como parâmetros.
    A função deve aplicar a operação recebida (ex: soma, multiplicação). 
    Exemplo:

  python
    def soma(a, b): return a + b
    aplicar_operacao(3, 4, soma)  # deve retornar 7
'''
