import pygame
from Beallitasok import Beallitasok

class Kaja:
    def __init__(self):
        b = Beallitasok()
        self.k = [(b.EGYSEG/5, b.EGYSEG/5),(b.EGYSEG/3, b.EGYSEG/3)]
        
    def kiskaja_be(self):
        b = Beallitasok()
        k = [(14/2, 14/2),(20/2, 20/2)]
        kaja = []
        x = -0.5
        y = 0.3
        quit = False
        with open("palya.txt") as f:
            while not quit:
                c = f.read(1)
                if c == "o" or c == "D":
                    kaja.append(pygame.Rect((x*b.EGYSEG, y*b.EGYSEG),(self.k[0])))
                elif c == "\n":
                    x = -0.5
                    y += 1
                if not c:
                    quit = True
                x += 1
        return kaja

    def nagykaja_be(self):
        b = Beallitasok()
        kaja = []
        x = -0.5
        y = 0.4
        quit = False
        with open("palya.txt") as f:
            while not quit:
                c = f.read(1)
                if c == "0":
                    kaja.append(pygame.Rect((x*b.EGYSEG, y*b.EGYSEG),(self.k[1])))
                elif c == "\n":
                    x = -0.5
                    y += 1
                if not c:
                    quit = True
                x += 1
        return kaja
    
    def kaja_ki(self, kiskaja, nagykaja, ablak):
        b = Beallitasok()
        for k in kiskaja:
            pygame.gfxdraw.filled_circle(ablak, k[0], k[1], b.EGYSEG//8, b.ORANGE)
        for k in nagykaja:
            pygame.gfxdraw.filled_circle(ablak, k[0], k[1], b.EGYSEG//3, b.ORANGE)
    
    def kkaja_eves(self, kiskaja, pacman):
        i = 0
        for k in kiskaja:
            if k.colliderect(pacman.rect):
                pacman.pont += 2
                kiskaja.pop(i)
            i += 1
        return kiskaja
    
    def nkaja_eves(self, nagykaja, pacman, szellemek):
        i = 0
        for k in nagykaja:
            if k.colliderect(pacman.rect):
                for sz in szellemek:
                    sz.megehet()
                pacman.pont += 20
                nagykaja.pop(i)        
            i += 1
        return nagykaja