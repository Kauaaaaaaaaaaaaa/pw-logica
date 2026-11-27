notas = []

print("Por favor, informe 5 notas:")

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

    soma = sum(notas)
    media = soma / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)

    print("\n--- Resultados ---")
    print(f"Notas cadastradas: {notas}")
    print(f"Soma das notas: {soma}")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")