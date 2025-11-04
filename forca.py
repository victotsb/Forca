import os
oculta = []
vidas = 5
letras_usadas = []

def palavra_oculta(palavra):
    global oculta
    oculta = list("*" * len(palavra))
    return oculta

def systemvida():
    global vidas
    vidas -= 1

def jogar(palavra):
    global vidas, oculta, letras_usadas
    while True:
        print(f"Você tem {vidas}")
        print(f"Palavra {oculta}")
        print(f"Letras usadas: {letras_usadas}")
        #E se o fdp do jogador colocar um número?
        letra = input("Coloque uma letra: ").lower().strip()
        
        for index, i in enumerate(palavra):
            if i == letra:
                print(f"existe a letra {i} na posição {index}")
                oculta[index] = letra
                print(oculta)
            if i == guardar_letras:
                print("Letra já usada")
            elif not i in oculta:
                print(f"Não existe nenhuma letra {i} em nenhuma posição {index}")
                print(f"Perdeu uma vida: {systemvida(vida)}")

            
            




palavra = input("Adicione a palavra: ").lower().strip()
if palavra == " ":
    print("nenhuma palavra adicionada")
else:
    os.system("cls")



oculta = palavra_oculta(palavra)

print(f"Você tem {vida} vidas")
print("Jogador tente adivinhar a palavra")

print(oculta)
jogador_acertou(palavra, oculta)