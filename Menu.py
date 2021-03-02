import pygame

class Kepek():
    def __init__(self):
        self.inky = pygame.image.load("inky_k.png")
        self.blinky = pygame.image.load("blinky_k.png")
        self.pinky = pygame.image.load("pinky_k.png")
        self.clyde = pygame.image.load("clyde_k.png")
        self.gyava_v = pygame.image.load("gyava_vk.png")
        self.gyava_s = pygame.image.load("gyava_sk.png")
        self.pac_ny = pygame.image.load("pac_nyk.png")
        self.pac_cs = pygame.image.load("pac_csk.png")

def forma(szoveg, szin, meret = 20, tipus = 'Arial Black'):
    ujforma = pygame.font.SysFont(tipus, meret)
    ujszoveg = ujforma.render(szoveg, True, szin)
 
    return ujszoveg

def fajl_be():
    eredmenyek = []
    with open("eredmenyek.txt", "rt") as f:
        for sor in f:
            sor = sor.rstrip("\n")
            seged = sor.split(" - ")
            eredmenyek.append((int(seged[0]), seged[1]))
    return eredmenyek

def fajl_ki(pont, jAblak, b):
    eredmenyek = fajl_be()
    nev = nev_be(jAblak, b)
    if nev == "":
        nev = "Névtelen"
    eredmenyek.append((pont,nev))
    eredmenyek = sorted(eredmenyek, reverse = True)
    with open("eredmenyek.txt", "wt") as f:
        i = 0
        for i in range(len(eredmenyek)):
            f.write("{} - {}\n".format(eredmenyek[i][0], eredmenyek[i][1]))
            i += 1
            if i == 10:
                break

def nev_ki(jAblak, b):
    eredmenyek = fajl_be()
    quit = False
    i = 3
    jAblak.fill(b.BLACK)
    pont = forma("DICSŐSÉGLISTA", b.YELLOW, 70)
    jAblak.blit(pont, (b.MERET/2 - (pont.get_width()/2), 0))
    for e in eredmenyek:
        nev = forma("{}.  {}".format(i-2, e[1][:16]), b.WHITE, b.EGYSEG+4)
        pont = forma("{} pont".format(e[0]), b.YELLOW, b.EGYSEG+4)
        jAblak.blit(nev, (b.MERET/8, i*(2*b.EGYSEG)))
        jAblak.blit(pont, (7*b.MERET/8 - pont.get_width(), i*(2*b.EGYSEG)))
        i += 1
    while not quit:
        bal_also("Folytatáshoz nyomjon meg egy gombot", b.WHITE, jAblak, b)
        pygame.display.update()
        quit = skip()

            
def jatek_vege(jAblak, b):
    kep = Kepek()
    x = b.MERET/2 - (b.EGYSEG+7)//2
    y = b.MERET/4
    vege = forma("JÁTÉK VÉGE", b.YELLOW, b.EGYSEG*3)
    jAblak.blit(vege, ((b.MERET/2 - (vege.get_width())/2), 0))
    jAblak.blit(kep.pac_ny, (x,y))
    jAblak.blit(kep.blinky, (x+2*b.EGYSEG,y))
    jAblak.blit(kep.inky, (x,y-2*b.EGYSEG))
    jAblak.blit(kep.pinky, (x,y+2*b.EGYSEG))
    jAblak.blit(kep.clyde, (x-2*b.EGYSEG,y))
    
    for i in range(3, b.MERET, b.EGYSEG):
        fal_f = pygame.Rect((i, 2*b.MERET/3 - 7*b.EGYSEG), (b.EGYSEG-7, b.EGYSEG-7))
        fal_a = pygame.Rect((i, 2*b.MERET/3 + b.EGYSEG), (b.EGYSEG-7, b.EGYSEG-7))
        pygame.gfxdraw.box(jAblak, fal_f, b.BLUE)
        pygame.gfxdraw.box(jAblak, fal_a, b.BLUE)
     
    jAblak.blit(kep.pac_ny, (x - 2*b.EGYSEG, 4*b.MERET/5))
    jAblak.blit(kep.gyava_s, (x,  4*b.MERET/5))
    jAblak.blit(kep.gyava_v, (x + 2*b.EGYSEG,  4*b.MERET/5))
    
    
def nev_be(jAblak, b):
    jAblak.fill(b.BLACK)
    jatek_vege(jAblak, b)
    bal_also("Enter - Bevitel/Tovább", b.YELLOW, jAblak, b)
    pygame.display.update()
    font = pygame.font.SysFont('Arial', 3*b.EGYSEG) 
    clip = jAblak.get_clip()
    hely = pygame.Rect(b.MERET/20, 2*b.MERET/3 - b.EGYSEG*4, 18*b.MERET/20, b.EGYSEG*4)
    jAblak.set_clip(hely)
    
    bemenet = ""
    enter = False
    while not enter:
        jAblak.fill(b.BLACK)
        szoveg = font.render("Név: " + bemenet + '|', True, b.YELLOW)
        jAblak.blit(szoveg, hely)
        pygame.display.update()
 
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                enter = True
            elif event.key == pygame.K_BACKSPACE:
                bemenet = bemenet[:-1]
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(event)
                pygame.quit()
                quit()
            else:
                bemenet += event.unicode
 
        if event.type == pygame.QUIT:
            pygame.event.post(event)
            pygame.quit()
            quit()
 
    jAblak.set_clip(clip);
    return bemenet

def bal_also(szoveg, szin, jAblak, b):
    szoveg = forma(szoveg, szin)
    jAblak.blit(szoveg, (b.EGYSEG, b.MERET - szoveg.get_height()))
    
