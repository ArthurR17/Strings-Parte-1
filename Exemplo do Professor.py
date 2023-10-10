import random  # Importa a biblioteca random

print("Bem vindo ao jogo de Pedra, Papel e Tesoura!")  # Mostra uma mensagem de boas vindas
opcoes = ["Pedra", "Papel", "Tesoura"]  # Cria uma lista com as opções do jogo

# Loop infinito até o jogador digitar sair
while True:
    # Escolhe uma opção aleatória da lista opcoes para o computador
    escolha_computador = random.choice(opcoes)
    # Pede para o jogador escolher uma opção
    escolha_jogador = input("Escolha Pedra, Papel ou Tesoura (Digite sair para terminar o jogo): ")

    if escolha_jogador == "sair":  # Se o jogador digitar sair, o jogo termina
        break  # Encerra o loop
    print("O computador escolheu: " + escolha_computador)  # Mostra a escolha do computador

    if escolha_jogador == escolha_computador:  # Se as escolhas forem iguais, vai ser empate
        print("Empate!")
    # Verifica se a escolha do jogador ganha do computador
    elif escolha_jogador == "Pedra" and escolha_computador == "Tesoura" or \
            escolha_jogador == "Papel" and escolha_computador == "Pedra" or \
            escolha_jogador == "Tesoura" and escolha_computador == "Papel":
        print("Você ganhou!") # Mostra que o jogador ganhou
    else:
        print("Você perdeu!") # Caso o contrário, mostra que o jogador perdeu

print("Obrigado por jogar!") # Mostra uma mensagem de agradecimento