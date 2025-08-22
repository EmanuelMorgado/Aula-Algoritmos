def primo():
    n = int(input("Digite um número: "))
    if n <= 1:
        print("Não primo")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Não primo")
            return
    print("Primo")

primo()