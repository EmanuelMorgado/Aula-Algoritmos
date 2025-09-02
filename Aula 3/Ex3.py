produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")