def skip():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            return True
    return False    
    
def animacio(jAblak, b):
    kep = Kepek()
    quit = False
    clock = pygame.time.Clock()
    
    zaba = 0
    x = -b.EGYSEG
    y = b.MERET/3
    while x < b.MERET + 9*b.EGYSEG and not quit:
        clock.tick(b.FPS)
        quit = skip()
        if zaba == 16:
            zaba = 0
        elif zaba < 8:
            pac = kep.pac_ny
        else:
            pac = kep.pac_cs
         
        bal_also("Átugráshoz nyomjon meg egy gombot", b.WHITE, jAblak, b)
        jAblak.blit(pac, (x-8*b.EGYSEG,y))
        jAblak.blit(kep.gyava_s, (x-6*b.EGYSEG,y))
        jAblak.blit(kep.gyava_s, (x-4*b.EGYSEG,y))
        jAblak.blit(kep.gyava_s, (x-2*b.EGYSEG,y))
        jAblak.blit(kep.gyava_s, (x,y))
        pygame.display.update()
        jAblak.fill(b.BLACK)
        zaba += 1
        x += 4
        
    zaba = 0
    x = b.MERET + b.EGYSEG 
    y = b.MERET/3
    while x > -9*b.EGYSEG and not quit:
        clock.tick(b.FPS) 
        quit = skip()
        if zaba == 16:
            zaba = 0
        elif zaba < 8:
            pac = pygame.transform.flip(kep.pac_ny, True, False)
        else:
            pac = pygame.transform.flip(kep.pac_cs, True, False)
            
        bal_also("Átugráshoz nyomjon meg egy gombot", b.WHITE, jAblak, b)    
        jAblak.blit(pac, (x,y))
        jAblak.blit(kep.blinky, (x+2*b.EGYSEG,y))
        jAblak.blit(kep.inky, (x+4*b.EGYSEG,y))
        jAblak.blit(kep.pinky, (x+6*b.EGYSEG,y))
        jAblak.blit(kep.clyde, (x+8*b.EGYSEG,y))
        pygame.display.update()
        jAblak.fill(b.BLACK)
        zaba += 1
        x -= 4
        
def kep(jAblak, b):
    kep = Kepek()
    x = b.MERET/2
    y = b.MERET/3
    jAblak.blit(kep.pac_ny, (x + 4*b.EGYSEG - kep.pac_ny.get_width()/2, y))
    jAblak.blit(kep.blinky, (x + 2*b.EGYSEG - kep.blinky.get_width()/2, y))
    jAblak.blit(kep.inky, (x - kep.inky.get_width()/2, y))
    jAblak.blit(kep.pinky, (x - 2*b.EGYSEG - kep.pinky.get_width()/2, y))
    jAblak.blit(kep.clyde, (x - 4*b.EGYSEG - kep.clyde.get_width()/2, y))
    

def fomenu(jAblak, b):
    i = 0
    menu = True
    menu_lista = ["start", "top10", "kilep"]
    menu_meret = [int(b.EGYSEG*1.9), int(b.EGYSEG*2.3)]
    menupont = menu_lista[i]
    
    while menu:
        jAblak.fill(b.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_UP or event.key==pygame.K_w:
                    if menupont == "start":
                        i = 2
                    else:
                        i -= 1
                    menupont = menu_lista[i]
                elif event.key == pygame.K_DOWN or event.key==pygame.K_s:
                    if menupont == "kilep":
                        i = 0
                    else:
                        i+= 1
                    menupont = menu_lista[i]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                    
                if event.key == pygame.K_RETURN:
                    if menupont == "start":
                        return True
                    elif menupont == "top10":
                        nev_ki(jAblak, b)
                    else:
                        pygame.quit()
                        quit()
        
        if menupont == "start":
            menu_start = forma("START", b.WHITE, menu_meret[1])
        else:
            menu_start = forma("START", b.YELLOW, menu_meret[0])
        if menupont == "top10":
            menu_top10 = forma("TOP10", b.WHITE, menu_meret[1])
        else:
            menu_top10 = forma("TOP10", b.YELLOW, menu_meret[0])
        if menupont == "kilep":
            menu_kilep = forma("KILÉPÉS", b.WHITE, menu_meret[1])
        else:
            menu_kilep = forma("KILÉPÉS", b.YELLOW, menu_meret[0])

        nyito = pygame.image.load('PAC_OPEN_k.png')
            
        cim = forma('PA   MAN', b.YELLOW, b.EGYSEG*5,)
        bal_also("ESC - Kilépés", b.WHITE, jAblak, b)
 
        start_rect = menu_start.get_rect()
        top10_rect = menu_top10.get_rect()
        kilep_rect = menu_kilep.get_rect()
        
        kep(jAblak, b)
        jAblak.blit(cim, ((b.MERET/2 - (cim.get_width())/2), b.EGYSEG))
        jAblak.blit(nyito, ((b.MERET/2 - (cim.get_width()/5.1),  int(2.5*b.EGYSEG))))
        
        jAblak.blit(menu_start, (b.MERET/2 - (start_rect[2]/2), 2 * b.MERET/3.5))
        jAblak.blit(menu_top10, (b.MERET/2 - (top10_rect[2]/2), 2 * b.MERET/3.5 + 70))
        jAblak.blit(menu_kilep, (b.MERET/2 - (kilep_rect[2]/2), 2 * b.MERET/3.5 + 2*70))
        pygame.display.update()