import pygame
import resources
import config
import textos
import random

# Dicionário de posicionamento do menu
#                       XY Botao,  XY Texto
menuDic = {'btStart': [(22, 300), (131, 451)], 'btConfig': [(22, 425), (275, 531)],
           'btAvatar': [(580, 300), (503, 461)], 'nomeJogo': (0, 0), 'btVoltar': [(488, 529), (560, 540)],
           'btLeft': (77, 434), 'btRight': (393, 434), 'opcaoIdioma': (152, 454), 'nomeMenu': (625, 195), 'posAvatarMenu': (365, 320), 'posAvatarLoja': (185, 266), 'btLeftAvatar': (77, 434), 'btRightAvatar': (343, 434),
           'nomeTexto': (39, 514), 'contrato1': (325, 30), 'contrato2': (50, 120), 'contrato3': (30, 200), 'contrato4': (350, 250), 'contrato5': (50, 320), 'contrato6': (200, 380)}
# /Dicionário de posicionamento do menu

# Dicionário de posicionamento In-Game
jogoDic = {'posCartaPlayer1': [(309, 525), (375, 525), (441, 525)], 'posCartaPlayer2': [(716, 388), (716, 340), (716, 290)], 'posCartaPlayer3': [(16, 278), (16, 328), (16, 378)],
           'posJogada': [(343, 290), (416, 388), (546, 278)], 'posBralho': (192, 290), 'posCartaVirada': (242, 290), 'posPontoJogador1': (692, 512), 'posPontoJogador2': (692, 55), 'posPontoJogador3': (68, 57),
           'posTextoRodada': (292, 8), 'posTextoNomeJogador1': (546, 525), 'posBgFundoAvatar': [(684, 475), (675, 23), (7, 24)], 'posAvatar': [(740, 490), (730, 34), (7, 34)]}
# /Dicionário de posicionamento In-Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(config.TITULO)
clock = pygame.time.Clock()

# inicialização das Variaveis instanciadas
botao = pygame.image.load(resources.BOTAO)
botao2 = pygame.image.load(resources.BOTAO2)

backgroundMenu = pygame.image.load(resources.BACKGROUND_MENU)
backgroundJogo = pygame.image.load(resources.BACKGROUND_JOGO)

baralhoImg = pygame.image.load(resources.BARALHO)

logoProjetoK = pygame.image.load(resources.LOGOK)
imgProjetoK = pygame.image.load(resources.PROJETOK)

imgCG = pygame.image.load(resources.IMAGEM_CG)

fundoCarta = pygame.image.load(resources.FUNDO_CARTA)
fundoAvatarBg = pygame.image.load(resources.FUNDO_AVATAR)

spriteSheetAvatar = (resources.spriteAvatar())

left = pygame.image.load(resources.LEFT)
right = pygame.image.load(resources.RIGHT)




pygame.mixer.init()
gameplayMusic = pygame.mixer.music.load(resources.gameplayMusic)
fxCardAnim = pygame.mixer.Sound(resources.fxCardAnim)

logo = (resources.spriteLogo())
anim = (resources.spriteCG())
hudMenu = (resources.spriteMenu())
avatarMirror = pygame.image.load(resources.AVATAR_MIRROR)
avatarMenu = (resources.avatarMenu())

avatarSelect = 0

# /inicialização das Variaveis instanciadas

global cronometro1, cronometro2, contadorG
cronometro1, cronometro2, contadorG = 0, 0, 0


pygame.font.init()


