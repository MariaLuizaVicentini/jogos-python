###  Código em desenvolvimento..... !!!!!###



import random

# Função principal que controla o jogo da forca
def jogar_forca():
    # Imprime uma mensagem de abertura do jogo
    imprime_mensagem_abertura()
    # Carrega a palavra secreta que o jogador deve adivinhar
    palavra_secreta = carrega_palavra_secreta()
    print(palavra_secreta)
    # Inicializa a lista que contém as letras acertadas como "_"
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    # Variáveis de controle para o loop do jogo
    enforcou = False  # Indica se o jogador foi enforcado
    acertou = False   # Indica se o jogador acertou a palavra
    erros = 0         # Contador de erros do jogador

    # Loop principal do jogo
    while not enforcou and not acertou:
        # Solicita uma letra ao jogador
        chute = pede_chute()
        # Verifica se o chute está correto
        if chute in palavra_secreta:
            # Atualiza as letras acertadas com o chute correto
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            # Incrementa o contador de erros
            erros += 1
            # Desenha a forca com base no número de erros
            desenha_forca(erros)

        # Verifica se o jogador perdeu ou ganhou
        enforcou = erros == 7  # O jogador perde após 7 erros
        acertou = "_" not in letras_acertadas  # O jogador ganha se não houver "_" nas letras acertadas
        print(letras_acertadas)

    # Exibe a mensagem final com base no resultado do jogo
    if acertou:
        imprime_mensagem_vencedor()
        
    else:
        imprime_mensagem_perdedor(palavra_secreta)


# Função que imprime a mensagem de abertura do jogo
def imprime_mensagem_abertura():
    print(40*"*")
    print("***Bem vindo ao jogo da Forca!***")
    print(40*"*")


# Função que carrega uma palavra secreta aleatória de um ficheiro
def carrega_palavra_secreta():
    palavras = []  # Lista para armazenar as palavras
    with open("texto.txt", "r") as arquivo:  # Abre o ficheiro de palavras
        for linha in arquivo:
            palavras.append(linha.strip())  # Adiciona cada palavra à lista, removendo espaços
    return random.choice(palavras).upper()  # Retorna uma palavra aleatória em maiúsculas


# Função que inicializa a lista de letras acertadas com "_" para cada letra da palavra
def inicializa_letras_acertadas(palavra):
    return ["_" for _ in palavra]  # Cria uma lista com "_" no lugar de cada letra


# Função que solicita uma letra ao jogador
def pede_chute():
    return input("Qual letra? ").strip().upper()  # Remove espaços e converte para maiúsculas


# Função que marca um chute correto na lista de letras acertadas
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    for index, letra in enumerate(palavra_secreta):  # Percorre cada letra da palavra secreta
        if chute == letra:  # Verifica se a letra chutada é igual à letra atual
            letras_acertadas[index] = letra  # Atualiza a posição correspondente na lista de letras acertadas


# Função que desenha a forca de acordo com o número de erros
def desenha_forca(erros):
    fases = [
        "  _______     \n |/      |    \n |            \n |            \n |            \n |            \n_|___         ",
        "  _______     \n |/      |    \n |      (_)   \n |            \n |            \n |            \n_|___         ",
        "  _______     \n |/      |    \n |      (_)   \n |       |    \n |            \n |            \n_|___         ",
        "  _______     \n |/      |    \n |      (_)   \n |      \\|    \n |            \n |            \n_|___         ",
        "  _______     \n |/      |    \n |      (_)   \n |      \\|/   \n |            \n |            \n_|___         ",
        "  _______     \n |/      |    \n |      (_)   \n |      \\|/   \n |       |    \n |            \n_|___         ",
        "  _______     \n |/      |    \n |      (_)   \n |      \\|/   \n |       |    \n |      /     \n_|___         ",
        "  _______     \n |/      |    \n |      (_)   \n |      \\|/   \n |       |    \n |      / \\   \n_|___         ",
    ]
    print(fases[erros])  # Exibe o estado atual da forca


# Função que imprime a mensagem de vitória
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    


# Função que imprime a mensagem de derrota
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\/\\  ")
    print("\\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           ")


# Executa o jogo se o ficheiro for executado diretamente
if __name__ == "__main__":
    jogar_forca()
