###  Código em desenvolvimento..... ###



import random

# Função principal que contém toda a lógica do jogo
def jogar_forca():

    # Saudação ao usuário
    print(36 * "*")
    print("\nBem-vindo ao jogo da Forca\n")
    print(36 * "*")

    # Abrir o arquivo em modo leitura
    arquivo = open("frutas.txt", "r")
    lista_palavras = []

    # Ler cada linha do arquivo e adicionar à lista de palavras
    for linha in arquivo:
        # Remover espaços no início e fim de cada linha
        linha = linha.strip()
        # Adicionar a linha como um elemento da lista de palavras
        lista_palavras.append(linha)

    # Fechar o arquivo após a leitura
    arquivo.close()

    # Escolher uma palavra aleatória da lista e transformá-la em maiúscula
    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero].upper()

    # Criar uma lista com "_" representando as letras da palavra secreta
    letras_acertadas = ["_" for letra in palavra_secreta]

    # Variáveis de controle
    enforcou = False
    acertou = False
    erros = 0

    # Laço de repetição: enquanto o jogador não enforcou e não acertou a palavra
    while not enforcou and not acertou:

        # Solicitar ao usuário uma letra
        chute = input("Qual letra? ")
        # Remover espaços e transformar a letra em maiúscula
        chute = chute.strip().upper()

        # Verificar se a letra chutada está na palavra secreta
        if chute in palavra_secreta:
            posicao = 0  # Inicializar a posição atual da letra

            # Percorrer cada letra da palavra secreta
            for letra in palavra_secreta:
                # Se a letra chutada for igual à letra atual da palavra secreta
                if chute == letra:
                    # Substituir "_" pela letra correta na posição correspondente
                    letras_acertadas[posicao] = letra
                # Incrementar a posição
                posicao = posicao + 1

        # Se a letra digitada não estiver presente na palavra secreta
        else:
            erros = erros + 1  # Incrementar o número de erros em 1

        # Verificar se o jogador atingiu o limite de 6 erros
        enforcou = erros == 6
        # Verificar se o jogador acertou todas as letras (não há mais "_")
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    # Exibir a mensagem final com o resultado do jogo
    if acertou:
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
        print(letras_acertadas)

    print("Fim do jogo!")


# Executar a função principal se o script for executado diretamente
if __name__ == "__main__":
    jogar_forca()
