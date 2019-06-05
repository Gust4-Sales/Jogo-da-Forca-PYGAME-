from Game_Over import *
from Ganhou import *
import random

pg.init()
screen = pg.display.set_mode((900, 500))
pg.display.set_caption('JOGO DA FORCA')


def palavra_secreta():
    with open('Palavras.txt', 'r') as arq:
        lista_palavras = arq.readlines()
        palavra = random.choice(lista_palavras).strip()
    return palavra.upper()


# Tela Padrão que sempre vai ser chamada
def tela_fixa(background):
    font_grande = pg.font.SysFont('comicsansms', 26, bold=True)
    screen.fill(background)
    titulo = font_grande.render('JOGO DA FORCA', 1, cor_texto)
    screen.blit(titulo, (335, 30))

    base = pg.Surface((900, 10))
    haste = pg.Surface((20, 230))
    topo = pg.Surface((80, 15))
    laco = pg.Surface((3, 40))
    screen.blit(base, (0, 450))
    screen.blit(haste, (70, 220))
    screen.blit(topo, (90, 220))
    screen.blit(laco, (167, 235))


# Insere na tela quando o usuário digita uma letra
def entrada(player_entrada):
    font_pequena = pg.font.SysFont('comicsansms', 16)
    pedido = font_pequena.render('>>', 1, black)
    digitado = font_pequena.render(player_entrada, 1, black)
    screen.blit(pedido, (250, 240))
    screen.blit(digitado, (265, 240))


# Insere as letras chutadas na tela
chutes = []
def tentativas(tentativa=''):
    global chutes
    if tentativa not in chutes:
        chutes.append(tentativa)
    font_pequena = pg.font.SysFont('comicsansms', 16)
    imprime_tentativa = font_pequena.render('TENTATIVAS: ' + '  '.join(chutes), 1, black)
    screen.blit(imprime_tentativa, (250, 220))


# Seta a qntd de traços de acordo com o tamanho da palavra / troca os traços pelos chutes certos / verifica se ganhou
lines = []
def underscore(palavra, letra = ''):
    if len(lines) < 1:
        for x in range(0, len(palavra)):
            lines.append('_ ')

    for cont, char in enumerate(palavra):
        if letra == char:
            lines[cont] = letra + ' '

    font_pequena = pg.font.SysFont('comicsansms', 16)
    linhas = font_pequena.render(''.join(lines), 1, black)
    screen.blit(linhas, (250, 410))
    if '_ ' not in lines:
        return True

    return False



# Loop principal do Game
def game():
    palavra = palavra_secreta()
    chute = ''
    letras_digitadas = []
    erros = 0
    done = False

    while not done:
        tela_fixa(cor_fundo)
        entrada(chute)
        tentativas()
        ganhou = underscore(palavra)
        if ganhou:
            return 1, palavra
        perdeu = boneco(screen, erros)
        if perdeu:
            return 0, palavra

        # Checa os eventos in game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if len(chute) < 1:
                    if pg.K_a <= event.key <= pg.K_z:
                        chute = pg.key.name(event.key).upper()
                else:
                    if event.key == pg.K_BACKSPACE:
                        chute = chute[:-1]
                    if event.key == pg.K_RETURN:
                        tentativas(chute)
                        if chute in palavra and chute not in letras_digitadas:
                            underscore(palavra, chute)
                        if chute not in palavra and chute not in letras_digitadas:
                            erros += 1
                        letras_digitadas.append(chute)
                        chute = chute[:-1]
        pg.display.update()

resultado, palavra = game()
if resultado == 0:
    print('perdeu')
    over(screen, palavra)
else:
    print('ganhou')
    win(screen, palavra)