def abertura(apresentacao):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    global cronometro1, contadorG

    screen.fill(resources.BRANCO)

    font = pygame.font.SysFont('Cooper Black', 45)

    if apresentacao == 1:
        cronometro1 += 1
        if cronometro1 <= 10:
           logo.draw(screen, 0, 160, 190, 0)
        elif 5 < cronometro1 <= 10:
            logo.draw(screen, 1, 160, 190, 0)
        elif 10 < cronometro1 <= 15:
            logo.draw(screen, 2, 160, 190, 0)
        elif 15 < cronometro1 <= 20:
            logo.draw(screen, 3, 160, 190, 0)
        elif 20 < cronometro1 <= 25:
            logo.draw(screen, 4, 160, 190, 0)
        elif 25 < cronometro1 <= 30:
            logo.draw(screen, 5, 160, 190, 0)
        elif 30 < cronometro1 <= 35:
            logo.draw(screen, 6, 160, 190, 0)
        elif 35 < cronometro1 <= 40:
            logo.draw(screen, 7, 160, 190, 0)
        elif 40 < cronometro1 <= 45:
            logo.draw(screen, 8, 160, 190, 0)
        elif 45 < cronometro1 <= 50:
            logo.draw(screen, 9, 160, 190, 0)
        elif 50 < cronometro1 <= 55:
            logo.draw(screen, 10, 160, 190, 0)
        else:
            logo.draw(screen, 11, 160, 190, 0)
            cronometro1 = 0
            contadorG = -100
            apresentacao += 1

    elif apresentacao == 2:
        cronometro1 += 1
        logo.draw(screen, 11, 160, 190, 0)
        if contadorG < 270:
            screen.blit(font.render('Apresenta', 1, resources.PRETO), (contadorG, 439))
            contadorG += 20
        else:
            screen.blit(font.render('Apresenta', 1, resources.PRETO), (270, 439))
            if cronometro1 > 50:
                apresentacao += 1
                cronometro1 = 0
                contadorG = 0


    elif apresentacao == 3:
        screen.blit(logoProjetoK, (0, 0))
        cronometro1 += 1
        if cronometro1 >60:
            screen.blit(imgProjetoK, (0, 0))
            print(cronometro1)
            cronometro1 += 1
        if cronometro1 > 200:
            apresentacao += 1
            cronometro1 = 0

    elif apresentacao == 4:

        # screen.blit(imgCG, (0, 0))
        # cronometro1 += 1

        cronometro1 += 1
        if cronometro1 <= 10:
            anim.draw(screen, 0, 0, 0, 0)
        elif 5 < cronometro1 <= 10:
            anim.draw(screen, 1, 0, 0, 0)
        elif 10 < cronometro1 <= 15:
            anim.draw(screen, 2, 0, 0, 0)
        elif 15 < cronometro1 <= 20:
            anim.draw(screen, 3, 0, 0, 0)
        elif 20 < cronometro1 <= 25:
            anim.draw(screen, 4, 0, 0, 0)
        elif 25 < cronometro1 <= 30:
            anim.draw(screen, 5, 0, 0, 0)
        elif 30 < cronometro1 <= 35:
            anim.draw(screen, 6, 0, 0, 0)
        elif 35 < cronometro1 <= 40:
            anim.draw(screen, 7, 0, 0, 0)
        elif 40 < cronometro1 <= 45:
            anim.draw(screen, 8, 0, 0, 0)
        elif 45 < cronometro1 <= 50:
            anim.draw(screen, 9, 0, 0, 0)
        elif 50 < cronometro1 <= 55:
            anim.draw(screen, 10, 0, 0, 0)
        elif 55 < cronometro1 <= 60:
            anim.draw(screen, 11, 0, 0, 0)
        elif 60 < cronometro1 <= 65:
            anim.draw(screen, 12, 0, 0, 0)
        elif 65 < cronometro1 <= 70:
            anim.draw(screen, 13, 0, 0, 0)
        elif 70 < cronometro1 <= 75:
            anim.draw(screen, 14, 0, 0, 0)
        elif 75 < cronometro1 <= 80:
            anim.draw(screen, 15, 0, 0, 0)
        elif 80 < cronometro1 <= 85:
            anim.draw(screen, 16, 0, 0, 0)
        elif 85 < cronometro1 <= 90:
            anim.draw(screen, 17, 0, 0, 0)
        elif 90 < cronometro1 <= 95:
            anim.draw(screen, 18, 0, 0, 0)
        elif 95 < cronometro1 <= 100:
            anim.draw(screen, 19, 0, 0, 0)
        elif 100 < cronometro1 <= 105:
            anim.draw(screen, 20, 0, 0, 0)
        elif 105 < cronometro1 <= 110:
            anim.draw(screen, 21, 0, 0, 0)
        elif 110 < cronometro1 <= 115:
            anim.draw(screen, 22, 0, 0, 0)
        elif 115 < cronometro1 <= 120:
            anim.draw(screen, 22, 0, 0, 0)
        elif 120 < cronometro1 <= 125:
            anim.draw(screen, 23, 0, 0, 0)
        elif 125 < cronometro1 <= 130:
            anim.draw(screen, 23, 0, 0, 0)
        elif 130 < cronometro1 <= 140:
            anim.draw(screen, 24, 0, 0, 0)
        elif 140 < cronometro1 <= 280:
            anim.draw(screen, 24, 0, 0, 0)
        else:
            anim.draw(screen, 24, 0, 0, 0)
            cronometro1 = 0
            contadorG = -100
            apresentacao += 1
            cronometro1 = 0
            return 'escreverNome', 0

    return 'abertura', apresentacao


