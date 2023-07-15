# Projet EESI avec pygame
# Version : 0.1
# By Fj2r
import pygame as pg
from Personnage.Perso import Perso


# fonctions de déplacement du perso principal
def deplacementPerso(keyb, x, y, direction, index, modulo, step):
    if keyb[pg.K_LEFT]:
        direction = pg.K_LEFT
        index = (index + 1) % modulo
        x = x - keyb[pg.K_LEFT] * step

    if keyb[pg.K_RIGHT]:
        direction = pg.K_RIGHT
        index = (index + 1) % modulo
        x = x + keyb[pg.K_RIGHT] * step
    if keyb[pg.K_DOWN]:
        direction = pg.K_DOWN
        index = (index + 1) % modulo
        y = y + keyb[pg.K_DOWN] * step
    if keyb[pg.K_UP]:
        direction = pg.K_UP
        index = (index + 1) % modulo
        y = y - keyb[pg.K_UP] * step
    return (x, y, direction, index, step)


# fonction principale du jeu
def main():
    # init de pygame
    pg.init()
    # paramètres de départ

    jeu = True
    etape = 0
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

    # images du jeu : Kirby
    kirby = pg.image.load('img/kirby.png').convert()
    kirby.set_colorkey((255, 0, 255))
    obj = Perso(kirby,50, 50, 1, 1)
    xpos = 0
    ypos = 0
    step_x = 1
    step_y = 1

    # Les spriteSheets du Dragon
    dragon = pg.image.load('img/DragonRouge.png').convert()
    dragonSprite = {
        pg.K_DOWN: [dragon.subsurface(x, 0, 96, 96) for x in range(0, 384, 96)],
        pg.K_LEFT: [dragon.subsurface(x, 96, 96, 96) for x in range(0, 384, 96)],
        pg.K_RIGHT: [dragon.subsurface(x, 192, 96, 96) for x in range(0, 384, 96)],
        pg.K_UP: [dragon.subsurface(x, 288, 96, 96) for x in range(0, 384, 96)]
    }
    # initialisation des sprites du dragon
    x_sprite = (largeurEcran//2)-(96/2)
    y_sprite = (hauteurEcran//2)-(96/2)
    direction = pg.K_DOWN
    index_sprite = 0
    mod = 4
    step = 10

    while jeu:
        keypressed = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                jeu = False
                pg.quit()

        #pg.display.update()

        # splash screen
        if etape == 0:
            screen.fill((255, 255, 255))
            police = pg.font.SysFont('comicsansms', 42)
            splashTexte = police.render('Appuyez sur la touche ENTREE !', True, (255, 0, 0), (0, 5, 255))
            screen.blit(splashTexte, (20, 20))
            if keypressed[pg.K_RETURN]:
                etape = 1
        # fenetre de jeu principale
        if etape == 1:

            screen.blit(background, (0, 0))

            nouvellesPositions = obj.deplacement(xpos, ypos, largeurEcran, hauteurEcran, step_x, step_y)
            #print(nouvellesPositions)

            xpos = nouvellesPositions[0]

            ypos = nouvellesPositions[1]
            step_x = nouvellesPositions[2]
            print(step_x)
            step_y = nouvellesPositions[3]

            screen.blit(kirby, (xpos, ypos))

            etatSprite = deplacementPerso(keypressed, x_sprite, y_sprite, direction, index_sprite, mod, step)

            x_sprite = etatSprite[0]
            y_sprite = etatSprite[1]
            direction = etatSprite[2]
            index_sprite = etatSprite[3]

            screen.blit(dragonSprite[etatSprite[2]][etatSprite[3]], (etatSprite[0], etatSprite[1]))

            if keypressed[pg.K_BACKSPACE]:
                etape = 0
        pg.display.flip()
        pg.time.wait(20)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
