'''
## Lista de Exercícios – POO classes e objetos

1. Crie uma classe chamada `Pessoa` que tenha os atributos `nome` e `idade`.
Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.

2. Expanda a classe `Pessoa` para incluir um método `apresentar()` que imprima uma frase como:
`"Olá, meu nome é João e tenho 25 anos."`. Teste o método chamando-o a partir de um objeto.

def apresentar(self):
    print(f"{self.nome} e tenho {self.idade} anos")

3. Crie uma classe `Carro` com os atributos `marca`, `modelo` e `ano`.
Use o método `__init__` para inicializar esses valores. Crie três objetos e mostre suas informações.

4. Usando a classe `Carro`, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano).
Imprima antes e depois da alteração.

5. Crie uma classe `ContaBancaria` com os atributos `titular` e `saldo`.
Adicione um método `depositar(valor)` que aumenta o saldo e um método `sacar(valor)` que diminui o
saldo (se houver saldo suficiente). Teste com depósitos e saques.

6. Modifique a classe `ContaBancaria` para que o método `sacar` retorne `True` se a operação for bem-sucedida
e `False` caso contrário. Teste o retorno e imprima mensagens adequadas.

7. Crie uma classe `Aluno` com atributos `nome` e `nota`.
Depois crie uma classe `Turma` que tenha uma lista de alunos e um método `adicionar_aluno(aluno)`.
Crie alguns objetos `Aluno` e adicione-os à turma.

8. Na classe `Aluno`, implemente o método `__str__` para que, ao imprimir um objeto da classe, apareça algo como:
`"Aluno: Maria - Nota: 9.5"`. Teste imprimindo os objetos.

9. Crie uma classe `Cachorro` com um atributo de classe `especie = "Canis familiaris"`
e atributos de instância `nome` e `idade`. Mostre a diferença entre acessar `especie` pelo objeto e pela classe.

'''
from typing import List


## 1.
class Pessoa:
    def __init__(self, name: str , years: int):
        self.name = name
        self.years = years
## 2.
    def presentation(self):
        print(f"Olá, meu nome é {self.name} e {self.years} anos \n")

Beatriz = Pessoa("Beatriz", 32)
print(Beatriz.name)
print(Beatriz.years)

## 2.
Beatriz.presentation()

## 3.
class Carro:
    def __init__(self, modelo: str, ano: int):
        self.modelo = modelo
        self.ano = ano

Polo = Carro("Polo", 2024)
print(Polo.modelo)
print(Polo.ano)
print("-"*50)
Uno = Carro("Uno", 1999)
print(Uno.modelo)
print(Uno.ano)
print("-"*50)
Fastback = Carro("Fastback", 2025)
print(Fastback.modelo)
print(Fastback.ano)
print("-"*50)

## 4.
Fastback.ano = 2024
print(Fastback.ano)

## 5. Crie uma classe `ContaBancaria` com os atributos `titular` e `saldo`.

class ContaBancaria():
    def __init__(self, titular: str, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if self.saldo < valor:
            self.saldo += valor

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
        elif self.saldo < valor:
            print("Saldo insuficiente")

Deposito1 = ContaBancaria("AnaBeatriz", 100)
Deposito1.depositar(100)
print (f"Após o seu depósito, seu saldo é {Deposito1.saldo}")

Saque1 = ContaBancaria("AnaBeatriz", 100)
Saque1.sacar(105)

## 6.
class ContaBancaria():
    def __init__(self, titular: str, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo > valor:
            print("Saque bem-secedido")
            return True

        elif self.saldo < valor:
            print("Saque mal-secedido")
            return False

Saque2 = ContaBancaria("AnaBeatriz", 100)
Saque2.sacar(105)

## 7.

class Aluno:
    def __init__(self, name: str , nota: float):
        self.name = name
        self.nota = nota

class Turma:
    def __init__(self):
        self.alunos = []

    Aluno1 = Aluno("José, ", 10.0)
    print(Aluno1.name, Aluno1.nota)
    Aluno2 = Aluno("Gabriela, ", 7.5)
    print(Aluno2.name, Aluno2.nota)
    Aluno3 = Aluno("Maria, ", 9.0)
    print(Aluno3.name, Aluno3.nota)

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)


turma = Turma()
turma.listar_alunos()

#8. Na classe `Aluno`, implemente o método `__str__` para que, ao imprimir um objeto da classe, 
# apareça algo como:
#`"Aluno: Maria - Nota: 9.5"`. Teste imprimindo os objetos.

#9. Crie uma classe `Cachorro` com um atributo de classe `especie = "Canis familiaris"`
#e atributos de instância `nome` e `idade`. Mostre a diferença entre acessar `especie` pelo objeto e pela classe.