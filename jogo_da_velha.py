#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:41:43 2019
@author: tiago      
"""
from random import choice
from sys import exit
from IPython.display import clear_output

board = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
print_board = '      1 | 2 | 3\n      ---------\n      4 | 5 | 6\n      ---------\n      7 | 8 | 9'
p1 = ['Jogador1','O',[]]
p2 = ['Jogador2','X',[]]
jogada = 0
seq = [1,2]
casas = '123456789'
casa = ''
escolha = ', é a sua vez. Lembre-se, você é o'
escolha_jogada = 'Escolha sua jogada: '
casa_selecionada = 'Esta casa já foi selecionada. Escolha outra.\n'
casa_valida = 'Por favor, selecione uma casa valida\n'
gabarito = [['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['7','5','3']]
j1n0 = 0
j1n1 = 0
j1n2 = 0
j1n3 = 0
j1n4 = 0
j1n5 = 0
j1n6 = 0
j1n7 = 0
j2n0 = 0
j2n1 = 0
j2n2 = 0
j2n3 = 0
j2n4 = 0
j2n5 = 0
j2n6 = 0
j2n7 = 0
opcoes = []

def nomear_jogador():
    global p1
    global p2
    p1[0] = input('Digite o nome do Jogador 1 (Bola): ')
    p2[0] = input('Digite o nome do Jogador 2 (Xis): ')
    return

def reset_part():
    global board
    global print_board
    global casas
    global jogada
    global p1
    global p2
    global j1n0
    global j1n1
    global j1n2
    global j1n3
    global j1n4
    global j1n5
    global j1n6
    global j1n7
    global j2n0
    global j2n1
    global j2n2
    global j2n3
    global j2n4
    global j2n5
    global j2n6
    global j2n7
    board = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
    print_board = '\n\n      1 | 2 | 3\n      ---------\n      4 | 5 | 6\n      ---------\n      7 | 8 | 9\n\n'
    casas = '123456789'
    jogada = 0
    p1[2] = []
    p2[2] = []
    j1n0 = 0
    j1n1 = 0
    j1n2 = 0
    j1n3 = 0
    j1n4 = 0
    j1n5 = 0
    j1n6 = 0
    j1n7 = 0
    j2n0 = 0
    j2n1 = 0
    j2n2 = 0
    j2n3 = 0
    j2n4 = 0
    j2n5 = 0
    j2n6 = 0
    j2n7 = 0
    return

def inicio_random():
    global jogada
    jogada = choice(seq)
    return jogada

def guarda_jogador():
    global casas
    casas = casas.replace(casa, '')
    if jogada == 1:
        p1[2].append(casa)
    elif jogada == 2:
        p2[2].append(casa)
    return casas

def altera_board():
    if jogada == 1:
        board[casa] = p1[1]
    elif jogada == 2:
        board[casa] = p2[1]
    else:
        print('Erro em altera_board()')
    return

def printa_board():
    global print_board
    if jogada == 1:
        print_board = print_board.replace(casa,'O')
    elif jogada == 2:
        print_board = print_board.replace(casa,'X')
    else:
        print('Erro em printa_board()')
    return

def return_jogo():
    global opcoes
    print('O que você gostaria de fazer agora?\n\n(n) novo jogo\n(m) mudar jogadores\n(s) sair\n')
    escolha = input('Selecione uma opção: ')
    if escolha != 'n' and escolha != 'm' and escolha != 's':
        print('Escolha uma opção válida!\n')
    elif escolha == 'n':
        opcoes = partida()
    elif escolha == 'm':
        opcoes = nova_partida()
    elif escolha == 's':
        opcoes = sair()
    return

def sair(): return exit()
      
def fim_jogo():
    return_jogo()
    return fim_jogo()

def ver_fimdejogo():
    if len(casas) == 0:
        print('Empate! Vocês são igualmente bons. Ou igualmente ruins!\n')
        fim_jogo()
    pass

def mensagem_campeao():
    if jogada == 1:
        print('>>>PARABÉNS',p1[0].upper(),'!!! VOCÊ VENCEU!<<<\n')
    elif jogada == 2:
        print('>>>PARABÉNS',p2[0].upper(),'!!! VOCÊ VENCEU!<<<\n')
    return

def ver_vencedor():
    global j1n0
    global j1n1
    global j2n0
    global j2n1
    global j1n2
    global j1n3
    global j1n4
    global j1n5
    global j1n6
    global j1n7
    global j2n0
    global j2n1
    global j2n2
    global j2n3
    global j2n4
    global j2n5
    global j2n6
    global j2n7
    global gabarito
    conta = [0,1,2]
    if jogada == 1:
        for x in conta:
            if gabarito[0][x] == casa:
                j1n0+=1
                if j1n0 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[1][x] == casa:
                j1n1+=1
                if j1n1 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[2][x] == casa:
                j1n2+=1
                if j1n2 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[3][x] == casa:
                j1n3+=1
                if j1n3 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[4][x] == casa:
                j1n4+=1
                if j1n4 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[5][x] == casa:
                j1n5+=1
                if j1n5 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[6][x] == casa:
                j1n6+=1
                if j1n6 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[7][x] == casa:
                j1n7+=1
                if j1n7 == 3:
                    mensagem_campeao()
                    fim_jogo()
    elif jogada == 2:
        for x in conta:
            if gabarito[0][x] == casa:
                j2n0+=1
                if j2n0 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[1][x] == casa:
                j2n1+=1
                if j2n1 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[2][x] == casa:
                j2n2+=1
                if j2n2 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[3][x] == casa:
                j2n3+=1
                if j2n3 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[4][x] == casa:
                j2n4+=1
                if j2n4 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[5][x] == casa:
                j2n5+=1
                if j2n5 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[6][x] == casa:
                j2n6+=1
                if j2n6 == 3:
                    mensagem_campeao()
                    fim_jogo()
        for x in conta:
            if gabarito[7][x] == casa:
                j2n7+=1
                if j2n7 == 3:
                    mensagem_campeao()
                    fim_jogo()
    else:
        print('Erro ver_vencedor()')
    return

def partida_rodando():
    global jogada
    global casa 
    global casas
    n = 1
    print(f'\nPreparados para começar? Boa sorte {p1[0]} e {p2[0]}')
    print(print_board)
    while n <= 9:
        if jogada == 1:
            print(p1[0], escolha,p1[1])
            casa = input(escolha_jogada)
            if len(casa) == 1 and casa.isdigit() and casa !='' and casa !='0':
                if casa in casas:
                    #print(n)
                    n+=1
                    guarda_jogador()
                    #print(casas)
                    #print(p1)
                    #print(p2)
                    altera_board()
                    printa_board()
                    print(print_board)
                    ver_vencedor()
                    ver_fimdejogo()
                    jogada = 2
                else:
                    print(casa_selecionada)
                    print(n)
            else:
                print(casa_valida)
                print(n)
        elif jogada == 2:
            print(p2[0], escolha,p2[1])
            casa = input(escolha_jogada)
            if len(casa) == 1 and casa.isdigit() and casa !='' and casa !='0':
                if casa in casas:
                    #print(n)
                    n+=1
                    guarda_jogador()
                    #print(casas)
                    #print(p1)
                    #print(p2)
                    altera_board()
                    printa_board()
                    print(print_board)
                    ver_vencedor()
                    ver_fimdejogo()
                    jogada = 1
                else:
                    print(casa_selecionada)
            else:
                print(casa_valida)
                
        else:
            print('Erro em partida()')
    return

def nova_partida():
    reset_part()
    nomear_jogador()
    inicio_random()
    partida_rodando()
    return

def partida():
    reset_part()
    inicio_random()
    partida_rodando()
    return

nova_partida()