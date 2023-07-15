# import pygame as pg
class Perso:

    def __init__(self, surface, xpos, ypos, step_x, step_y):
        self.surface = surface
        self.xpos=xpos
        self.ypos=ypos
        self.step_x=step_x
        self.step_y = step_y

    def deplacement(self, xpos=None, ypos=None, largeurEcran=None, hauteurEcran=None, step_x=None,
                    step_y=None):

        if xpos > largeurEcran - 96 or xpos < 0:
            step_x = -step_x
            print(step_x)
        if ypos > hauteurEcran - 90 or ypos < 0:
            step_y = -step_y
        xpos += step_x
        ypos += step_y
        return (xpos, ypos, step_x, step_y)

