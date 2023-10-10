palavra = input("Digite um palíndromo: ")
if palavra == palavra[::-1]:
    print(f"{palavra} é um palíndromo")
else:
    print("Não é um palíndromo")