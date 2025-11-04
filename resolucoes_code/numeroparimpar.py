# Programa para verificar se um número é par ou ímpar

# Solicita um número ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
