#1.Na classe, ContaBancaria, converta saldo para uma atributo privado. 
# Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica 
# (Ex: saldo não pode ser negativo)

class ContaBancaria:
    def __init__(self, titular: str, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("Saldo não pode ser negativo.")
        else:
            self.__saldo = novo_saldo
            print(f"Saldo atualizado para R${novo_saldo} com sucesso.")
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor do depósito deve ser positivo.")
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque ou valor inválido.")


#2. Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. 
# Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores

class Pessoa:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, identidade: str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf  # Atributo privado
        self.__identidade = identidade  # Atributo privado

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf
        print(f"CPF atualizado para {novo_cpf} com sucesso.")

    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade
        print(f"Identidade atualizada para {nova_identidade} com sucesso.")