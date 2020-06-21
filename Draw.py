import pygame, Keyboard

class Draw:
    drawingRect = False
    drawingCircle = False
    def DrawRect(self, screen, w, h, colors):
        drawing = Keyboard.KeyBoard.DrawRect(self)
        mouse = pygame.mouse.get_pos()

        if drawing and pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, colors, [mouse[0], mouse[1], w, h])
        elif drawing and pygame.mouse.get_pressed() == (0, 0, 1):
            pygame.draw.rect(screen, (255, 255, 255), [mouse[0], mouse[1], w, h])

    def DrawCircle(self, screen, radios, color):
        drawing = Keyboard.KeyBoard.DrawCircle(self)
        mouse = pygame.mouse.get_pos()

        if drawing and pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.circle(screen, color, mouse, radios)
        elif pygame.mouse.get_pressed() == (0, 0, 1) and drawing:
            pygame.draw.circle(screen, (255, 255, 255), mouse, radios)


    def DrawableArea(self, h, w, x, y):

        mousePos = pygame.mouse.get_pos()
        if (mousePos[0] > x and mousePos[0] < x + w and mousePos[1] > y and mousePos[1] < y + h):
            return True
        else:
            return False


