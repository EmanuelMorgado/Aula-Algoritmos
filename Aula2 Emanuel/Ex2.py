lista = []
n = int(input("Quantos itens quer adicionar? "))

for i in range(n):
    itens = str(input(f"Digite o {i + 1}° item: "))
    lista.append(itens)

while True:
    print("""[1] Encerrar
[2] Mostrar a lista""")
    op = input("Escolha: ")

    if op == "1":
        print("Lista encerrada.")
        break
        
    else:
        lista.sort()
        print(lista)
        break