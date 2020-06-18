import pygame

class Button:

    def CreateButton(self, screen, x, y, path):
        img = pygame.image.load(path);
        screen.blit(img, (x, y))


    def getPressedButton(self,x,y,w,h):
        mousePos = pygame.mouse.get_pos()
        if(mousePos[0] > x and mousePos[0] < x+w and mousePos[1] > y and mousePos[1] < y+h and pygame.mouse.get_pressed() == (1, 0, 0)):
            return True
        else:
            return False

