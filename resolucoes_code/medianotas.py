# Programa para calcular a média de notas de um aluno

# Solicita as notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado
print(f"\nA média do aluno é: {media:.2f}")

# Verifica a situação do aluno
if media >= 7:
    print("Situação: Aprovado ✅")
elif media >= 5:
    print("Situação: Recuperação ⚠️")
else:
    print("Situação: Reprovado ❌")
