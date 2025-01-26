import random

def jogar_forca():

    """Exibir mensagem de saudação"""
    imprime_mensagem_abertura()

    """Sortear palavra secreta"""
    palavra_secreta = carrega_palavra_secreta()

    """Inicializar lista de underscore para representar a quantidade de letras que a palavra secreta possui"""
    lista_letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    """inicializar lista de letras chutadas pelo usuário"""
    letras_chutadas = []

    enforcou = False
    acertou = False
    erros = 0
    max_erros = 7  # Define o número máximo de erros permitidos

    while not enforcou and not acertou:
        print(lista_letras_acertadas)
        chute = pede_chute()

        if chute in letras_chutadas:
            print("Você já chutou essa letra. Tente outra.")
            continue  # Pede um novo chute se a letra já foi chutada

        letras_chutadas.append(chute)  # Adiciona o chute à lista de letras chutadas

        if chute in palavra_secreta:
            marca_chute_correto(chute, lista_letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros >= max_erros
        acertou = "_" not in lista_letras_acertadas

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    

def imprime_mensagem_abertura():
    print(40 * "*")
    print("***Bem vindo ao jogo da Forca!***")
    print(40 * "*")


def carrega_palavra_secreta():
    palavras = [] # Iicializando lista de palavras 
    with open("texto.txt", "r") as arquivo: # abrindo o arquivo em modo leitura e renomeando-o 
        """Para cada LINHA dentro do ARQUIVO:"""
        for linha in arquivo:
            """Strip remove os espaços da linha e adiciona a linha na lista de palavras"""
            palavras.append(linha.strip())
            """Random escolhe aleatóriamente um elemento da lista de palavras e retorna ela em letra MAIÚSCULA"""
    return random.choice(palavras).upper()


def inicializa_letras_acertadas(palavra_secreta):
    """Separar palavra secreta em uma lista onde cada elemento é uma letra"""
    palavra_secreta.split()
    """retorna 1 underscore para cada letra dentro da palavra secreta"""
    return ["_" for letra in palavra_secreta]


def pede_chute():
    """Retorna uma letra maiuscula sem espaços digita pelo usuario"""
    return input("Qual letra? ").strip().upper()

def marca_chute_correto(chute, lista_letras_acertadas, palavra_secreta):
    """para cada posição e letra dentro da minha palavra secreta"""
    for index, letra in enumerate(palavra_secreta):
        """se o chute do usuario for igual a alguma letra da minha palavra secreta"""
        if chute == letra:
            """lista de letras acertadas recebe acessa a posição da letra e realiza a substituição"""
            lista_letras_acertadas[index] = letra

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
