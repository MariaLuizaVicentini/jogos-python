
import Jogo_Adivinhacao # Importando o script do jogo de adivinhação
import Jogo_Forca # Importnado o script do jogo da Forca

# Inicializando a função: 
def escolher_jogo():

    # Exibindo mensagem de saudação 
    print(36 * "*")
    print("Olá, seja bem-vindo ao Jogos.py!\n{} \nEscolha o seu jogo!".format(36 * "*")) # Saudação ao usuario 
    print(36 * "*")
            
    # Exibição dos jogos disponíveis 
    print("(1) Forca\n(2) Adivinhação")
            
    # Solicitando ao usuário que escolha um dos jogos 
    jogo = int(input("Qual jogo?"))
    
    
    # Estrutura condicional: Se o jogo for igual a 1:
    if jogo == 1:
        print("Jogando Forca")
        Jogo_Forca.jogar_forca()  # Chama a função jogar_forca() do módulo Jogo_Forca
    # Se o jogo for igual a 2:
    elif jogo == 2:
        print("Jogando Adivinhação")
        Jogo_Adivinhacao.jogar_adivinhacao()  # Chama a função jogar_adivinhacao() do módulo Jogo_Adivinhacao
    else: # se não
        print("Entrada inválida: Por favor, Digite 1 ou 2")

# Se o nome do módulo atual for igual a "__main__"
if __name__ == "__main__":
    escolher_jogo() # Chamamos a função que executa o jogo 
