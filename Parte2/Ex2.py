print("Bem vindo ao sistema, digite sua senha abaixo.")
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == "senha123":
        print("Acesso liberado, seja bem-vindo.")
        break
    else:
        tentativas += 1
        print("Senha incorreta, tente novamente.")

else:
    print("Acesso bloqueado.")