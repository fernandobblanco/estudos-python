# 3 — Usuário e senha

usuario_correto = "fernando"
senha_correta = "1234"

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")