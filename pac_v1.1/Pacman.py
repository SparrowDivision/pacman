import pygame

class Pacman:
    def __init__(self, b):
        self.pac_ny = pygame.image.load('pac_nyk.png')
        self.pac_cs = pygame.image.load('pac_csk.png')
        self.felulet = self.pac_ny 
        self.rect = pygame.Rect(0, 0, b.EGYSEG + 6, b.EGYSEG + 6)
        self.rect.left = b.EGYSEG * 14 + 12
        self.rect.top = b.EGYSEG * 17 - 6
        self.FEL = self.BAL = self.LE = self.JOBB = False
        self.zaba = 0
        self.irany = -1
        self.kov_irany = -1
        self.sebesseg = 2
        self.pont = 0
        self.elet = 3

    def uj(self, b):
        self.felulet = self.pac_ny
        self.rect.left = b.EGYSEG * 15 - 16
        self.rect.top = b.EGYSEG * 17 - 7
        self.irany = -1
        self.kov_irany = -1
        self.FEL = self.BAL = self.LE = self.JOBB = False

    def melyik(self):
        self.zaba += 1
        if self.zaba == 16:
            self.zaba = 0
            
        if self.irany == 0:
            if self.zaba < 8:
                self.felulet = pygame.transform.rotate(self.pac_ny, 90)
            else:
                self.felulet = pygame.transform.rotate(self.pac_cs, 90)
        elif self.irany == 1:
            if self.zaba < 8:
                self.felulet = pygame.transform.flip(self.pac_ny, True, False)
            else:
                self.felulet = pygame.transform.flip(self.pac_cs, True, False)
        elif self.irany == 2:
            if self.zaba < 8:
                self.felulet = pygame.transform.rotate(self.pac_ny, -90)
            else:
                self.felulet = pygame.transform.rotate(self.pac_cs, -90)
        elif self.irany == 3:
            if self.zaba < 8:
                self.felulet = self.pac_ny
            else:
                self.felulet = self.pac_cs
    
    def iranyit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                self.elozo_irany = self.irany
                if event.key == pygame.K_UP:
                    self.kov_irany = 0                  
                elif event.key == pygame.K_LEFT:
                    self.kov_irany = 1              
                elif event.key == pygame.K_DOWN:
                    self.kov_irany = 2       
                elif event.key == pygame.K_RIGHT:
                    self.kov_irany = 3            
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True

    def mozog(self, palya):
        if self.mozoghat(self.kov_irany, palya):
            self.irany = self.kov_irany
        if self.irany == 0:
            self.FEL = True
            self.BAL = self.LE = self.JOBB = False
            self.irany = 0
        elif self.irany == 1:
            self.BAL = True
            self.FEL = self.LE = self.JOBB = False
            self.irany = 1
        elif self.irany == 2:
            self.LE = True
            self.FEL = self.BAL = self.JOBB = False
            self.irany = 2
        elif self.irany == 3:
            self.JOBB = True
            self.FEL = self.BAL = self.LE = False
            self.irany = 3 
            
        if self.FEL and self.mozoghat(0, palya):
            self.lepes(0)                     
        elif self.BAL and self.mozoghat(1, palya):
            self.lepes(1) 
        elif self.LE and self.mozoghat(2, palya):
            self.lepes(2)    
        elif self.JOBB and self.mozoghat(3, palya):
            self.lepes(3)
                      
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
            if fal.colliderect(rectTest):
                return False
        return True
    
    def lepes(self, irany):     
        if irany == 0:
            self.rect.top -= self.sebesseg
        elif irany == 1:
            self.rect.left -= self.sebesseg
        elif irany == 2:
            self.rect.top += self.sebesseg
        elif irany == 3:
            self.rect.left += self.sebesseg

    def teleport(self, b):
        if self.rect.colliderect(pygame.Rect((-b.EGYSEG/2, b.EGYSEG * 15), (b.EGYSEG, b.EGYSEG))):
            self.rect.left += b.EGYSEG * 26
        if self.rect.colliderect(pygame.Rect((b.EGYSEG * 29, b.EGYSEG * 15), (b.EGYSEG, b.EGYSEG))):
            self.rect.left -= b.EGYSEG * 26

    def pont_kiir(self, b):
        return pygame.font.SysFont("Arial Black",32).render(str(self.pont) + " pont", True, b.YELLOW)

    def elet_kiir(self, b, jAblak):
        x = b.MERET-120
        for i in range(self.elet):
            jAblak.blit(self.pac_ny, (x, 12))
            x += 30
