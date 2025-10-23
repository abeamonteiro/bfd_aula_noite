# Exercícios de Dicionários em Python

## 1. Crie um dicionário simples
## Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.
dicionario_simples = {
    "nome": "Erica",
    "idade": 41,
    "nota": 10
}

## 2. Acessando valores
#Dado o dicionário:
#produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
# Imprima o nome do produto e a quantidade em estoque.

produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print(produto["nome"])
print(produto["estoque"])   

# 3. Adicionando novos pares chave-valor

#Dado o dicionário:
#pessoa = {"nome": "Carlos", "idade": 30}
#Adicione uma nova chave "cidade" com valor "São Paulo".
dicionario_pessoa = {"nome": "Manoel", "idade": 12}
print(dicionario_pessoa)

dicionario_pessoa["cidade"] = "Recife"
print(dicionario_pessoa)

# 4. Removendo elementos

#Dado o dicionário:
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
#Remova a chave "ano" do dicionário.
carro.pop("ano")
#ou 
#del carro["ano"]
print(carro)

# 5. Verificando existência de uma chave
#Verifique se a chave "telefone" existe no dicionário:

contato = {"nome": "Ana", "email": "ana@email.com"}
#print("telefone" in contato)  # Retorna False
print(contato.get("telefone"))  

# 6. Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.

def contagem_frutas(lista_frutas):
    contagem = {}
    for fruta in lista_frutas:
        if fruta in contagem:
            contagem[fruta] += 1
        else:
            contagem[fruta] = 1
    return contagem

frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
lista_contagem = contagem_frutas(frutas)
print(lista_contagem)

# 7. Invertendo um dicionário
# Dado o dicionário:
d = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
d_invertido = {valor: chave for chave, valor in d.items()}
print(d_invertido)

# 8. Dicionário com listas
# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. 
# Depois, imprima a média de cada aluno.
listas_notas = {
    "Cecilia": [8, 7, 9],
    "Marilia": [6, 5, 7],
    "Renata": [9, 8, 10]
}

for aluno, notas in listas_notas.items():
    media = sum(notas) / len(notas)
    print(f"Média de {aluno}: {media}")

# 9. Mesclando dois dicionários
# Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. 
# Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 3, "c": 4}

def mesclar_dicionarios(dic1, dic2):
    dicionario_mesclado = dic1.copy()
    dicionario_mesclado.update(dic2)
    return dicionario_mesclado

dicionario_mesclado = mesclar_dicionarios(dicionario1, dicionario2)
print(dicionario_mesclado)

# 10. Ordenando dicionário por valor
# Dado o dicionário:
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
for aluno, pontuacao in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
    print(f"{aluno}: {pontuacao}")
