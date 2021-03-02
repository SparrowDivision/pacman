import pygame
import random
from A_star import a_star_search, reconstruct_path
from Palya import Palya


class Kozos:
    def __init__ (self):
        self.gyava = [pygame.image.load("gyava_sk.png"), pygame.image.load("gyava_vk.png")]
        self.rect = None
        self.sebesseg = None
        self.eheto_ido = 0
        
    def megehet(self):
        self.eheto = True
        self.eheto_ido  = 600
        self.felulet = Kozos().gyava[0]

    def eheto_e(self):
        self.eheto_ido  -= 1
        if self.eheto_ido  < 200:
            if self.eheto_ido  % 20 < 5:
                self.felulet = Kozos().gyava[0]
            else:
                self.felulet = Kozos().gyava[1]
        if self.eheto_ido  <= 0:
            self.eheto = False
            self.eheto_ido  = 0
            self.felulet = self.normal
            
    def mozoghat(self, irany, falak):
        if irany == 0:
            rectTest = self.rect.move((0, -self.sebesseg))
        elif irany == 1:
            rectTest = self.rect.move((-self.sebesseg, 0))
        elif irany == 2:
            rectTest = self.rect.move((0, self.sebesseg))
        elif irany == 3:
            rectTest = self.rect.move((self.sebesseg, 0))
        else:
            return False

        for fal in falak:
            if falak[197].colliderect(rectTest) or falak[198].colliderect(rectTest) or falak[196].colliderect(rectTest) or falak[199].colliderect(rectTest):
                return True
            elif fal.colliderect(rectTest):
                return False
        return True

    def lep(self, irany):
        if irany == 0:
            self.rect.top -= self.sebesseg
        elif irany == 1:
            self.rect.left -= self.sebesseg
        elif irany == 2:
            self.rect.top += self.sebesseg
        elif irany == 3:
            self.rect.left += self.sebesseg
            
    def lepesek(self):
        lepesek = [-1, -1, -1, -1]
        
        if abs(self.x_tav) > abs(self.y_tav):
            if self.y_tav >= 0:
                lepes = 2
                lepesek[1] = 2
                lepesek[2] = 0
            elif self.y_tav < 0:
                lepesek[1] = 0
                lepesek[2] = 2
            if self.x_tav >= 0:
                lepesek[0] = 3
                lepesek[3] = 1
            elif self.x_tav < 0:
                lepesek[0] = 1
                lepesek[3] = 3
                        
        elif abs(self.y_tav) >= abs(self.x_tav):
            if self.x_tav >= 0:
                lepesek[1] = 3
                lepesek[2] = 1
            elif self.x_tav < 0:
                lepesek[1] = 1
                lepesek[2] = 3
            if self.y_tav >= 0:
                lepesek[0] = 2
                lepesek[3] = 0
            elif self.y_tav < 0:
                lepesek[0] = 0
                lepesek[3] = 2
                
        return lepesek
    
    def ut(self, pacman, sz_x, sz_y, b):
        p = Palya()
        pac_y = pacman.left//b.EGYSEG + 1
        pac_x = pacman.top//b.EGYSEG + 1
             
        tol = (sz_y, sz_x)
        ig = (pac_y, pac_x)
        vissza_vezet = a_star_search(p.diagram4, tol, ig)
        cel = reconstruct_path(vissza_vezet, tol, ig)
        
        return(((cel[1])*b.EGYSEG-7) - self.rect.top, ((cel[0])*b.EGYSEG-2) - self.rect.left)
    
    def mehet_e(self):
        if self.mehet > 0:
            self.mehet -= 1
            return False
        return True
    
    def teleport(self, b):
        if self.rect.colliderect(pygame.Rect((-b.EGYSEG/2, b.EGYSEG * 15), (b.EGYSEG, b.EGYSEG))):
            self.rect.left += b.EGYSEG * 26
        if self.rect.colliderect(pygame.Rect((b.EGYSEG * 29, b.EGYSEG * 15), (b.EGYSEG, b.EGYSEG))):
            self.rect.left -= b.EGYSEG * 26
            
