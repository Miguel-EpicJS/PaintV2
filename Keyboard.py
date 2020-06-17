import pygame

class KeyBoard:

    def CleanScreen(self, screen):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            screen.fill((255, 255, 255));

