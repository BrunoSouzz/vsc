from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simulação de banco de dados em memória
usuarios = {}

# Página inicial
html_home = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Banco Python</title>
</head>
<body>
    <h1>Bem-vindo ao Banco Python!</h1>
    <p>Seu banco digital, rápido e seguro!</p>
    <a href="/cadastro">Novo Cadastro</a> | <a href="/login">Acessar Cadastro</a>
</body>
</html>
"""

# Formulário de cadastro
html_cadastro = """
<form method="post">
    <h2>Novo Cadastro</h2>
    Nome: <input type="text" name="nome"><br>
    Idade: <input type="number" name="idade"><br>
    Telefone: <input type="text" name="telefone"><br>
    Email: <input type="email" name="email"><br>
    CPF: <input type="text" name="cpf"><br>
    Senha: <input type="password" name="senha"><br>
    <input type="submit" value="Cadastrar">
</form>
"""

# Formulário de login
html_login = """
<form method="post">
    <h2>Acessar Conta</h2>
    CPF: <input type="text" name="cpf"><br>
    Senha: <input type="password" name="senha"><br>
    <input type="submit" value="Entrar">
</form>
"""

# Tela da conta
html_conta = """
<h2>Bem-vindo, {{ nome }}!</h2>
<p>Saldo atual: R$ {{ saldo }}</p>
<form method="post" action="/depositar">
    Valor para depósito: R$ <input type="number" step="0.01" name="valor">
    <input type="submit" value="Depositar">
</form>
<form method="post" action="/sacar">
    Valor para saque: R$ <input type="number" step="0.01" name="valor">
    <input type="submit" value="Sacar">
</form>
<a href="/">Sair</a>
"""

# Rotas Flask
@app.route("/")
def home():
    return render_template_string(html_home)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        cpf = request.form["cpf"]
        usuarios[cpf] = {
            "nome": request.form["nome"],
            "idade": request.form["idade"],
            "telefone": request.form["telefone"],
            "email": request.form["email"],
            "senha": request.form["senha"],
            "saldo": 0.0
        }
        return redirect(url_for("login"))
    return render_template_string(html_cadastro)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cpf = request.form["cpf"]
        senha = request.form["senha"]
        if cpf in usuarios and usuarios[cpf]["senha"] == senha:
            return redirect(url_for("conta", cpf=cpf))
        else:
            return "CPF ou senha inválidos!"
    return render_template_string(html_login)

@app.route("/conta/<cpf>")
def conta(cpf):
    user = usuarios.get(cpf)
    if user:
        return render_template_string(html_conta, nome=user["nome"], saldo=round(user["saldo"], 2))
    return "Usuário não encontrado"

@app.route("/depositar", methods=["POST"])
def depositar():
    cpf = list(usuarios.keys())[0]
    valor = float(request.form["valor"])
    usuarios[cpf]["saldo"] += valor
    return redirect(url_for("conta", cpf=cpf))

@app.route("/sacar", methods=["POST"])
def sacar():
    cpf = list(usuarios.keys())[0]
    valor = float(request.form["valor"])
    if usuarios[cpf]["saldo"] >= valor:
        usuarios[cpf]["saldo"] -= valor
    return redirect(url_for("conta", cpf=cpf))

# Rodar o app
if __name__ == "__main__":
    app.run(debug=True)
