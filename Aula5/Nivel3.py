def buscar_pessoa(lista, nome_buscado):
    for pessoa in lista:
        if pessoa["nome"] == nome_buscado:
            return pessoa
    return None

pessoas = [
    {"nome": "Emanuel", "idade": 19},
    {"nome": "Carlos", "idade": 64},
    {"nome": "Flavia", "idade": 53}
]

resultado = buscar_pessoa(pessoas, "Emanuel")

if resultado:
    print(f"Pessoa encontrada: {resultado}")
else:
    print("Pessoa não encontrada.")

#12 exercicio

import random

def jogo_adivinhe_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Acertou o número {numero_secreto} em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("O número é maior.")
        else:
            print("O número é menor.")


jogo_adivinhe_numero()

#13 exercicio

def buscar_produtos(lista, preco_buscado):
    encontrados = []
    for produto in lista:
        if produto["preco"] == preco_buscado:
            encontrados.append(produto)
    return encontrados


produtos = [
    {"nome": "Gabinete", "preco": 450},
    {"nome": "Mouse", "preco": 230},
    {"nome": "Teclado", "preco": 230},
    {"nome": "Monitor", "preco": 1200}
]

resultado = buscar_produtos(produtos, 230)
print("Produtos com preço R$100:")
for prod in resultado:
    print(f"- {prod['nome']}")

#14 exercicio

def meu_index(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return -1  


lista = [10, 20, 30, 40, 30]
print(meu_index(lista, 30))
print(meu_index(lista, 100))