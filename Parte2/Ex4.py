def buscar(lista, nome):
    for i, n in enumerate(lista):
        if n == nome:
            return i
    return -1

nomes = input("Digite os nomes separados por espaço: ").split()
busca = input("Digite o nome a buscar: ")

posicao = busca(nomes, busca)
if posicao != -1:
    print(f"Nome encontrado na posição {posicao}.")
else:
    print("Nome não encontrado.")