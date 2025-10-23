# Lista de Exercícios: Função lambda (map, filter, reduce, sorted)

## 1. Dobro dos números (map + lambda)
   # Dada a lista `[1, 2, 3, 4, 5]`, use `map` com `lambda` para gerar uma nova lista com o dobro de cada número.
lista = [1,2,3,4,5]
print(list(map(lambda num:num*2, lista)))

## 2. Filtrar pares (filter + lambda)
   # Dada a lista `[10, 15, 20, 25, 30]`, use `filter` com `lambda` para obter apenas os números pares.
lista2 = [10, 15, 20, 25, 30]
print(list(filter(lambda num:num%2==0, lista2)))

## 3. Soma dos números (reduce + lambda)
   # Usando `reduce`, some todos os números da lista `[1, 2, 3, 4, 5]`.
from functools import reduce
print(reduce(lambda x, y : x+y, lista))

## 4. Ordenação por comprimento da palavra (sorted + lambda)
   # Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando `sorted` e `lambda`.
frutas = ["uva", "banana", "maçã", "laranja"]
frutas_ordenadas = sorted(frutas, key=lambda x:x)
print(frutas_ordenadas)

## 5. Primeira letra maiúscula (map + lambda)
    # Dada a lista `["ana", "pedro", "maria"]`, use `map` e `lambda` para transformar em `["Ana", "Pedro", "Maria"]`.
nomes = ["ana", "pedro", "maria"]
print(list(map(lambda x: x.capitalize(), nomes)))

## 6. Produto dos números (reduce + lambda)
    # Usando `reduce`, calcule o produto (multiplicação) de todos os elementos da lista `[2, 3, 4, 5]`.
lista3 = [2, 3, 4, 5]
print(reduce(lambda x, y: x*y, lista3))

## 7. Ordenar por último caractere (sorted + lambda)
   # Dada a lista `["banana", "uva", "maçã", "laranja"]`, ordene as palavras pelo último caractere.

# observação: visto que todas as palavras da lista sugerida terminam com a mesma letra,
# foi criado código solicitando a ordenação da lista de frutas com base na terceira letra
# de trás para frente de cada string;

frutas2 = ["banana", "uva", "maçã", "laranja"]
ordenadas2 = sorted(frutas2, key=lambda x: x[-3])
print(ordenadas2)