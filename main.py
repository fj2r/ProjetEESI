# Projet EESI avec pygame
# Version : 0.1
# By Fj2r
import time
from os import *
import pygame as pg
from math import *


# fonctions de déplacement du perso principal
def deplacementPerso(keyb, x, y, direction, index, step):
    if keyb[pg.K_LEFT]:
        direction = pg.K_LEFT
        index = (index + 1) % 4
        x = x - keyb[pg.K_LEFT] * step

    if keyb[pg.K_RIGHT]:
        direction = pg.K_RIGHT
        index = (index + 1) % 4
        x = x + keyb[pg.K_RIGHT] * step
    if keyb[pg.K_DOWN]:
        direction = pg.K_DOWN
        index = (index + 1) % 4
        y = y + keyb[pg.K_DOWN] * step
    if keyb[pg.K_UP]:
        direction = pg.K_UP
        index = (index + 1) % 4
        y = y - keyb[pg.K_UP] * step
    return (x, y, direction, index, step)


# fonction principale du jeu
def main():
    # init de pygame
    pg.init()
    # paramètres de départ

    jeu = True
    etat = 0
    fps = pg.time.Clock()
    fps.tick(60)
    # paramètres d'initialisation de la fenêtre principale

    largeurEcran = 928
    hauteurEcran = 570
    pg.display.set_caption('Projet EESI')

    fond = 'img/projet_pygame_fond.jpg'
    remplissage = (220, 220, 220)
    screen = pg.display.set_mode((largeurEcran, hauteurEcran))
    screen.fill(remplissage)
    background = pg.image.load(fond).convert()

    # images du jeu
    kirby = pg.image.load('img/sprite.png').convert()
    kirby.set_colorkey((0, 0, 0))
    xpos = 50
    ypos = 50
    step_x = 1
    step_y = 1
    # Les spriteSheets
    dragon = pg.image.load('img/DragonRouge.png').convert()
    dragonSprite = {
        pg.K_DOWN: [dragon.subsurface(x, 0, 96, 96) for x in range(0, 384, 96)],
        pg.K_LEFT: [dragon.subsurface(x, 96, 96, 96) for x in range(0, 384, 96)],
        pg.K_RIGHT: [dragon.subsurface(x, 192, 96, 96) for x in range(0, 384, 96)],
        pg.K_UP: [dragon.subsurface(x, 288, 96, 96) for x in range(0, 384, 96)]
    }
    # initialisation des sprites
    x_sprite = 202
    y_sprite = 202
    direction = pg.K_DOWN
    index_sprite = 0
    step = 10

    while jeu:
        keypressed = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                jeu = False
                pg.quit()
                sys.exit()

        pg.display.update()

        # splash screen
        if etat == 0:
            screen.fill((255, 255, 255))
            police = pg.font.SysFont('comicsansms', 42)
            splashTexte = police.render('Appuyez sur la touche ENTREE !', True, (255, 0, 0), (0, 5, 255))
            screen.blit(splashTexte, (20, 20))
            if keypressed[pg.K_RETURN]:
                etat = 1
        # fenetre de jeu principale
        if etat == 1:
            if xpos > largeurEcran - 380 or xpos < 0:
                step_x = -step_x
            if ypos > hauteurEcran - 360 or ypos < 0:
                step_y = -step_y
            xpos += step_x
            ypos += step_y
            screen.blit(background, (0, 0))
            # screen.blit(kirby, (xpos, ypos))
            etatSprite = deplacementPerso(keypressed, x_sprite, y_sprite, direction, index_sprite, step)

            x_sprite = etatSprite[0]
            y_sprite = etatSprite[1]
            direction = etatSprite[2]
            index_sprite = etatSprite[3]
            screen.blit(dragonSprite[etatSprite[2]][etatSprite[3]], (etatSprite[0], etatSprite[1]))

            if keypressed[pg.K_BACKSPACE]:
                etat = 0
        pg.display.flip()
        pg.time.wait(25)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
