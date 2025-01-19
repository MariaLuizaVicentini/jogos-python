###  Código em desenvolvimento..... !!!!!###

import random

# Função principal que controla o jogo da forca
def jogar_forca():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    print(palavra_secreta)
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_chutadas = []  # Lista para armazenar letras já chutadas

    enforcou = False
    acertou = False
    erros = 0
    max_erros = 7  # Define o número máximo de erros permitidos

    while not enforcou and not acertou:
        print(letras_acertadas)
        chute = pede_chute()

        if chute in letras_chutadas:
            print("Você já chutou essa letra. Tente outra.")
            continue  # Pede um novo chute se a letra já foi chutada

        letras_chutadas.append(chute)  # Adiciona o chute à lista de letras chutadas

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros >= max_erros
        acertou = "_" not in letras_acertadas

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    print(40 * "*")
    print("***Bem vindo ao jogo da Forca!***")
    print(40 * "*")


def carrega_palavra_secreta():
    palavras = []
    with open("texto.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    return random.choice(palavras).upper()


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for _ in palavra_secreta]


def pede_chute():
    return input("Qual letra? ").strip().upper()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    for index, letra in enumerate(palavra_secreta):
        if chute == letra:
            letras_acertadas[index] = letra


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
    print(fases[erros])


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


if __name__ == "__main__":
    jogar_forca()
