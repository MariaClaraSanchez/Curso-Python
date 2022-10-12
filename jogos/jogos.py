import forca
import adivinhacao

def escolha_jogos():
    print("**********************************")
    print("******* Escolha o seu jogo *******")
    print("**********************************")

    print("(1) Forca | (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca\n")
        forca.jogar_forca()
    elif (jogo == 2):
        print("Jogando adivinhação\n")
        adivinhacao.jogar_ad()

if(__name__ == "__main__"):
    escolha_jogos()