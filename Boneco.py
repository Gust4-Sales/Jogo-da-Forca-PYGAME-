import pygame as pg
from Cores import *


def game_over(tela):
    tela.fill(cor_fundo)
    font_grande = pg.font.SysFont('comicsansms', 26, bold=True)
    font_pequena = pg.font.SysFont('comicsansms', 16)
    pg.draw.line(tela, white, (169, 400), (198, 440), 5)
    eyes = font_pequena.render('x x', 1, black)
    tela.blit(eyes, (158, 280))
    final = font_grande.render('GAME OVER', 1, black)
    tela.blit(final, (375, 200))


def boneco(tela, erros):
    def cabeca():
        pg.draw.circle(tela, white, (169, 295), 20)

    def corpo():
        cabeca()
        pg.draw.line(tela, white, (169, 315), (169, 400), 5)

    def b_1():
        corpo()
        pg.draw.line(tela, white, (165, 320), (140, 350), 5)

    def b_2():
        b_1()
        pg.draw.line(tela, white, (173, 320), (195, 350), 5)

    def p_1():
        b_2()
        pg.draw.line(tela, white, (169, 400), (140, 440), 5)

    if erros == 1:
        cabeca()
    elif erros == 2:
        corpo()
    elif erros == 3:
        b_1()
    elif erros == 4:
        b_2()
    elif erros == 5:
        p_1()
    elif erros == 6:
        print('perdeu')
        return True

    return False
