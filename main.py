alunos = {
    "João": 8,
    "Maria": 9,
    "Pedro": 5,
    "Ana": 6,
}

for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome} Está Aprovado")
    else:
        print(f"{nome}Está Reprovado")