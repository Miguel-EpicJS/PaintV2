import pygame
import Event, Colors, Keyboard


#Objects
events = Event.Events()
colors = Colors.Colors()
keyboard = Keyboard.KeyBoard()
#Vars
exec = True

#pygame vars

pygame.init()
paint = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Paint V2")

#Game logic

#paint.fill(colors.white)
while exec:
    pygame.display.update()
    if not events.exit():
        exec = False
    keyboard.CleanScreen(paint)


pygame.quit()