def enterNomePlayer(idioma, nome):
    font = pygame.font.SysFont('Cooper Black', 45)
    font2 = pygame.font.SysFont('Cooper Black', 35)
    mouse = pygame.mouse.get_pos()
    screen.fill(resources.PRETO)

    texto = font.render(nome, 1, resources.BRANCO)

    screen.blit(font2.render((idioma['contrato1']), 1, resources.BRANCO), menuDic['contrato1'])
    screen.blit(font2.render((idioma['contrato2']), 1, resources.BRANCO), menuDic['contrato2'])
    screen.blit(font2.render((idioma['contrato3']), 1, resources.BRANCO), menuDic['contrato3'])
    screen.blit(font2.render((idioma['contrato4']), 1, resources.BRANCO), menuDic['contrato4'])
    screen.blit(font2.render((idioma['contrato5']), 1, resources.BRANCO), menuDic['contrato5'])
    screen.blit(font2.render((idioma['contrato6']), 1, resources.BRANCO), menuDic['contrato6'])

    nome = nome.split()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                for i in range(len(nome)):
                    if nome[i] == '_':
                        nome[i] = event.unicode
                        break
            if event.key == pygame.K_BACKSPACE:
                for i in range(len(nome)):
                    if nome[i] == '_':
                        nome[i - 1] = '_'
                        break
                    elif i == (len(nome) - 1):
                        nome[i] = '_'
            if event.key == pygame.K_SPACE:
                for i in range(len(nome)):
                    if nome[i] == '_':
                        nome[i] = '-'
                        break
            if event.key == pygame.K_ESCAPE:
                print('Esc')
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                nomeTemp = ' '.join(str(nome) for nome in nome)
                nomeTemp = nomeTemp.replace('_', '')
                nomeTemp = nomeTemp.replace(' ', '')
                return 'menu', nomeTemp

    nomeTemp = ' '.join(str(nome) for nome in nome)
    screen.blit(texto, menuDic['nomeTexto'])

    return 'escreverNome', nomeTemp


def menu(idioma, nome, avatarJogador):
    font = pygame.font.SysFont('Cooper Black', 45)
    mouse = pygame.mouse.get_pos()
    anim.draw(screen,23,0,0,0)

    botaoRetIniciar = pygame.Rect(menuDic['btStart'][0][0], menuDic['btStart'][0][1], hudMenu.cellWidth, hudMenu.cellHeight)
    botaoRetConfigurar = pygame.Rect(menuDic['btConfig'][0][0], menuDic['btConfig'][0][1], botao.get_width(), botao.get_height()) #hudMenu.rect#
    botaoRetAvatar = pygame.Rect(menuDic['btAvatar'][0][0], menuDic['btAvatar'][0][1], botao.get_width(), botao.get_height())#hudMenu.rect#

    if botaoRetIniciar.collidepoint(mouse):
        hudMenu.draw(screen, 0, menuDic['btStart'][0][0], menuDic['btStart'][0][1], 0)
    else:
        hudMenu.draw(screen, 1, menuDic['btStart'][0][0], menuDic['btStart'][0][1], 0)

    if botaoRetConfigurar.collidepoint(mouse):
        hudMenu.draw(screen, 4, menuDic['btConfig'][0][0], menuDic['btConfig'][0][1], 0)
    else:
        hudMenu.draw(screen, 5, menuDic['btConfig'][0][0], menuDic['btConfig'][0][1], 0)

    if botaoRetAvatar.collidepoint(mouse):
        hudMenu.draw(screen, 8, menuDic['btAvatar'][0][0], menuDic['btAvatar'][0][1], 0)
    else:
        hudMenu.draw(screen, 9, menuDic['btAvatar'][0][0], menuDic['btAvatar'][0][1], 0)


    screen.blit(font.render(nome, 1, resources.PRETO), menuDic['nomeMenu'])
    screen.blit(avatarMirror,(305,285))
    avatarMenu.draw(screen, avatarSelect, 365,320)
    #screen.blit(pygame.transform.flip(pygame.transform.scale2x(spriteSheetAvatar[avatarJogador[0]]), -1, 0), (305,205))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botaoRetIniciar.collidepoint(mouse):
                print('Iniciar Jogo')
                return 'jogando', avatarJogador

            elif botaoRetConfigurar.collidepoint(mouse):
                print('Trocar para config')
                return 'configuracao', avatarJogador
            elif botaoRetAvatar.collidepoint(mouse):
                return 'avatar', avatarJogador
    return 'menu', avatarJogador


