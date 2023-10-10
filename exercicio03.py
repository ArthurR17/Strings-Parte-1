palavra = input("Digite uma palavra: ")
letra = input("Digite a letra que deseja substituir: ")
sub = input("Digite a letra que deseja colocar no lugar: ")

if letra in palavra:
    print(f'A palavra {palavra} foi transformada para: ' + palavra.replace(letra, sub))
