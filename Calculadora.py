#inicio do Programa

#Solicitar número ao usuario
print('-----------------------------------------------')
print('Bem-vindo à calculadora!')
print('-----------------------------------------------')
print('|Digite dois números inteiros para realizar operações matemáticas.|')
print('-----------------------------------------------')
numero1 = int(input("Digite primeiro número: "))
numero2 = int(input("Digite segundo número: "))

#solicitar a operação desejada
print('-----------------------------------------------')
print("Escolha a operação desejada:")
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Potência')
escolha = int(input("Digite o número da operação desejada: "))
print('-----------------------------------------------')

#inicializar a variável resultado
resultado = None
operacao = ""

#Realização de operações escolhidas pelo usuário
if escolha == 1:
    resultado = numero1 + numero2
    print(f'{numero1} + {numero2} = {resultado}')
elif escolha == 2:
    resultado = numero1 - numero2
    print(f'{numero1} - {numero2} = {resultado}')
elif escolha == 3:
    resultado = numero1 * numero2
    print(f'{numero1} * {numero2} = {resultado}')
elif escolha == 4:
    if numero2 == 0:
        print('ERROR DIVISÃO POR ZERO NÃO EXISTENTE')
    else:
        resultado = numero1 / numero2
        print(f'{numero1} / {numero2} = {resultado}')
elif escolha == 5:
    resultado = numero1 ** numero2
    print(f'{numero1} ^ {numero2} = {resultado}')

#Caso o usuário não escolha uma operação válida
else:
    print('ERROR: operação inválida!')

#exibindo o resultado
print('-----------------------------------------------')
print(f'O resultado da operação é: {operacao} {resultado}')
print('-----------------------------------------------')
#FIM DO PROGRAMA