import pygame
import Event, Colors, Keyboard, Draw


#Objects
events = Event.Events()
colors = Colors.Colors()
keyboard = Keyboard.KeyBoard()
draw = Draw.Draw()
#Vars
exec = True

#pygame vars

pygame.init()
paint = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Paint V2")

#Game logic

paint.fill(colors.white)
while exec:
    pygame.display.update()
    if not events.exit():
        exec = False
    keyboard.CleanScreen(paint)
    draw.DrawRect(paint, 10, 10, colors.cyan)
    draw.DrawCircle(paint, 10, colors.green)
    pygame.time.delay(10)
pygame.quit()
