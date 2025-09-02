aluno = {
    "nome": "Emanuel",
    "idade": 19,
    "curso": "Engenharia de Software"
}

aluno.update({"nota": 9.5})
aluno.pop("idade")

print(aluno["nome"])

if "curso" in aluno:
    print("A chave existe.")
else:
    print("A chave não existe")