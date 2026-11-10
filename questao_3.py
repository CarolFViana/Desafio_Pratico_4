
import math

# QUESTÃO 3 - EQUAÇÃO DO SEGUNDO GRAU

def calcular_raizes(a, b, c):
    if a == 0:
        print("Não é uma equação do 2º grau.")
        return

    delta = b ** 2 - 4 * a * c
    print(f"Delta: {delta:.2f}")

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print("A equação possui duas raízes reais distintas.")
        print(f"Primeira raiz: {x1:.2f}")
        print(f"Segunda raiz: {x2:.2f}")

    elif delta == 0:
        x = -b / (2 * a)

        print("A equação possui uma raiz real.")
        print(f"Raiz: {x:.2f}")

    else:
        print("A equação não possui raízes reais.")


print("=" * 45)
print("QUESTÃO 3 - EQUAÇÃO DO SEGUNDO GRAU")
print("=" * 45)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

calcular_raizes(a, b, c)
