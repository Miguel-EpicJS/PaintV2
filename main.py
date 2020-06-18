import pygame
import Event, Colors, Keyboard, Draw, Button


#Objects
events = Event.Events()
colors = Colors.Colors()
keyboard = Keyboard.KeyBoard()
draw = Draw.Draw()

btnPlus = Button.Button()
btnMinus = Button.Button()

#Vars
exec = True
d = 9
up = 8
#pygame vars

pygame.init()
paint = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Paint V2")

#Game logic

paint.fill(colors.white)
btnPlus.CreateButton(paint, 1210, 85, "img/up.png")
btnMinus.CreateButton(paint, 1210, 167, "img/down.png")
while exec:
    pygame.display.update()
    if not events.exit():
        exec = False
    if keyboard.CleanScreen():
        paint.fill((255, 255, 255))
        btnPlus.CreateButton(paint, 1210, 85, "img/up.png")
        btnMinus.CreateButton(paint, 1210, 167, "img/down.png")

    draw.DrawRect(paint, d, d, colors.cyan)
    draw.DrawCircle(paint, d, colors.green)
    pygame.time.delay(10)
    #(1210, 85) e (1241, 167)
    if btnPlus.getPressedButton(1210, 85, 32, 32):
        d += up
    if btnMinus.getPressedButton(1210, 167, 32, 32) and d > up:
        d -= up

pygame.quit()
