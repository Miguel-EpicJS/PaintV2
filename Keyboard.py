import pygame

class KeyBoard:

    def CleanScreen(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:

            return True



    def DrawRect(self):

        mouse = pygame.mouse.get_pressed()
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            return True
        elif mouse == (0, 0, 1):
            return False


    def DrawCircle(self):

        key = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if key[pygame.K_c]:
            return True
        elif mouse == (0, 0, 1):
            return False

