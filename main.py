numeros = []

print("Por favor, informe 10 números inteiros:")

for contador in range(10):
    num = int(input(f"Digite o {contador+1} número:"))
    numeros.append(num)

    pares = []
    impares = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    else:
            impares.append(num)

print("\n--- Resultados ---")
print(f"Lista completa de números: {numeros}")
print(f"Números pares: {pares}")
print(f"Quantidade de números pares: {len(pares)}")
print(f"Números ímpares: {impares}")
print(f"Quantidade de números ímpares: {len(impares)}")