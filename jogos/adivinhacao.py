import random

def print_menu():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************\n")

def nivel() -> int:

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5
    
    return tentativas

def print_msg_vencedor(pontos:int):
    print(f"Parabéns, você ganhou! E fez {pontos}")
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

def print_msg_perdedor(numero:int):
    print("\nPuxa, perdeu!")
    print(f"O número secreto era {numero}!!")
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

def iniciar_jogo():

    # numero_secreto = round(random.random() * 100) #0.0 a 1.0
    numero_secreto = random.randrange(1,101)
    #print(numero_secreto)
    tentativas = nivel()

    rodada = 1;
    pontos = 1000

    while rodada <= tentativas:
        
        print(f'Tentativa:{rodada} de {tentativas}')
        chute = int(input("Digite o seu número entre 1 e 100: "))

        if chute < 1 or chute > 100 :
            print("Digite um número enre 1 e 100!! ")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto 

        if acertou:
            print_msg_vencedor(pontos=pontos)
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute);
            if rodada == tentativas:
                    print_msg_perdedor(numero=numero_secreto)
                    break
            if maior:
                print("Você errou! Seu chute foi maior que o número secreto! Você perdeu {} pontos".format(pontos_perdidos))
                
            elif menor:
                print("Você errou! Seu chute foi menor que o número secreto! Você perdeu {} pontos".format(pontos_perdidos))
            
        rodada +=1
        pontos -= pontos_perdidos


def jogar_ad():

    print_menu()
    iniciar_jogo()
    print("Fim do Jogo!\n")

if(__name__ == "__main__"):
    jogar_ad()

