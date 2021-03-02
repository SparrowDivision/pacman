import pygame
class Beallitasok:
    def __init__(self):
        self.EGYSEG = 24     
        self.M = 30
        self.MERET = self.M * self.EGYSEG
        self.ABLAK = (self.MERET, self.MERET)
        self.FPS = 60
        self.BLACK = (0, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.PEACH = (255,218,185)
        self.WHITE = (255, 255, 255)
        self.ORANGE = (255, 215, 0)
        
    def kezdo(self):
        pygame.init()
        jAblak = pygame.display.set_mode(self.ABLAK)
        pygame.display.set_caption("Pacman")
        pygame.display.set_icon(pygame.image.load('logo.png'))
        return jAblak
