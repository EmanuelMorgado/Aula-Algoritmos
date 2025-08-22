cpf = input("Informe o seu CPF (apenas números): ")

if cpf.isdigit() and len(cpf) == 11:
    print("CPF válido")
else:
    print("CPF inválido")