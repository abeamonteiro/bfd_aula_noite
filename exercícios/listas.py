# 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.

lista_livros_Chimamanda = ["Americanah", "Meio Sol Amarelo","Hibisco Roxo"]
print(lista_livros_Chimamanda)

# 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.

print("O primeiro item da lista é", lista_livros_Chimamanda[0])
print("O último item da lista até agora é", lista_livros_Chimamanda[2])

# 3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.

lista_livros_Chimamanda.append("Notas Sobre o Luto")
print(lista_livros_Chimamanda)

# 4- Insira o livro "Duna" na segunda posição da lista livros usando insert().

lista_livros_Chimamanda.insert(1, "Duna")
print(lista_livros_Chimamanda)

# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".

if "Silencio dos Inocentes" in lista_livros_Chimamanda:
    lista_livros_Chimamanda.remove("Silencio dos Inocentes")
    print(lista_livros_Chimamanda)
else:
    print("Livro não encontrado!")

# 6- Crie uma lista chamada numeros com os valores [1, 2, 3, 2, 4, 2, 5].

numeros = [1, 2, 3, 2, 4, 2, 5]
print(numeros.count(2))

# 7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
for livro in lista_livros_Chimamanda:
    print(f"O livro {livro} é interessante")

# 8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
lista_idades = [12, 18, 25, 14, 30]

for idade in lista_idades:
    if idade >= 18:
       print(idade)

# 9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
lista_valores = [10, 20, 30, 40]

for valor in lista_valores:
    soma = 0
    soma += valor
    
print(soma)
    
# 10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo: notas = [[7, 8, 9], [6, 5, 7]]
# No fim, imprima a média de cada aluno.
n1 = int(input("Digite o valor da primeira nota: ")) #lembrar que o input vai ler como string
n2 = int(input("Digite o valor da segunda nota: "))
n3 = int(input("Digite o valor da terceira nota: "))

notas = [n1, n2, n3]
media = ((n1 + n2 + n3)//3)
print("Sua média é: ", media)

'''
11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. 
Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:

[ ] - para posições vazias
tor - para a torre
cav - para o cavalo
bis - para o bispo
rai - para a rainha
rei - para o rei
pea - para o peão
Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. 
(Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)
'''

