import pygame
import spritesheetClass

BRANCO = (255, 255, 255)
PRETO = (13, 13, 13)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

BOTAO = 'imagens/botao.png'
BOTAO2 = 'imagens/botao2.png'
BACKGROUND_JOGO = 'imagens/mesaBG.png'
BACKGROUND_MENU = 'imagens/background_menu.png'
FUNDO_CARTA = 'imagens/fundo.png'
BARALHO = 'imagens/baralho.png'
SPRITESHEET_BARALHO = pygame.image.load('imagens/sprite_baralho.png')
SPRITESHEET_AVATAR = pygame.image.load('imagens/avatar_sprite_sheet.png')
FUNDO_AVATAR = 'imagens/Fundo Avatar.png'
IMAGEM1 = 'imagens/imagem1.jpg'

LOGOK = 'imagens/projetoKlogo.png'
PROJETOK = 'imagens/projetok.jpg'
IMAGEM_CG = 'imagens/cg.jpg'
LEFT = 'imagens/left.png'
RIGHT = 'imagens/right.png'
SPRITESHEET_LOGO = pygame.image.load('imagens/logo_spritesheet.png')
MENU_SHEET = 'imagens/HUD_Menu.png'
AVATAR_MIRROR = 'imagens/avatar_mirror.png'
AVATAR_MENU = 'imagens/avatarSpritesheetMenu.png'

fxCardAnim = 'audio/cardAnim.wav'
gameplayMusic = 'audio/inGame.mp3'

AVATAR_SELECT_MORTE = 'imagens/avatar_SelectPage.png'
AVATAR_SELECT_BUROC = 'imagens/avatar_SelectPage(1).png'
AVATAR_SELECT_HOMEM = 'imagens/avatar_SelectPage(2).png'
AVATAR_SELECT_DIGI = 'imagens/avatar_SelectPage(3).png'
AVATAR_SELECT_PETER = 'imagens/avatar_SelectPage(4).png'
frames = []  # Lista para armazenar as sprites do baralho.
logo = []  # Lista para armazenar as sprites do Logo.
avatar = []

CHARACTER_SHEET = 'imagens/character_sheet.png'


def spritesBaralho():
    x = 0
    for i in range(24):
        frames.append(SPRITESHEET_BARALHO.subsurface(pygame.Rect(x, 0, 50, 75)))
        x += 50

    return frames


def spriteLogo():

    logo = spritesheetClass.Spritesheet('imagens/logo_spritesheet.png', 1, 24)
    # x = 0
    # for i in range(11):
    #     logo.append(SPRITESHEET_LOGO.subsurface(pygame.Rect(x, 0, 480, 220)))
    #     x += 480

    return logo

def spriteMenu():
    hud_menu = spritesheetClass.Spritesheet(MENU_SHEET, 1,10)

    return hud_menu


def spriteCG():
    anim = spritesheetClass.Spritesheet('imagens/anim1.png',1,25)

    return anim

def avatarMenu():
    menuAvatar = spritesheetClass.Spritesheet(AVATAR_MENU,1,5)

    return menuAvatar

def characterSheet():
    characterSheet = spritesheetClass.Spritesheet(CHARACTER_SHEET,1,5)

    return characterSheet

def spriteAvatar():
    x = 0
    for i in range(4):
        avatar.append(SPRITESHEET_AVATAR.subsurface(pygame.Rect(x, 0, 55, 100)))
        x += 55
    return avatar


