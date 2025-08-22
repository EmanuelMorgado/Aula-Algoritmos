notas = input("Digite as notas separadas com espaçamento: ")
lista = [float(n) for n in notas.split()]

if lista:
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    acima_media = [n for n in lista if n > media]
    per = (len(acima_media) / len(lista)) * 100

    print(f"""Média da turma: {media:.2f}
        Maior nota: {maior})
        Menor nota: {menor})
        Percentual de alunos acima da média: {per:.1f}%""")
    
else:
    print("Nenhuma nota informada.")
    