import pygame
from Menu import fajl_ki, nev_ki, fomenu, forma, bal_also, animacio
from Beallitasok import Beallitasok 
from Pacman import Pacman
from Szellemek import Blinky, Inky, Pinky, Clyde
from Palya import Palya
from Kaja import Kaja

def main():
    b = Beallitasok()
    jAblak = b.kezdo()   
    pont = 0
    clock = pygame.time.Clock()
    TOP10 = False
    keepGoing_game = False
    animacio(jAblak, b)
    while True:
        jAblak.fill(b.BLACK)
        if TOP10:
            fajl_ki(pacman.pont, jAblak, b)
            nev_ki(jAblak, b)
        keepGoing_game = fomenu(jAblak, b)      
        while keepGoing_game:
            szellemek = [Blinky(b),Inky(b), Pinky(b), Clyde(b)]
            pacman = Pacman(b)
            pacman.pont = pont
            palya = Palya().palya_be(b)
            csomopontok = Palya().csomopont_be(b)
            kiskaja = Kaja().kiskaja_be()
            nagykaja = Kaja().nagykaja_be()
            kaja = Kaja()
            keepGoing_round = True
            while keepGoing_round:
                clock.tick(b.FPS)
                
                keepGoing_game = keepGoing_round = TOP10 = pacman.iranyit()
                       
                pacman.mozog(palya)
                pacman.billentyu = False
                pacman.teleport(b)
                pacman.melyik()
                jAblak.fill(b.BLACK)
                kiskaja = kaja.kkaja_eves(kiskaja, pacman)
                nagykaja = kaja.nkaja_eves(nagykaja, pacman, szellemek)
                kaja.kaja_ki(kiskaja, nagykaja, jAblak)
                
                for sz in szellemek:
                    sz.mozog(palya, csomopontok, pacman, b)
                    sz.teleport(b)
                    jAblak.blit(sz.felulet, sz.rect)
                    if sz.eheto:
                        sz.eheto_e()
                    if sz.nev == "Blinky":
                        sz.cruise_elroy(kiskaja)
                
                Palya().palya_ki(palya, jAblak, b)
                
                
                jAblak.blit(pacman.pont_kiir(b), (b.EGYSEG, 0))
                pacman.elet_kiir(b, jAblak)
                bal_also("ESC - Kilépés a főmenübe", b.YELLOW, jAblak, b)
                    
                jAblak.blit(pacman.felulet, pacman.rect)
                pygame.display.update()
                
                
                for sz in szellemek:
                    if pacman.rect.colliderect(sz.rect):
                        if sz.eheto:
                            szellemek.pop(szellemek.index(sz))
                            pacman.pont += 50
                            if sz.nev == "Blinky":
                                szellemek.append(Blinky(b))
                            elif sz.nev == "Pinky":
                                szellemek.append(Pinky(b))
                            elif sz.nev == "Inky":
                                szellemek.append(Inky(b))
                            elif sz.nev == "Clyde":
                                szellemek.append(Clyde(b))      
                        else:
                            pacman.elet -= 1
                            pacman.uj(b)
                            szellemek = [Inky(b),Blinky(b), Pinky(b),Clyde(b)]
                            Inky.db = 1
                            if pacman.elet == 0:
                                keepGoing_game = keepGoing_round = False
                                TOP10 = True
                            break
                        
                pont = pacman.pont
                if len(kiskaja) == 0 and len(nagykaja) == 0:
                    keepGoing_round = False
                

main()
pygame.quit()

