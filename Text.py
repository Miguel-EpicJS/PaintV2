import pygame

class Text:
#beta test
    def CreateText(self, text, size, color, screen, x, y):
        pygame.font.init()
        font = pygame.font.get_default_font()
        fontSys = pygame.font.SysFont(font, size)
        txtScreen = fontSys.render(text, 1, color)
        screen.blit(txtScreen, (x, y))

