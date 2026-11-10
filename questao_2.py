
import math

# QUESTÃO 2 - CALCULADORA DE ÁREAS

def area_triangulo():
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    return (base * altura) / 2

def area_retangulo():
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    return base * altura

def area_quadrado():
    lado = float(input("Digite o lado: "))
    return lado ** 2

def area_trapezio():
    base_maior = float(input("Digite a base maior: "))
    base_menor = float(input("Digite a base menor: "))
    altura = float(input("Digite a altura: "))
    return ((base_maior + base_menor) * altura) / 2

def area_losango():
    diagonal_maior = float(input("Digite a diagonal maior: "))
    diagonal_menor = float(input("Digite a diagonal menor: "))
    return (diagonal_maior * diagonal_menor) / 2

def area_circulo():
    raio = float(input("Digite o raio: "))
    return math.pi * (raio ** 2)


print("=" * 40)
print("QUESTÃO 2 - CALCULADORA DE ÁREAS")
print("=" * 40)

print("1 - Triângulo")
print("2 - Retângulo")
print("3 - Quadrado")
print("4 - Trapézio")
print("5 - Losango")
print("6 - Círculo")

opcao = input("Escolha uma figura de 1 a 6: ")

if opcao == "1":
    resultado = area_triangulo()
elif opcao == "2":
    resultado = area_retangulo()
elif opcao == "3":
    resultado = area_quadrado()
elif opcao == "4":
    resultado = area_trapezio()
elif opcao == "5":
    resultado = area_losango()
elif opcao == "6":
    resultado = area_circulo()
else:
    resultado = None
    print("Opção inválida!")

if resultado is not None:
    print(f"Área calculada: {resultado:.2f}")
