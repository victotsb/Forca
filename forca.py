import os
oculta = []
vidas = 5
letras_usadas = []

def palavra_oculta(palavra):
    global oculta
    oculta = list(palavra.replace(" ", " "))
    for i in range(len(oculta)):
        if oculta[i] != " ":
            oculta[i] = "*"
    return oculta

def sistema_de_vida():
    global vidas
    vidas -= 1

def verificação_da_letra_do_jogador(letra):
    if not letra:
        print("Coloque uma letra!")
        return False
    elif len(letra) != 1:
        print("Coloque só uma letra")
        return False
    elif not letra.isalpha():
        print("Coloque só letras, não números nem símbolos")
        return False
    elif letra in letras_usadas:
        print("Você já usou essa letra, tente novamente")
        return False
    else:
        return True 
         
def jogador_ganhou_ou_perdeu(palavra):
    if "*" not in oculta:
        print("Você acertou a palavra: ", palavra)
        return True
        
    if vidas == 0:
        print("Acabaram suas vidas, você perdeu o jogo, a palavra era: ", palavra)
        return True
    return False

def verifica_se_tem_letra_na_palavra(letra, palavra):
    if letra in palavra:
        for index, i in enumerate(palavra):
            if i == letra:
                oculta[index] = letra
        print("Você acertou uma letra")
    else:
        sistema_de_vida()
        print("Você errou a letra, perdeu uma vida! Tente novamente")

def sistema_do_jogo(palavra):
    global letras_usadas
    while True:
        print(f"Palavra:", "".join(oculta))
        print(f"Letras usadas: {',' .join(letras_usadas)}")
        print(f"Você tem {vidas} vidas")

        letra = input("Coloque uma letra: ").lower().strip()
        if not verificação_da_letra_do_jogador(letra):
            continue
        letras_usadas.append(letra)

        verifica_se_tem_letra_na_palavra(letra, palavra)

        if jogador_ganhou_ou_perdeu(palavra):
            break

def adicionar_palavra_para_jogar(palavra_oculta, sistema_do_jogo):
    while True:
        palavra = input("Adicione a palavra: ").lower()
        if palavra == "":
            print("nenhuma palavra adicionada")
        elif not palavra.replace(" ", "").isalpha():
            print("Coloque só letras e espaços, não números nem símbolos")
        else:
            os.system("cls")
            palavra_oculta(palavra)
            print("Tente adivnhar a palavra")
            sistema_do_jogo(palavra)
            break

adicionar_palavra_para_jogar(palavra_oculta, sistema_do_jogo)