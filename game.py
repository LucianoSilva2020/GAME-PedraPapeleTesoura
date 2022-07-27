from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua jogada?'))
print('-=' * 12)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 12)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')            
    else:
        print('Jogada inválida!')    
elif computador == 1: #computador jogou papel
    if jogador == 0:    
        print('Computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')                                        