def configuracao(idioma, idiomaTexto):
    font = pygame.font.SysFont('Cooper Black', 45)
    mouse = pygame.mouse.get_pos()
    screen.blit(backgroundMenu, (0, 0))
    botaoRetVoltar = pygame.Rect(menuDic['btVoltar'][0][0], menuDic['btVoltar'][0][1], botao.get_width(), botao.get_height())
    botaoRetLeft = pygame.Rect(menuDic['btLeft'][0], menuDic['btLeft'][1], left.get_width(), left.get_height())
    botaoRetRight = pygame.Rect(menuDic['btRight'][0], menuDic['btRight'][1], right.get_width(), right.get_height())

    screen.blit(left, menuDic['btLeft'])
    screen.blit(right, menuDic['btRight'])

    screen.blit(font.render(idiomaTexto, 1, resources.PRETO), menuDic['opcaoIdioma'])
    if botaoRetVoltar.collidepoint(mouse):
        screen.blit(botao2, menuDic['btVoltar'][0])
    else:
        screen.blit(botao, menuDic['btVoltar'][0])
    screen.blit(font.render(idioma['voltar'], 1, resources.PRETO), menuDic['btVoltar'][1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botaoRetVoltar.collidepoint(mouse):
                return 'menu', idiomaTexto, idioma
            elif botaoRetLeft.collidepoint(mouse) or botaoRetRight.collidepoint(mouse):
                if idiomaTexto == 'Português':
                    idiomaTexto = 'Inglês'
                    idioma = textos.dicIngles
                else:
                    idiomaTexto = 'Português'
                    idioma = textos.dicPortugues

        screen.blit(font.render(idiomaTexto, 1, resources.PRETO), menuDic['opcaoIdioma'])
    return 'configuracao', idiomaTexto, idioma


def avatar(idioma, avatarJogador):
    font = pygame.font.SysFont('Cooper Black', 45)
    mouse = pygame.mouse.get_pos()
    screen.blit(backgroundMenu, (0, 0))
    botaoRetVoltar = pygame.Rect(menuDic['btVoltar'][0][0], menuDic['btVoltar'][0][1], botao.get_width(), botao.get_height())
    botaoRetLeft = pygame.Rect(menuDic['btLeftAvatar'][0], menuDic['btLeftAvatar'][1], left.get_width(), left.get_height())
    botaoRetRight = pygame.Rect(menuDic['btRightAvatar'][0], menuDic['btRightAvatar'][1], right.get_width(), right.get_height())

    if botaoRetVoltar.collidepoint(mouse):
        screen.blit(botao2, menuDic['btVoltar'][0])
    else:
        screen.blit(botao, menuDic['btVoltar'][0])
    screen.blit(font.render(idioma['voltar'], 1, resources.PRETO), menuDic['btVoltar'][1])

    screen.blit(left, menuDic['btLeftAvatar'])
    screen.blit(right, menuDic['btRightAvatar'])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botaoRetVoltar.collidepoint(mouse):
                return 'menu', avatarJogador
            if botaoRetLeft.collidepoint(mouse):
                if avatarJogador[0] < 3:
                    avatarJogador[0] += 1
                else:
                    avatarJogador[0] = 0
            if botaoRetRight.collidepoint(mouse):
                if avatarJogador[0] < 3:
                    avatarJogador[0] += 1
                else:
                    avatarJogador[0] = 0

    screen.blit(pygame.transform.scale2x(spriteSheetAvatar[avatarJogador[0]]), menuDic['posAvatarLoja'])

    return 'avatar', avatarJogador




def entregarCartas(baralho):
    cartasPlayer = [[None, None, None], [None, None, None], [None, None, None]]
    for i in range(3):
        for j in range(3):
            while True:
                cartasPlayer[i][j] = random.randint(0, len(baralho) - 1)
                if baralho[cartasPlayer[i][j]] is not None:
                    break
            baralho[cartasPlayer[i][j]] = None

    for i in range(24):
        if i % 4 == 0:
            print('')
        print(baralho[i], end=' ')

    return cartasPlayer, baralho


def inverterPosCartas(spritesBaralho, cartasInverter=[]):
    temp = [0] * 4
    for i in range(4):
        temp[i] = spritesBaralho[cartasInverter[i]]
    while i >= 0:
        spritesBaralho.remove(spritesBaralho[cartasInverter[i]])
        i -= 1
    for i in range(4):
        spritesBaralho.append(temp[i])

    return spritesBaralho


def virarCarta(baralho, spritesBaralho):
    while True:
        cartaVirada = random.randint(0, len(baralho) - 1)
        if baralho[cartaVirada] is not None:
            break
    baralho[cartaVirada] = None
    print('\nVirou', cartaVirada)
    if 0 <= cartaVirada <= 3:
        spritesBaralho = inverterPosCartas(spritesBaralho, [4, 5, 6, 7])
    elif 4 <= cartaVirada <= 7:
        spritesBaralho = inverterPosCartas(spritesBaralho, [8, 9, 10, 11])
    elif 8 <= cartaVirada <= 11:
        spritesBaralho = inverterPosCartas(spritesBaralho, [12, 13, 14, 15])
    elif 12 <= cartaVirada <= 15:
        spritesBaralho = inverterPosCartas(spritesBaralho, [16, 17, 18, 19])
    elif 16 <= cartaVirada <= 19:
        spritesBaralho = inverterPosCartas(spritesBaralho, [20, 21, 22, 23])
    elif 20 <= cartaVirada <= 23:
        spritesBaralho = inverterPosCartas(spritesBaralho, [0, 1, 2, 3])
        cartaVirada -= 4
    return cartaVirada, baralho, spritesBaralho


# Distribui as cartas Vira a manilha.
def distribuirCartas(distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho):

    if distribuir_cartas and animacaoCarta[1] < 9:
        screen.blit(fundoCarta, (animacaoCarta[0], 290))
        animacaoCarta[0] += 10

        if animacaoCarta[0] > 300:
            animacaoCarta[0] = 192
            animacaoCarta[1] += 1
        if animacaoCarta[0] < 100:
            animacaoCarta[0] = 192
            animacaoCarta[1] += 1
        if animacaoCarta[1] >= 1:
            screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][0])
        if animacaoCarta[1] >= 2:
            screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][1])
        if animacaoCarta[1] >= 3:
            screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][2])
        if animacaoCarta[1] >= 4:
            screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][0])
        if animacaoCarta[1] >= 5:
            screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][1])
        if animacaoCarta[1] >= 6:
            screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][2])
            animacaoCarta[0] -= 20
        if animacaoCarta[1] >= 7:
            screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][0])
        if animacaoCarta[1] >= 8:
            screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][1])
        if animacaoCarta[1] >= 9:
            screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][2])
            distribuir_cartas = False
            cartasComJogador, baralho = entregarCartas(baralho)
            cartaVirada, baralho, spritesBaralho = virarCarta(baralho, spritesBaralho)
            print('\n\n', cartasComJogador)

    return distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho


