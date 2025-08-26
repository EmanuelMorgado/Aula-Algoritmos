def media_temperaturas():

    n1 = 7
    temp = []


    for i in range(n1):
        temperatura = float(input(f"Digite a {i + 1}° temperatura: "))
        temp.append(temperatura)

    media = sum(temp) / len(temp)
    quente = max(temp)
    frio = min(temp)
    acima = [n for n in temp if n > media]
    acima2 = len(acima)

    print(f"""
Média das temperaturas: {media:.2f}°C
Dia mais quente: {quente}°C
Dia mais frio: {frio}°C
{acima2} Dias ficaram acima da média.""")

media_temperaturas()