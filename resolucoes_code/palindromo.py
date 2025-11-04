def verifica_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    invertida = palavra[::-1]
    
    if palavra == invertida:
        print("É um palíndromo! 🔄")
    else:
        print("Não é um palíndromo ❌")

entrada = input("Digite uma palavra ou frase: ")
verifica_palindromo(entrada)