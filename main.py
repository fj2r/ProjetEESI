# Projet EESI avec pygame
# Version : 0.1

import pygame as pg

def heroInit () :
    perso = pg.image.load('img/sprite.png').convert()
    perso.set_colorkey((0, 0, 0))
    return perso

def main() :
    pg.init()
    jeu = True

    largeurEcran = 1280
    hauteurEcran = 600

    screen = pg.display.set_mode((largeurEcran, hauteurEcran))
    fond = pg.image.load('img/background.jpg').convert()

    hero = heroInit()

    xpos = 50
    ypos = 50
    step_x = 1
    step_y = 1

    while jeu:
        if xpos > largeurEcran - 60 or xpos < 0:
            step_x = -step_x
        if ypos > hauteurEcran - 60 or ypos < 0:
            step_y = -step_y
        xpos += step_x
        ypos += step_y
        screen.blit(fond, (0, 0))
        screen.blit(hero, (xpos, ypos))
        print(xpos)
        print(ypos)
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                jeu = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


