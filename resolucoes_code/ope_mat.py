# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")


opcao = input("Digite o número da operação desejada: ")

if opcao == "1":
    resultado = num1 + num2
    print(f"\nResultado: {num1} + {num2} = {resultado}")
elif opcao == "2":
    resultado = num1 - num2
    print(f"\nResultado: {num1} - {num2} = {resultado}")
elif opcao == "3":
    resultado = num1 * num2
    print(f"\nResultado: {num1} * {num2} = {resultado}")
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado: {num1} / {num2} = {resultado}")
    else:
        print("\nErro: divisão por zero não é permitida.")
else:
    print("\nOpção inválida. Tente novamente.")
