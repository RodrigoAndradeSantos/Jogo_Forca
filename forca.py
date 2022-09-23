import os
import random


print('JOGO DA FORCA!')
nome = input('Digite seu nome: ')
print (f'Olá {nome}! Vamos iniciar o jogo?')
input ('\nPressione Enter para iniciar')
os.system('cls')


lista_palavras = ['laranja','abacaxi','morango','acerola','banana','carambola','manga','maracuja','caqui']
palavra_selecionada = random.choice (lista_palavras).upper()
tamanho_palavra = len(palavra_selecionada)
palavra_codificada = ['_']*tamanho_palavra
quant_erros = 0


while '_' in palavra_codificada and quant_erros < 6:
    print (f'\nSua palavra tem {tamanho_palavra} letras e o tema é FRUTAS')
    print (f'Erros: {quant_erros} de 6')

    for letra in palavra_codificada:
        print (letra, end = ' ')
    print()


    letra_escolhida = input('Digite uma letra: ').upper()
    acertou = False
    for i in range(len(palavra_selecionada)):

        if letra_escolhida == palavra_selecionada[i]:
            palavra_codificada [i] = letra_escolhida
            acertou = True
        
    if acertou == True:
        print('Parabéns! Você acertou')
    else:
        print('Você errou! Essa letra não existe na palavra')
        quant_erros = quant_erros + 1
    
if quant_erros == 6:
    print('Você Perdeu!')
else:
    print('Parabéns! Você ganhou!')

print(f'A palavra selecionada era {palavra_selecionada}')