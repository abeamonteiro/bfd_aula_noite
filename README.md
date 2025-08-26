# bfd_aula_noite
aula 01 - documentação em https://peps.python.org

limpar o terminal com um espaço: ctrl + L; limpar completo: clear + enter

caso o "git add ." tenha sido no arquivo errado, para restaurar, usar: "git restore --staged <file>..."

para parar o terminal: 

----------------------------------------------------------------------------------------------------

aula 02

- variaveis, tipo de variáveis, nomeando variáveis
    - o que são variáveis?

    - variáveis tipo string, tipo float, tipo int, tipo booleano

            *** quando voce trabalha com número flutante, voce sobrecarrega a aplicação  (pesquisar sobre o ponto flutuante e o numero flutuante)

- operações: Soma (+) , subtração (-), multiplicação (*), divisão convencional (/), divisão por inteiro (//), módulo -resto da divisão pelo inteiro- (%), exponencial (**)

ctrl + : -comenta e descomenta o texto todo de uma só vez, e ''' antes e depois de um bloco de texto 

----------------------------------------------------------------------------------------------------

aula 06

CRUD
instalação do venv dentro do repositorio
em crud: python -m venv .venv  (instala venv)
source .venv/bin/activate   
pip install django 
pip freeze
------------------------------------------------------------------------------------------------------

aula 07

1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
6- Crie uma lista chamada numeros com os valores [1, 2, 3, 2, 4, 2, 5].
Mostre quantas vezes o número 2 aparece na lista.
7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
notas = [[7, 8, 9], [6, 5, 7]]
No fim, imprima a média de cada aluno.
'''
