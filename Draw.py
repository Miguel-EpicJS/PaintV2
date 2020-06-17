import pygame, Colors, Keyboard

class Draw:
    def DrawRect(self, screen, w, h, colors):

        mouse = pygame.mouse.get_pos()
        keyboard = Keyboard.KeyBoard()

        if keyboard.DrawRect():
            pygame.draw.rect(screen, colors, [mouse[0], mouse[1], w, h])

    def DrawCircle(self, screen, radios, color):
        mouse = pygame.mouse.get_pos()
        keyboard = Keyboard.KeyBoard()
        if keyboard.DrawCircle():
            pygame.draw.circle(screen, color, mouse, radios)