class Inky(Kozos):
    def __init__ (self, b):
        self.normal = pygame.image.load("inky_k.png")
        self.nev = "Inky"
        self.felulet = self.normal
        self.rect = pygame.Rect(0, 0, b.EGYSEG + 6, b.EGYSEG + 6)
        self.rect.left = b.MERET/2 - b.EGYSEG/2
        self.rect.top = b.EGYSEG * 15 - 8
        self.otthon = pygame.Rect(b.EGYSEG * 1, b.EGYSEG * 2, 7, 7)
        self.irany = -1
        self.sebesseg = 1
        self.eheto = False
        self.mehet = 6*b.FPS
        self.x_tav = 0
        self.y_tav = 0
        self.cel = self.rect
        self.cel_y = 15
        self.cel_x = 15
        self.szamlalo = 24

    def mozog(self, palya, csomopontok, pacman, b):
        if not Kozos.mehet_e(self):
            return
        
        tav = abs(pacman.rect.left - self.rect.left) + abs(pacman.rect.top - self.rect.top)
        
        if self.szamlalo == 24:
            sz_y = self.rect.left//b.EGYSEG + 1
            sz_x = self.rect.top//b.EGYSEG + 1
            if self.eheto:
                self.cel = self.otthon
            elif tav <= b.EGYSEG*6:
                self.cel = pacman.rect
            elif self.rect.colliderect(self.cel) or self.rect.colliderect(self.otthon):
                while self.rect.colliderect(self.cel):
                    csomo = csomopontok[random.randint(0, len(csomopontok)-1)]
                    csomo.left -= b.EGYSEG
                    csomo.top -= b.EGYSEG
                    self.cel = csomo
            elif tav > b.EGYSEG*10 and self.cel == pacman.rect:
                csomo = csomopontok[random.randint(0, len(csomopontok)-1)]
                csomo.left -= b.EGYSEG
                csomo.top -= b.EGYSEG
                self.cel = csomo
                
            # a számítás ami elhelyzné a a súlyozott diagramm4-ben nem pontos így néha, falat kap célként #
            # még fejlesztés alatt #
            try:    
                irany = Kozos.ut(self, self.cel, sz_x, sz_y, b)
            except IndexError:
                self.cel = pacman.rect
                irany = Kozos.ut(self, self.cel, sz_x, sz_y, b)
            except KeyError:
                self.cel = pacman.rect
                irany = Kozos.ut(self, self.cel, sz_x, sz_y, b)
            
            self.x_tav = irany[1]
            self.y_tav = irany[0]
            self.szamlalo = 0
        self.szamlalo += self.sebesseg

        lepesek = Kozos.lepesek(self)
        
        for i in lepesek:
            if i == -1 or (not self.mozoghat(i, palya)):
                if len(lepesek) > 0:
                    lepesek.pop(lepesek.index(i))
        
        self.irany = lepesek[0]
        
        if self.mozoghat(self.irany, palya):
            Kozos.lep(self, self.irany)

class Clyde(Kozos):
    def __init__ (self, b):
        self.nev = "Clyde"
        self.normal = pygame.image.load("clyde_k.png")
        self.felulet = self.normal
        self.rect = pygame.Rect(0, 0, 28, 28)
        self.rect.left = b.MERET/2 + b.EGYSEG
        self.rect.top = b.EGYSEG * 15 - 8
        self.otthon = pygame.Rect(b.EGYSEG * 2 - 7, b.EGYSEG * 27-3, 7, 7)
        self.menekul = False
        self.irany = -1
        self.sebesseg = 1
        self.eheto = False
        self.mehet = 4*b.FPS
        self.x_tav = 0
        self.y_tav = 0
        self.cel_y = 13
        self.cel_x = 15
        self.szamlalo = 24


    def mozog(self, palya, cs, pacman, b):
        if not Kozos.mehet_e(self):
            return
                           
        if self.szamlalo == 24:
            sz_y = self.rect.left//b.EGYSEG + 1
            sz_x = self.rect.top//b.EGYSEG + 1 
            if not self.eheto:
                cel = Kozos.ut(self, pacman.rect, sz_x, sz_y, b)
            else:
                cel = Kozos.ut(self, self.otthon, sz_x, sz_y, b)
            self.y_tav = cel[0]
            self.x_tav = cel[1]
            self.szamlalo = 0
        self.szamlalo += self.sebesseg
 
        lepesek = Kozos.lepesek(self)
        for i in lepesek:
            if i == -1 or (not self.mozoghat(i, palya)):
                if len(lepesek) > 0:
                    lepesek.pop(lepesek.index(i))
        
        self.irany = lepesek[0]
        
        if self.mozoghat(self.irany, palya):
            Kozos.lep(self, self.irany)
            
        """if not Kozos.mehet_e(self):
            return
        
        if self.szamlalo == 24:
            pac_szell_x = pacman.rect.left - self.rect.left
            pac_szell_y = pacman.rect.top - self.rect.top
        
        if self.rect.colliderect(self.otthon):
            self.sebesseg = 1
            self.menekul = False
        
        if (abs(pac_szell_x) + abs(pac_szell_y)) > (b.EGYSEG*3) and not self.menekul:
            self.cel = pacman.rect
        else:
            self.sebesseg = 2
            self.menekul = True
            self.cel = self.otthon
        try:    
            cel = Kozos.ut(self, self.cel, b)
        except IndexError:
            cel = Kozos.ut(self, pacman.rect, b)
        y_tav = cel[0]
        x_tav = cel[1]
        
        for i in lepesek:
            if i == -1 or (not self.mozoghat(i, palya)):
                if len(lepesek) > 0:
                    lepesek.pop(lepesek.index(i))
        
        self.irany = lepesek[0]
        
        if self.mozoghat(self.irany, palya):
            Kozos.lep(self, self.irany)"""
            

