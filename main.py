import random

numero_secreto = random.randint(1, 20)
tentativas = 0
palpite = int(input(
    "Tente advinhar um numero entre 1 e 20:"))

while palpite != numero_secreto:
    tentativas += 1
    if palpite < numero_secreto:
        print("O número secreto é maior!")
    else:
        print("O número secreto é menor!")