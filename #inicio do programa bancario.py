#inicio do programa bancario

#apresentação do aplicativo
print('|------------------|')
print("Bem-vindo ao Banco Python!")
print("Seu banco digital, rápido e seguro!")
print('|------------------|')

#Menu de opções
print('|------------------|')
print("Escolha uma opção para iniciar:")
print('|------------------|')
print("1. Novo cadastro")
print("2. Acessar cadastro anterior")
print('|------------------|')

#Seleção da opção
opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    print("Novo cadastro")
elif opcao == 2:
    print("Acessar cadastro anterior")
else:
    print("Opção inválida!")
    exit()

#Novo cadastro
def novo_cadastro():
    print("Novo cadastro")
    print("Por favor, preencha as informações abaixo:")
    print('|------------------|')

#Solicitação de informações do cliente
nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
telefone = input("Digite seu telefone: ")
email = input("Digite seu email: ")
CPF = input("Digite seu CPF: ")

#Criação de segurança para o cliente
senha = input("Digite nova senha: ")
confirmar_senha = input("Confirme sua senha: ")
while senha != confirmar_senha:
    print("Senhas não conferem!")
    senha = input("Digite nova senha: ")
    confirmar_senha = input("Confirme sua senha: ")

print("Cadastro realizado com sucesso!")

#Acesso ao cadastro anterior
def acessar_cadastro():
    print('|------------------|')
    print("Acessar cadastro anterior")
    print("Por favor, insira seu CPF e senha:")
    print('|------------------|')

#Solicitação de informações do cliente anterior
senha_acesso = input("Digite sua senha: ")
confirmar_senha_acesso = input("Confirme sua senha: ")
while senha_acesso != confirmar_senha_acesso:
    print("Senhas não conferem!")
    senha_acesso = input("Digite nova senha: ")
    confirmar_senha_acesso = input("Confirme sua senha: ")

print("Acesso realizado com sucesso!")

print('|------------------|')
print("Bem-vindo de volta, " + nome + "!")
print('|------------------|')

#sair do aplicativo
def sair_aplicativo():
    print('|------------------|')
    print("Saindo do aplicativo...")
    print("Obrigado por usar o Banco Python! Até logo!")
    print('|------------------|')
    exit()

#Menu de opções após o cadastro
print('|------------------|')
print("Escolha uma opção:")
print('|------------------|')
print("1. Consultar saldo")
print("2. Realizar depósito")
print("3. Realizar saque")
print("4. Transferir dinheiro")
print("5. Alterar senha")
print("6. Sair do aplicativo")
print('|------------------|')

#Escolha da opção
opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    print("Consultar saldo")
elif opcao == 2:
    print("Realizar depósito")
elif opcao == 3:
    print("Realizar saque")
elif opcao == 4:
    print("Transferir dinheiro")
elif opcao == 5:
    print("Alterar senha")
elif opcao == 6:    
    sair_aplicativo()

#Consulta de saldo
def consultar_saldo():
    print('|------------------|')
    print("Consultar saldo")
    print("Seu saldo atual é: R$ 0,00")
    print('|------------------|')
    return 0.00

#Depósito
def realizar_deposito(saldo):
    print('|------------------|')
    print("Realizar depósito")
    valor = float(input("Digite o valor a ser depositado: R$ "))
    saldo += valor
    print("Depósito realizado com sucesso!")
    print("Seu novo saldo é: R$ " + str(saldo))
    print('|------------------|')
    return saldo

#Saque
def realizar_saque(saldo):
    print('|------------------|')
    print("Realizar saque")
    valor = float(input("Digite o valor a ser sacado: R$ "))
    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        print("Saque realizado com sucesso!")
        print("Seu novo saldo é: R$ " + str(saldo))
    print('|------------------|')
    return saldo

#Transferência
def transferir_dinheiro(saldo):
    print('|------------------|')
    print("Transferir dinheiro")
    valor = float(input("Digite o valor a ser transferido: R$ "))
    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        print("Transferência realizada com sucesso!")
        print("Seu novo saldo é: R$ " + str(saldo))
    print('|------------------|')
    return saldo

#alterar senha
def alterar_senha():
    print('|------------------|')
    print("Alterar senha")
    nova_senha = input("Digite sua nova senha: ")
    confirmar_nova_senha = input("Confirme sua nova senha: ")
    while nova_senha != confirmar_nova_senha:
        print("Senhas não conferem!")
        nova_senha = input("Digite sua nova senha: ")
        confirmar_nova_senha = input("Confirme sua nova senha: ")
    print("Senha alterada com sucesso!")
    print('|------------------|')
    return nova_senha

#Sair do aplicativo
def sair_aplicativo():
    print('|------------------|')
    print("Saindo do aplicativo...")
    print("Obrigado por usar o Banco Python! Até logo!")
    print('|------------------|')
    exit()

#Fim do programa bancario