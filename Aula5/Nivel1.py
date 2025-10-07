#primeiro exercicio

def busca_numero(lista, numero_procurado):

    for posicao in range(len(lista)):
        if lista[posicao] == numero_procurado:

            return True, posicao

    return False, -1

mlista = [4, 8, 15, 16, 23, 42]
numero = 15


print(mlista)
print(numero)


encontrou, posicao = busca_numero(mlista, numero)


if encontrou:
    print(f"Indice:{posicao}")
else:
    print(f"Não esta na lista")


#segundo exercicio

def contar_ocorrencias(lista, numero_buscado):
    contador = 0
    for elemento in lista:
        if elemento == numero_buscado:
            contador += 1
    return contador

lista = [3, 5, 2, 3, 8, 3, 1, 4]
numero = 3

print(f"Aparece {contar_ocorrencias(lista, numero)} vezes na lista.")

#terceiro exercicio

def encontrar_maior(lista):
    if not lista:
        return None 

    maior = lista[0]  
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

lista = [10, 25, 3, 48, 17, 48]
maior_numero = encontrar_maior(lista)

print(f"O maior número da lista é: {maior_numero}")


#quarto exercicio

def encontrar_menor(lista):
    if not lista:
        return None 

    menor = lista[0] 
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor

lista = [10, 25, 3, 48, 17, -2]
menor_numero = encontrar_menor(lista)

print(f"O menor número da lista é: {menor_numero}")


#quinto exercicio

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            inicio = meio + 1  
        else:
            fim = meio - 1  

    return False  

lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
numero = 7

if busca_binaria(lista_ordenada, numero):
    print(f"O número {numero} está na lista.")
else:
    print(f"O número {numero} não está na lista.")