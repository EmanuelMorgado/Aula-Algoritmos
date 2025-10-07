def busca_linear_nomes(lista, nome_buscado):
    for nome in lista:
        if nome() == nome_buscado():
            return True
    return False

nomes = []
print("Digite nomes (digite 'fim' para parar):")
while True:
    nome = input("Nome: ")
    if nome() == 'fim':
        break
    nomes.append(nome)

nome_procurado = input("Digite o nome a ser procurado: ")
if busca_linear_nomes(nomes, nome_procurado):
    print(f"O nome '{nome_procurado}' está na lista.")
else:
    print(f"O nome '{nome_procurado}' não foi encontrado.")


#setimo exercicio

def busca_binaria_recursiva(lista, alvo, inicio, fim):
    if inicio > fim:
        return False

    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        return True
    elif lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim)
    else:
        return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)


lista = [1, 3, 5, 7, 9, 11, 13]
alvo = 5
print("Encontrado!" if busca_binaria_recursiva(lista, alvo, 0, len(lista) - 1) else "Não encontrado.")


#oitavo exercicio


import time


lista = list(range(1_000_000))


alvo = 999999


def busca_linear(lista, alvo):
    for item in lista:
        if item == alvo:
            return True
    return False


def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False


inicio_tempo = time.time()
busca_linear(lista, alvo)
fim_tempo = time.time()
print(f"Tempo da busca linear: {fim_tempo - inicio_tempo:.6f} segundos")

inicio_tempo = time.time()
busca_binaria(lista, alvo)
fim_tempo = time.time()
print(f"Tempo da busca binária: {fim_tempo - inicio_tempo:.6f} segundos")


#nono exercicio


def primeira_ocorrencia(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    resultado = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            resultado = meio
            fim = meio - 1 
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resultado


lista = [1, 2, 2, 2, 3, 4]
alvo = 2
indice = primeira_ocorrencia(lista, alvo)
print(f"Primeira ocorrência de {alvo}: índice {indice}")



#decimo exercicio



def encontrar_inicio(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    resultado = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            resultado = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resultado

def encontrar_fim(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    resultado = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            resultado = meio
            inicio = meio + 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resultado

lista = [1, 2, 2, 2, 3, 4]
alvo = 2
inicio = encontrar_inicio(lista, alvo)
fim = encontrar_fim(lista, alvo)

if inicio != -1 and fim != -1:
    print(f"O número {alvo} aparece entre os índices {inicio} e {fim}.")
else:
    print(f"O número {alvo} não foi encontrado.")