aluno = {
    "nome": "Emanuel",
    "idade": 19,
    "curso": "Engenharia de Software"
}

aluno.update({"nota": 9.5})
aluno.pop("idade")

print(aluno["nome"])
