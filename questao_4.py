
from validador_senha import validar_senha

# QUESTÃO 4 - VALIDADOR DE SENHAS

print("=" * 40)
print("QUESTÃO 4 - VALIDADOR DE SENHAS")
print("=" * 40)

senha = input("Digite uma senha para verificar: ")

erros = validar_senha(senha)

if len(erros) == 0:
    print("Senha válida! Todos os critérios foram atendidos.")
else:
    print("Senha inválida!")
    print("Problemas encontrados:")

    for erro in erros:
        print("-", erro)
