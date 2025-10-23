

Mostre todos os registros da tabela Aluno. 
(Use SELECT *)
SELECT *
FROM Aluno

Exiba apenas o nome e a nota1 de todos os alunos.
(Use SELECT com colunas específicas)
SELECT nome, nota1
FROM Aluno  

Liste todos os alunos cuja nota2 seja maior que 8.
(Use WHERE)
SELECT 
    nome,
    nota2
FROM Aluno
WHERE nota2 > 8;

Mostre os alunos que nasceram após o ano de 2000.
(Use WHERE com data)
SELECT 
    nome,
    data_nascimento
FROM Aluno
WHERE data_nascimento > '2000-12-31';

Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais.
(Use WHERE com condição numérica)
SELECT
    nome,
    mensalidade
FROM Curso
WHERE mensalidade > 600;    

Mostre o nome das turmas e o ano correspondente, ordenados pelo ano em ordem crescente.
(Use ORDER BY)
SELECT
    nome,
    ano
FROM Turma
ORDER BY ano ASC;

Liste o ano das turmas e a quantidade de turmas por ano.
(Use GROUP BY)
SELECT
    ano,
    COUNT(*) AS quantidade_turmas
FROM Turma
GROUP BY ano;

Calcule a média da nota1 dos alunos por id_turma.
(Use GROUP BY com função de agregação)
SELECT
    id_turma,
    AVG (nota1) AS media_nota1  
FROM Aluno
GROUP BY id_turma;

/*AVG para calcular a média*/

Mostre o ano e a quantidade de turmas apenas para os anos que têm mais de 2 turmas.
(Use GROUP BY e HAVING)
SELECT
    ano,
    COUNT(*) AS quantidade_turmas
FROM Turma
GROUP BY ano
HAVING COUNT(*) > 2;

Exiba o nome dos cursos e suas mensalidades, ordenando primeiro pela mensalidade (decrescente).
(Use ORDER BY)
SELECT
    nome,
    mensalidade
FROM Curso
ORDER BY mensalidade DESC;git 