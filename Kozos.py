class Kozos:
    def __init__ (self):
        self.felulet = None
        self.rect = None
        self.sebesseg = None
        
    def mozoghat(self, irany, falak):
        if irany == 0:
            rectTest = self.rect.move((0, -self.sebesseg))
        elif irany == 1:
            rectTest = self.rect.move((-self.sebesseg, 0))
        elif irany == 2:
            rectTest = self.rect.move((0, self.sebesseg))
        elif irany == 3:
            rectTest = self.rect.move((self.sebesseg, 0))

        for fal in falak:
            if fal.colliderect(rectTest):
                return False
        return True

    def mozog(self, irany):
        if irany == 0:
            self.rect.top -= self.sebesseg
        elif irany == 1:
            self.rect.left -= self.sebesseg
        elif irany == 2:
            self.rect.top += self.sebesseg
        elif irany == 3:
            self.rect.left += self.sebesseg