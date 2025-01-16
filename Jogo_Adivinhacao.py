# Jogo de adivinhação em Python.

import random  # biblioteca para gerar números aleatórios

# Inicializando função
def jogar_adivinhacao():

    # Exibindo a saudação 
    print(40 * '*')
    print("Bem-vindo ao jogo de Adivinhação!")
    print(40 * '*')

    # Inicializando e definindo as variáveis
    num_secreto = random.randint(1, 101)
    tentativas = 0
    pontos = 1000

    # Exibindo os níveis disponíveis do jogo
    print("Qual nível de dificuldade?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    # Pedindo para o usuário que escolha um nível 
    nivel = int(input("Digite o número do nível que você deseja: "))

    # Estrutura condicional: Definindo número de tentativas de acordo com o nível que foi esolhido
    if nivel == 1:
        tentativas = 10
    elif nivel == 2:
        tentativas = 5
    elif nivel == 3:
        tentativas = 3

    # Laço de repetição: Esse bloco será executado de acordo com o número de rodadas
    for rodada in range(1, tentativas + 1):
        print("Essa é a {}ª rodada de {} tentativas!".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print(40 * '-')

        # Estrutura condicional: Se o chute for menor que 1 maior que 100 partimos para próxima iteração
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        print("Você digitou: {}".format(chute))

        # Atribuindo valor as variáveis para melhorar a legibilidade do código
        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        
        if acertou:
            print(40 * '-')
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi MAIOR do que o número secreto.")
                print(40 * '-')
            elif menor:
                print("Você errou! O seu chute foi MENOR do que o número secreto.")

            # Atribuindo a variável o cálculo de numeros perdidos 
            pontos_perdidos = abs(num_secreto - chute)
            # Atribuindo a variável o
            pontos = abs(pontos - pontos_perdidos)  # Garante que a pontuação não seja negativa
            print(40 * '-')
    
    print("Fim do jogo!")
    print(40 * '-')

#Estrutura condicional: Se o nome do módulo for igual a "__main__":
if __name__ == "__main__":
    # A função será chamada para inicializar o jogo 
    jogar_adivinhacao()


