import random

def print_menu():
    print("************************************")
    print("**** Bem vind@ ao jogo da Forca ****")
    print("************************************\n")

def randon_palavra(caminho:str) -> str:

    arquivo = open(caminho,"r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())
    
    palavra_secreta = (palavras[random.randrange(0,len(palavras))]).upper()
    arquivo.close()

    return palavra_secreta

def print_msg_vencedor():
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
    print("\n")

def print_msg_perdedor(palavra_secreta:str):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}\n".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("\n")

def desenha_forca(erros:int):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print("\n")

def inicio_jogo(palavra_secreta:str):
    letras_acertadas = ["_" for letra in palavra_secreta] 

    ##for letra in palavra_secreta:
    ##   letras_acertadas.append("_")
    acertou = False
    enforcou = False 
    erros = 0

    print(letras_acertadas,"\n")
    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros=erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas , "\n")

    if acertou:
        print_msg_vencedor()
    else:
        print_msg_perdedor(palavra_secreta=palavra_secreta)

def jogar_forca():

    print_menu()

    palavra_secreta = randon_palavra(caminho = "palavras.txt")

    inicio_jogo(palavra_secreta = palavra_secreta)

if(__name__ == "__main__"):
    jogar_forca()