# 1. Escreva um programa que peça ao usuário para digitar um número. 
# Trate o erro caso ele digite algo que não seja um número inteiro.

input_numero = input("Digite um número inteiro: ")
try:
    numero_inteiro = int(input_numero)
    print(f"Você digitou o número inteiro: {numero_inteiro}")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")

# 2. Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é {resultado}.")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")

# 3. Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
else:
    print(f"Você digitou o número inteiro: {numero}")

# 4. Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). 
# Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo dados.txt não foi encontrado.")
finally:
    print("Encerrando programa.")
    try:
        arquivo.close()
    except NameError:
        pass  # O arquivo não foi aberto, então não há nada para fechar.
    
# 5. Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

# 6. Crie uma exceção personalizada chamada IdadeInvalidaError. 
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception):

idade = int(input("Digite sua idade: "))
if idade < 0:
    raise IdadeInvalidaError("Idade não pode ser negativa.")


# 7. Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:

    #  ValueError se o usuário digitar algo inválido
    # ZeroDivisionError se tentar dividir por zero
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 / num2
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"O resultado da divisão é {resultado}.")

# 8. Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
    # try para a conversão,
    # else para verificar se é par ou ímpar,
    # finally para exibir "Fim do programa".
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
else:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
finally:
    print("Fim do programa.")   

# 9. Crie uma função sacar(saldo, valor) que:

    # Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
    # Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.
def sacar(saldo, valor):
    class SaldoInsuficienteError(Exception):
        pass

    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
    return saldo - valor
try:
    saldo_atual = 1000
    valor_saque = int(input("Digite o valor que deseja sacar: "))
    novo_saldo = sacar(saldo_atual, valor_saque)
    print(f"Saque realizado com sucesso. Novo saldo: R${novo_saldo}")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
except SaldoInsuficienteError as e:
    print(e)