class Pinky(Kozos):
    def __init__ (self, b):
        self.normal = pygame.image.load("pinky_k.png")
        self.nev = "Pinky"
        self.felulet = self.normal
        self.rect = pygame.Rect(0, 0, 28, 28)
        self.rect.left = b.MERET/2 - 2*b.EGYSEG
        self.rect.top = b.EGYSEG * 15 - 8
        self.otthon = pygame.Rect(b.EGYSEG * 26, b.EGYSEG * 2, 7, 7)
        self.cel = 0
        self.irany = -1
        self.sebesseg = 1
        self.eheto = False
        self.mehet = 2*b.FPS
        self.x_tav = 0
        self.y_tav = 0
        self.cel_y = 13
        self.cel_x = 15
        self.szamlalo = 24

    def mozog(self, palya, cs, pacman, b):
        if not Kozos.mehet_e(self):
            return
                            
        if self.szamlalo == 24:
            sz_y = self.rect.left//b.EGYSEG + 1
            sz_x = self.rect.top//b.EGYSEG + 1
            if not self.eheto:
                cel = Kozos.ut(self, pacman.rect, sz_x, sz_y, b)
            else:
                cel = Kozos.ut(self, self.otthon, sz_x, sz_y, b)
            self.y_tav = cel[0]
            self.x_tav = cel[1]
            self.szamlalo = 0
        self.szamlalo += self.sebesseg
 
        lepesek = Kozos.lepesek(self)
        for i in lepesek:
            if i == -1 or (not self.mozoghat(i, palya)):
                if len(lepesek) > 0:
                    lepesek.pop(lepesek.index(i))
        
        self.irany = lepesek[0]
        
        if self.mozoghat(self.irany, palya):
            Kozos.lep(self, self.irany)

class Blinky(Kozos): 
    def __init__ (self, b):
        self.normal = pygame.image.load("blinky_k.png")
        self.nev = "Blinky"
        self.felulet = self.normal
        self.rect = pygame.Rect(0, 0, 28, 28)
        self.rect.left = b.MERET/2 - b.EGYSEG/2
        self.rect.top = b.EGYSEG * 13 -5
        self.otthon = pygame.Rect(b.EGYSEG * 26, b.EGYSEG * 26, 7, 7)
        self.irany = -1
        self.sebesseg = 1
        self.eheto = False
        self.mehet = b.FPS
        self.x_tav = 0
        self.y_tav = 0
        self.cel_y = 13
        self.cel_x = 15
        self.szamlalo = 24
        
    def cruise_elroy(self, k):
        if len(k) < 40:
            self.sebesseg = 2


    def mozog(self, palya, cs, pacman, b):
        if not Kozos.mehet_e(self):
            return
                           
        if self.szamlalo == 24:
            sz_y = self.rect.left//b.EGYSEG + 1
            sz_x = self.rect.top//b.EGYSEG + 1 
            if not self.eheto:
                cel = Kozos.ut(self, pacman.rect, sz_x, sz_y, b)
            else:
                cel = Kozos.ut(self, self.otthon, sz_x, sz_y, b)
            self.y_tav = cel[0]
            self.x_tav = cel[1]
            self.szamlalo = 0
        self.szamlalo += self.sebesseg
 
        lepesek = Kozos.lepesek(self)
        for i in lepesek:
            if i == -1 or (not self.mozoghat(i, palya)):
                if len(lepesek) > 0:
                    lepesek.pop(lepesek.index(i))
        
        self.irany = lepesek[0]
        
        if self.mozoghat(self.irany, palya):
            Kozos.lep(self, self.irany)