def atribuirPontos(rodada, pontosJogador, vencedor):
    if rodada == 1:
        pontosJogador[vencedor] += 3
    elif rodada == 2:
        pontosJogador[vencedor] += 2
    else:
        pontosJogador[vencedor] += 1
    if pontosJogador[vencedor] == 12:
        print('Jogador {} Venceu.'.format(vencedor))
        main()
    elif pontosJogador[vencedor] > 12:
        print('Jogador {} Zerou.'.format(vencedor))
        pontosJogador[0] = 0
    return pontosJogador


# Verifica quem jogou a carta com o maior valor.
def verificarVencedorRodada(cartasJogadas, rodada, pontosJogador):
    forcaCarta = [1, 1, 1, 1,
                  2, 2, 2, 2,
                  3, 3, 3, 3,
                  4, 4, 4, 4,
                  5, 5, 5, 5,
                  6, 6, 6, 6]

    if forcaCarta[cartasJogadas[0]] != 6 or forcaCarta[cartasJogadas[1]] != 6 or forcaCarta[cartasJogadas[2] != 6]:
        if cartasJogadas[0] > cartasJogadas[1] and cartasJogadas[0] > cartasJogadas[2]:
            if forcaCarta[cartasJogadas[0]] != forcaCarta[cartasJogadas[1]] and forcaCarta[cartasJogadas[0]] != forcaCarta[cartasJogadas[2]]:
                pontosJogador = atribuirPontos(rodada, pontosJogador, 0)
            else:
                print("Empatou")
        elif cartasJogadas[1] > cartasJogadas[0] and cartasJogadas[1] > cartasJogadas[2]:
            if forcaCarta[cartasJogadas[1]] != forcaCarta[cartasJogadas[0]] and forcaCarta[cartasJogadas[1]] != forcaCarta[cartasJogadas[2]]:
                pontosJogador = atribuirPontos(rodada, pontosJogador, 1)
            else:
                print("Empatou")
        elif cartasJogadas[2] > cartasJogadas[0] and cartasJogadas[2] > cartasJogadas[1]:
            if forcaCarta[cartasJogadas[2]] != forcaCarta[cartasJogadas[0]] and forcaCarta[cartasJogadas[2]] != forcaCarta[cartasJogadas[1]]:
                pontosJogador = atribuirPontos(rodada, pontosJogador, 2)
            else:
                print("Empatou")
    else:
        if cartasJogadas[0] > cartasJogadas[1] and cartasJogadas[0] > cartasJogadas[2]:
            pontosJogador = atribuirPontos(rodada, pontosJogador, 0)
        elif cartasJogadas[1] > cartasJogadas[0] and cartasJogadas[1] > cartasJogadas[2]:
            pontosJogador = atribuirPontos(rodada, pontosJogador, 1)
        else:
            pontosJogador = atribuirPontos(rodada, pontosJogador, 2)

    return pontosJogador
