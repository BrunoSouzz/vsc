#declaração de dados
aluno= input('digite o nome do aluno:')
materia = input('digite o nome da materia:')
nota1 = input('digite nota1:')
nota2 = input('digite nota2:')
media = (float(nota1) + float(nota2)) / 2
#declaração de do resultado
if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')
#exibição do resultado
print('Nome do aluno:', aluno)
print('Nome da materia:', materia)
print('Nota 1:', nota1)
print('Nota 2:', nota2)
print('Média:', media)
#exibição tabela
print('---------------------------------------')
print('Tabela de Resultados')
print('---------------------------------------')
print('| Nome do aluno | Nome da materia | Nota 1 | Nota 2 | Média |')
print('---------------------------------------')
print('|', aluno, '|', materia, '|', nota1, '|', nota2, '|', media, '|')
print('---------------------------------------')