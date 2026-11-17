import random

opcoes = ("pedra", "papel", "tesoura")
computador = random.choice(opcoes)

jogador = input("\nEscolha (pedra/papel/tesoura): ").lower()

print(f"\nVocê: {jogador}")
print(f"Computador: {computador}")

if jogador == computador:
    print("\nEmpate!")
elif jogador == "pedra" and computador == "tesoura":
   print("\nVocê ganhou!")
elif jogador == "papel" and computador == "pedra":
    print("\nVocê ganhou!")
elif jogador == "tesoura" and computador == "papel":
    print("\nVocê ganhou!")
else:
   print("\nVocê Perdeu!")