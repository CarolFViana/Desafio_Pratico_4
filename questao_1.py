
import random

# QUESTÃO 1 - JOGO DE ADIVINHAÇÃO

def jogo_adivinhacao():
    print("=" * 45)
    print("QUESTÃO 1 - JOGO DE ADIVINHAÇÃO")
    print("=" * 45)

    numero_secreto = random.randint(1, 100)
    palpites = []

    while True:
        try:
            palpite = int(input("Digite um número de 1 a 100: "))

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
            continue

        if palpite < 1 or palpite > 100:
            print("Atenção! Escolha um número entre 1 e 100.")
            continue

        palpites.append(palpite)

        if palpite < numero_secreto:
            print("Errou! O número secreto é maior.")

        elif palpite > numero_secreto:
            print("Errou! O número secreto é menor.")

        else:
            print("Parabéns! Você acertou!")
            print("Seus palpites:", palpites)
            print("Quantidade de tentativas:", len(palpites))
            break

jogo_adivinhacao()
