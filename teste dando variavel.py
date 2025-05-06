#entrada de dados
nome = input('escreva nome:')
idade = input('escreva idade:')
altura = input('escreva altura:')
#saida de dados
print('nome:', nome)
print('idade:', idade)
print('altura:',altura)
#verifica se a idade é maior que 18
if int(idade) >= 18:
    print('maior de idade')
else:
    print('menor de idade')
#verifica se a altura é maior que 1.70
if float(altura) >= 1.70:
    print('altura maior que 1.70')
else:
    print('altura menor que 1.70')