import pygame

class KeyBoard:

    def CleanScreen(self, screen):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            screen.fill((255, 255, 255));

    def DrawRect(self):
        ok = False
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            ok = True

        return ok

    def DrawCircle(self):
        ok = False
        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            ok = True

        return ok
