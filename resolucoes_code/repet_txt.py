#Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 

# Solicita a string ao usuário
texto = input("Digite uma palavra ou frase: ")

# Solicita o número de repetições
repeticoes = int(input("Digite um número inteiro: "))

# Exibe a string repetida o número de vezes informado
resultado = texto * repeticoes

print("\nResultado:")
print(resultado)
