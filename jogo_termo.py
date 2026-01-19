import os
import random

palavras = [
    "casa",
    "barco",
    "sonho",
    "tempo",
    "nuvem",
    "pedra",
    "rosto",
    "pista",
    "ponto",
    "verde",
    "fruta",
    "letra",
    "chave",
    "garfo",
    "manga",
    "matar",
    "cobra",
    "cuidar",
    "praia",
    "janela",
    "linha",
    "vento",
    "forca",
    "noite",
    "luzes",
    "escola",
    "dente",
    "carne",
    "cheio",
    "corpo",
    "disco",
    "rodas",
    "farol",
    "monte",
    "sinal",
    "leite",
    "beijo",
    "pulso",
    "banco",
    "mapa",
    "senha",
    "faixa",
    "salto",
    "amigo",
    "apoio",
    "honra",
    "grito",
    "dedo",
    "curta"
]
palavra_secreta = random.choice(palavras)
letras_acertadas = ''
tentativas = 0

while True:
    letra_ditada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_ditada) > 1:
        print('Digite apenas UMA letra.')
        continue

    if letra_ditada in palavra_secreta:
        letras_acertadas += letra_ditada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)

    # if palavra_formada == palavra_secreta:
    #     print(f'Parabéns, você ganhou com {tentativas} tentativas!')
    #     letras_acertadas = ''
    #     tentativas = 0

    if tentativas > len(palavra_secreta):
        os.system('cls')
        print(f'Perdeu! A palavra era: {palavra_secreta}')
        letras_acertadas = ''
        tentativas = 0
    elif tentativas <= len(palavra_secreta):
        if palavra_formada == palavra_secreta:
            os.system('cls')
            print(f'Parabéns, você ganhou! A palavra era {palavra_secreta}.')
            letras_acertadas = ''
            tentativas = 0