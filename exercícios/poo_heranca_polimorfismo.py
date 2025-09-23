# 1. Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. 
# Crie uma instancia de um cliente e acesse todos os atributos.
# 2. Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. 
# Mostre como chamar o método herdado a partir de um objeto Cliente.
# 3. Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". 
# Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
# 4. Na classe Cliente, adicione o atributo saldo. 
# Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().


class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
    def exibir_informacoes(self): #2ª questão
        return f"Nome: {self.nome}, Email: {self.email}"
    def saudacao(self): # 3ª questão
        return "Olá, usuário"
    
class Cliente(Usuario):
    def __init__(self, nome: str, email: str, cliente_id: int, saldo=0): # 4ª questão
        super().__init__(nome, email)
        self.cliente_id = cliente_id
        self.saldo = saldo
    def saudacao(self): # 3ª questão
        return "Olá, cliente"
    def exibir_informacoes(self): #2ª questão
        usuario_info = super().exibir_informacoes()
        return f"{usuario_info}, Saldo: {self.saldo}, ID: {self.cliente_id}"

cliente = Cliente("Ana Beatriz", "abeatrizbmonteiro@gmail.com", 1)
print(cliente.exibir_informacoes())

print(cliente.saudacao())

# 5. Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. 
# Mostre como instanciar um gerente e acessar seus atributos.
class Funcionario(Usuario):
    def __init__(self, nome: str, email: str, funcionario_id: int):
        super().__init__(nome, email)
        self.funcionario_id = funcionario_id

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, funcionario_id: int, departamento: str):
        super().__init__(nome, email, funcionario_id)
        self.departamento = departamento

gerente = Gerente("Carlos Silva", "carlossilva@empresa.com", 101, "Vendas") # Gerente instanciado
print(f"Gerente: {gerente.nome}, Email: {gerente.email}, ID: {gerente.funcionario_id}, Departamento: {gerente.departamento}") #acesso aos atributos do gerente


# 6. Crie uma classe Autenticacao com um método login(). 
class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "0000":
            return True
        return False
    
# Crie outra classe Permissao com um método verificar_permissao(). 
class Permissao:
    def verificar_permissao(self, usuario):
        if usuario == "admin":
            return True
        return False

# Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?
class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome
admin = Administrador("Super Admin")
print(admin.login("admin", "0000"))  # Usando método de Autenticacao
print(admin.verificar_permissao("admin"))  # Usando método de Permissao


# 7. Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. 
# Se a classe Administrador herda das duas, qual versão de status() será chamada? 
# Use Administrador.__mro__ para mostrar a ordem.

class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "password":
            return True
        return False
    
    def status(self):
        return "Status da Autenticação"

class Permissao:
    def verificar_permissao(self, usuario):
        if usuario == "admin":
            return True
        return False

    def status(self):
        return "Status da Permissão"
    
class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome    
admin = Administrador("Super Admin")
print(admin.status())  # Chama o método status() de Autenticacao devido à ordem
print(Administrador.__mro__)  # Mostra a ordem de resolução de métodos