# /Verifica quem jogou a carta com o maior valor.


def jogar(idioma, nome, baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, distribuir_cartas, animacaoCarta, spritesBaralho, avatarJogador, tempoExibicaoRodada):

    if pygame.mixer.music.get_busy():
        pass
    else:
        pygame.mixer.music.play()

    font = pygame.font.SysFont('Cooper Black', 45)
    font2 = pygame.font.SysFont('Cooper Black', 35)
    mouse = pygame.mouse.get_pos()
    screen.blit(backgroundJogo, (0, 0))

    if distribuir_cartas:
        # Exibe o placar e a rodada.
        for i in range(3):
            screen.blit(fundoAvatarBg, jogoDic['posBgFundoAvatar'][i])
        # Desenha os Avatar
        screen.blit(pygame.transform.flip(spriteSheetAvatar[avatarJogador[0]], -1, 0), jogoDic['posAvatar'][0])
        screen.blit(pygame.transform.flip(spriteSheetAvatar[avatarJogador[1]], -1, 0), jogoDic['posAvatar'][1])
        screen.blit(spriteSheetAvatar[avatarJogador[2]], jogoDic['posAvatar'][2])
        # /Desenha os Avatar

        screen.blit(font.render(str(pontosJogador[0]), 1, resources.PRETO), jogoDic['posPontoJogador1'])
        screen.blit(font.render(str(pontosJogador[1]), 1, resources.PRETO), jogoDic['posPontoJogador2'])
        screen.blit(font.render(str(pontosJogador[2]), 1, resources.PRETO), jogoDic['posPontoJogador3'])
        screen.blit(font2.render(str(nome), 1, resources.PRETO), jogoDic['posTextoNomeJogador1'])
        screen.blit(font.render(idioma['embaralhar'], 1, resources.PRETO), (jogoDic['posTextoRodada'][0] - 40, jogoDic['posTextoRodada'][1]))

        # /Exibe o placar e a rodada.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho = distribuirCartas(distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho)
    else:
        # Desenha o retangulo das cartas do player
        retCartas = [None] * 3
        for i in range(3):
            retCartas[i] = pygame.Rect(jogoDic['posCartaPlayer1'][i][0], jogoDic['posCartaPlayer1'][i][1],
                                       spritesBaralho[0].get_width(), spritesBaralho[0].get_height())
        # /Desenha o retangulo das cartas do player
        # Animação das Cartas ------------------------------------------------------------------------------------------------------------------------------------------
        for i in range(3):
            if cartasComJogador[0][i] is not None:
                if retCartas[i].collidepoint(mouse[0], mouse[1]):
                    screen.blit(spritesBaralho[cartasComJogador[0][i]], (jogoDic['posCartaPlayer1'][i][0], jogoDic['posCartaPlayer1'][i][1] - 15))
                else:
                    screen.blit(spritesBaralho[cartasComJogador[0][i]], jogoDic['posCartaPlayer1'][i])
        # /Animação das Cartas ------------------------------------------------------------------------------------------------------------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turno == 0:
                    if retCartas[0].collidepoint(mouse[0], mouse[1]) and cartasComJogador[0][0] is not None:
                        cartasJogadas.append(cartasComJogador[0][0])
                        cartasComJogador[0][0] = None
                        turno += 1
                    elif retCartas[1].collidepoint(mouse[0], mouse[1]) and cartasComJogador[0][1] is not None:
                        cartasJogadas.append(cartasComJogador[0][1])
                        cartasComJogador[0][1] = None
                        turno += 1
                    elif retCartas[2].collidepoint(mouse[0], mouse[1]) and cartasComJogador[0][2] is not None:
                        cartasJogadas.append(cartasComJogador[0][2])
                        cartasComJogador[0][2] = None
                        turno += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #return 'jogando', baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador
                    main()

        screen.blit(spritesBaralho[cartaVirada], jogoDic['posCartaVirada'])

        # # Blit na mao do player 2 - Mostra
        # for i in range(3):
        #     if cartasComJogador[1][i] is not None:
        #         screen.blit(pygame.transform.rotate(spritesBaralho[cartasComJogador[1][i]], 90), jogoDic['posCartaPlayer2'][i])
        #
        # # Blit na mao do player 3
        # for i in range(3):
        #     if cartasComJogador[2][i] is not None:
        #         screen.blit(pygame.transform.rotate(spritesBaralho[cartasComJogador[2][i]], -90), jogoDic['posCartaPlayer3'][i])

        # Blit na mao do player 2 - Esconde
        for i in range(3):
            if cartasComJogador[1][i] is not None:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][i])

        # Blit na mao do player 3
        for i in range(3):
            if cartasComJogador[2][i] is not None:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer3'][i])

        # Desenha as cartas jogadas na mesa -----------------------------------------------------
        for i in range(len(cartasJogadas)):
            screen.blit(spritesBaralho[cartasJogadas[i]], jogoDic['posJogada'][i])
        # /Desenha as cartas jogadas na mesa -----------------------------------------------------

        # Desenha o Placar
        for i in range(3):
            screen.blit(fundoAvatarBg, jogoDic['posBgFundoAvatar'][i])

        screen.blit(pygame.transform.flip(spriteSheetAvatar[avatarJogador[0]], -1, 0), jogoDic['posAvatar'][0])
        screen.blit(pygame.transform.flip(spriteSheetAvatar[avatarJogador[1]], -1, 0), jogoDic['posAvatar'][1])
        screen.blit(spriteSheetAvatar[avatarJogador[2]], jogoDic['posAvatar'][2])

        screen.blit(font.render(str(pontosJogador[0]), 1, resources.PRETO), jogoDic['posPontoJogador1'])
        screen.blit(font.render(str(pontosJogador[1]), 1, resources.PRETO), jogoDic['posPontoJogador2'])
        screen.blit(font.render(str(pontosJogador[2]), 1, resources.PRETO), jogoDic['posPontoJogador3'])
        screen.blit(font2.render(str(nome), 1, resources.PRETO), jogoDic['posTextoNomeJogador1'])
        screen.blit(font.render(idioma['rodada'] + ' ' + str(rodada), 1, resources.PRETO), jogoDic['posTextoRodada'])
        # /Desenha o Placar

    screen.blit(baralhoImg, jogoDic['posBralho'])

    # Inteligencia Artificial TEMP
    if turno == 1:
        while True:
            aleatorio = random.randint(0, 2)
            if cartasComJogador[1][aleatorio] is not None:
                break
        cartasJogadas.append(cartasComJogador[1][aleatorio])
        cartasComJogador[1][aleatorio] = None
        turno += 1

    if turno == 2:
        while True:
            aleatorio = random.randint(0, 2)
            if cartasComJogador[2][aleatorio] is not None:
                break
        cartasJogadas.append(cartasComJogador[2][aleatorio])
        cartasComJogador[2][aleatorio] = None
        turno = -1
    # /Inteligencia Artificial

    # Tempo de exibição da rodada

    if turno == -1:
        global cronometro1
        cronometro1 += 1
        if cronometro1 == tempoExibicaoRodada:
            print('Cartas jogadas', cartasJogadas)
            print('\n\n', cartasComJogador)
            pontosJogador = verificarVencedorRodada(cartasJogadas, rodada, pontosJogador)
            cartasJogadas.clear()
            turno = 0
            rodada += 1
            cronometro1 = 0
        # Reset
        if rodada > 3:
            baralho = [0, 1, 2, 3,
                       4, 5, 6, 7,
                       8, 9, 10, 11,
                       12, 13, 14, 15,
                       16, 17, 18, 19,
                       20, 21, 22, 23]
            distribuir_cartas = True
            animacaoCarta[1] = 0
            spritesBaralho.clear()
            spritesBaralho = resources.spritesBaralho()
            rodada = 1
        # /Reset
    # /Tempo de exibição da rodada

    return 'jogando', baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador







