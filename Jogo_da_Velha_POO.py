import os
from time import sleep

# Criando a classe dos jogadores
class Jogador:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

# Criando o dicionário 'campo', para que possamos acessar as hashs depois e efetuar as jogadas.
campo = {'1' : '_', '2' : '_', '3' : '_',
         '4' : '_', '5' : '_', '6' : '_',
         '7' : '_', '8' : '_', '9' : '_'}

# Montando a função responsável pela jogada
def desenha_campo(tipo):  
    os.system('cls')
    print(f'|{campo["1"]}|{campo["2"]}|{campo["3"]}|')
    sleep(1)
    print(f'|{campo["4"]}|{campo["5"]}|{campo["6"]}|')
    sleep(1)
    print(f'|{campo["7"]}|{campo["8"]}|{campo["9"]}|')

print('-=' * 10, 'Olá, bem vindo ao meu jogo da velha!', '-=' * 10)
print()

# Verificando qual o tipo o jogador 1 irá jogar, X ou O
tipo_jogador1 = input('Por favor, Jogador 1, digite o que você deseja ser: [x] para X e [o] para O: ').upper()
while tipo_jogador1 not in 'XOQ':
    tipo_jogador1 = input('Por favor, digite x ou o. Para sair do jogo, digite "q": ').upper()
    if tipo_jogador1 == 'q':
        exit()
# Criando o objeto da classe Jogador
if tipo_jogador1 == 'x':
    jogador1 = Jogador('Jogador 1', tipo_jogador1)
    jogador2 = Jogador('Jogador 2', 'O')
else:
    jogador1 = Jogador('Jogador 2', 'X')
    jogador2 = Jogador('Jogador 1', 'O')

os.system('cls')
print('-=' * 4, 'Olá, bem vindo ao meu jogo da velha!', '-=' * 4)
print()
print(f'Muito bem! o [{jogador1.nome}] será "{jogador1.tipo}" e o [{jogador2.nome}] será "{jogador2.tipo}"')
sleep(2.5)
os.system('cls')
print('Criando o campo de batalha...')
print('|_|_|_|')
sleep(1)
print('|_|_|_|')
sleep(1)
print('|_|_|_|')

# Fazendo a primeira jogada e checando se o valor digitado é um número e se está dentro dos parâmetros do jogo
print(f'Pela regra, o jogador X é quem começa jogando, portanto será o [{jogador1.nome}]')
jogada = input(f'Por favor, {jogador1.nome} digite um número entre 1 e 9: ')
checando = True
while checando:
    try:    
        while int(jogada) > 9 or int(jogada) < 1:
            jogada = input(f'Por favor, digite um número entre 1 e 9: ')
        checando = False
    except:
        jogada = input(f'Por favor, digite um número entre 1 e 9: ')

campo[jogada] = jogador1.tipo
os.system('cls')
print(f'|{campo["1"]}|{campo["2"]}|{campo["3"]}|')
sleep(1)
print(f'|{campo["4"]}|{campo["5"]}|{campo["6"]}|')
sleep(1)
print(f'|{campo["7"]}|{campo["8"]}|{campo["9"]}|')

# Criando uma tupla para checar os espaços que já foram jogados
checar_jogadas = tuple()
checar_jogadas = jogada
contador = 1
# Criando um for para realizar as 9 jogadas do jogo. Realizamos o mesmo processo de tratamento, para caso os inputs sejam exceções ou diferentes dos parâmetros
for i in range(0,8):
    checando = True
    if contador % 2 == 0:
        jogada = input(f'Por favor, {jogador1.nome} digite um número entre 1 e 9: ')
        while checando:
            try:
                while jogada in checar_jogadas:
                    jogada = input(f'O número digitado já foi escolhido anteriormente, por favor digite outro número: ')
                while int(jogada) > 9 or int(jogada) < 1:
                    jogada = input(f'Por favor, digite um número entre 1 e 9: ')
                campo[jogada] = jogador1.tipo
                checando = False
                checar_jogadas += jogada
            except:
                jogada = input(f'Por favor, digite um número entre 1 e 9: ')

    # Verificando se há vitória nas linhas do jogador 1
        if campo['1'] == campo['2'] == campo['3'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador1.nome} você venceu usando [{jogador1.tipo}]')
            break
        if campo['4'] == campo['5'] == campo['6'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador1.nome} você venceu usando [{jogador1.tipo}]')
            break
        if campo['7'] == campo['8'] == campo['9'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador1.nome} você venceu usando [{jogador1.tipo}]')
            break

        # Verificando se há vitória nas colunas do jogador 1
        if campo['1'] == campo['4'] == campo['7'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador1.nome} você venceu usando [{jogador1.tipo}]')
            break
        if campo['2'] == campo['5'] == campo['8'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador1.nome} você venceu usando [{jogador1.tipo}]')
            break
        if campo['3'] == campo['6'] == campo['9'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador1.nome} você venceu usando [{jogador1.tipo}]')
            break

        # Verificando se há vitória nas diagonais do jogador 1
        if campo['1'] == campo['5'] == campo['9'] != '_':
            print(f'Parabéns! {jogador1.nome} você venceu usando [{jogador1.tipo}]')
            break
        if campo['3'] == campo['5'] == campo['7'] != '_':
            print(f'Parabéns! {jogador1.nome} você venceu usando [{jogador1.tipo}]')
            break           
    else:
        jogada = input(f'Por favor, {jogador2.nome} digite um número entre 1 e 9: ')
        while checando:
            try:
                while jogada in checar_jogadas:
                    jogada = input(f'O número digitado já foi escolhido anteriormente, por favor digite outro número: ')
                while int(jogada) > 9 or int(jogada) < 1:
                    jogada = input(f'Por favor, digite um número entre 1 e 9: ')
                campo[jogada] = jogador2.tipo
                checando = False
                checar_jogadas += jogada
            except:
                jogada = input(f'Por favor, digite um número entre 1 e 9: ')

        # Verificando se há vitória nas linhas do jogador 2
        if campo['1'] == campo['2'] == campo['3'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador2.nome} você venceu usando [{jogador2.tipo}]')
            break
        if campo['4'] == campo['5'] == campo['6'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador2.nome} você venceu usando [{jogador2.tipo}]')
            break
        if campo['7'] == campo['8'] == campo['9'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador2.nome} você venceu usando [{jogador2.tipo}]')
            break

        # Verificando se há vitória nas colunas do jogador 2
        if campo['1'] == campo['4'] == campo['7'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador2.nome} você venceu usando [{jogador2.tipo}]')
            break
        if campo['2'] == campo['5'] == campo['8'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador2.nome} você venceu usando [{jogador2.tipo}]')
            break
        if campo['3'] == campo['6'] == campo['9'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador2.nome} você venceu usando [{jogador2.tipo}]')
            break

        # Verificando se há vitória nas diagonais do jogador 2
        if campo['1'] == campo['5'] == campo['9'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador2.nome} você venceu usando [{jogador2.tipo}]')
            break
        if campo['3'] == campo['5'] == campo['7'] != '_':
            desenha_campo(jogada)
            print(f'Parabéns! {jogador2.nome} você venceu usando [{jogador2.tipo}]')
            break
    contador += 1
    desenha_campo(jogada)
    if contador > 8:
        print('O jogo empatou!')




