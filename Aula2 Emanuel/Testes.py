lista = ["arroz", "feijao",2,3]
lista.append("elemento") # Adiciona um elemento na lista na ultima posição
print(lista)

print(lista[0],lista[4]) # Printa determinados elementos dentro da lista

lista[0] = "macarrão" # Sobrepoem um elemento pelo outro em determinada posição
print(lista)

lista.insert(1,"lasanha") # Inserir elemento em determinada posição
print(lista)


var = len(lista) # Informa a quantidade de itens dentro de uma lista
print(var)


for i in lista: # Printa cada item da lista separadamente
    print(i)

for i in range(len(lista)): # Printa a lista com o número dos elementos
    print(i, ":", lista[i])


lista2 = [3,2,1]

lista.extend(lista2) # Extente uma lista com a outra

print(lista)

lista.remove("lasanha") # Remove o determinado ELEMENTO de uma lista
print(lista)

lista.pop(0) # Remove determinado elemento de sua POSIÇÃO
print(lista)



lista1 = [1,2,3,4,5,6,]

i = 0

while i < len(lista1): # Printa uma lista até o final dela
    print(lista1[i])
    i += 1