def main():
    baralho = [0, 1, 2, 3,
               4, 5, 6, 7,
               8, 9, 10, 11,
               12, 13, 14, 15,
               16, 17, 18, 19,
               20, 21, 22, 23]

    pontosJogador = [0] * 3
    cartasComJogador = [[None, None, None], [None, None, None], [None, None, None]]
    cartasJogadas = []
    distribuir_cartas = True
    turno = 0
    rodada = 1
    tempoExibicaoRodada = 85
    cartaVirada = None
    animacaoCarta = [192, 0]
    spritesBaralho = resources.spritesBaralho()
    apresentacao = 1
    avatarJogador = [0] * 3
    avatarJogador[0] = 0
    avatarJogador[1] = 1
    avatarJogador[2] = 3

    pygame.init()
    pygame.font.init()

    estado = 'abertura'
    nome = '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'
    idioma = textos.dicPortugues
    idiomaTexto = 'Português'
    while True:
        if estado == 'abertura':
            estado, apresentacao = abertura(apresentacao)
        elif estado == 'escreverNome':
            estado, nome = enterNomePlayer(idioma, nome)
        elif estado == 'menu':
            estado, avatarJogador = menu(idioma, nome, avatarJogador)
        elif estado == 'configuracao':
            estado, idiomaTexto, idioma = configuracao(idioma, idiomaTexto)
        elif estado == 'avatar':
            estado, avatarJogador = avatar(idioma, avatarJogador)
        elif estado == 'jogando':
            estado, baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador = \
                jogar(idioma, nome, baralho, turno, rodada,  pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, distribuir_cartas, animacaoCarta, spritesBaralho, avatarJogador, tempoExibicaoRodada)

        clock.tick(config.FPS)
        pygame.display.update()


main()
