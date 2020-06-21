import pygame
import Event, Colors, Keyboard, Draw, Button, Text

#const

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

#Vars
exec = True
drawingCircle = False
drawingRect = False
d = 9
w = 9
h = 9
up = 8
red = 1
blue = 1
green = 1
alter = 5

def ButtonUpdate():
    btnPlus.CreateImageButton(paint, 1210, 85, "img/up.png")
    btnMinus.CreateImageButton(paint, 1210, 167, "img/down.png")
    btnMinusWidth.CreateImageButton(paint, 30, 167, "img/down.png")
    btnPlusWidth.CreateImageButton(paint, 30, 85, "img/up.png")

    btnRedPlus.CreateNoImageButton(paint, 50, 400, 50, 50, colors.red)
    btnRedMinus.CreateNoImageButton(paint, 1200, 400, 50, 50, colors.red)

    btnGreenPlus.CreateNoImageButton(paint, 50, 470, 50, 50, colors.green)
    btnGreenMinus.CreateNoImageButton(paint, 1200, 470, 50, 50, colors.green)

    btnBluePlus.CreateNoImageButton(paint, 50, 540, 50, 50, colors.blue)
    btnBlueMinus.CreateNoImageButton(paint, 1200, 540, 50, 50, colors.blue)

def recognizingClicks():
    global d, w, h, up
    if btnPlus.getPressedButton(1210, 85, 32, 32):
        d += up
        w += up


    if btnMinus.getPressedButton(1210, 167, 32, 32) and d > up:
        d -= up
        w -= up

    if btnPlusHeight.getPressedButton(30, 85, 32, 32):
        h += up


    if btnMinusHeight.getPressedButton(30, 167, 32, 32) and d > up:
        h -= up


def AlterRedColor():
    global red
    if btnRedMinus.getPressedButton(1200, 470, 50, 50) and red > 1:
        red -= alter

    if btnRedPlus.getPressedButton(50, 400, 50, 50) and red < 255 :
        red += alter

def AlterGreenColor():
    global green
    if btnGreenMinus.getPressedButton(1200, 470, 50, 50) and green > 1:
        green -= alter

    if btnGreenPlus.getPressedButton(50, 470, 50, 50) and green < 255:
        green += alter

def AlterBlueColor():
    global blue
    if btnBluePlus.getPressedButton(50, 540, 50, 50) and blue < 255:
        blue += alter

    if btnBlueMinus.getPressedButton(1200, 540, 50, 50) and blue > 1:
        blue -= alter

def AlterAllColors():
    AlterRedColor()
    AlterGreenColor()
    AlterBlueColor()

#Objects
events = Event.Events()
colors = Colors.Colors()
keyboard = Keyboard.KeyBoard()
draw = Draw.Draw()
text = Text.Text()

btnPlus = Button.Button()
btnMinus = Button.Button()
btnPlusWidth = Button.Button()
btnPlusHeight = Button.Button()
btnMinusWidth = Button.Button()
btnMinusHeight = Button.Button()

btnRedPlus = Button.Button()
btnRedMinus = Button.Button()

btnBluePlus = Button.Button()
btnBlueMinus = Button.Button()

btnGreenPlus = Button.Button()
btnGreenMinus = Button.Button()



#pygame vars

pygame.init()
paint = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint V2")
clock = pygame.time.Clock()

#Game logic

paint.fill(colors.white)

ButtonUpdate()

while exec:
    #if pygame.mouse.get_pressed() == (1,0,0):
    #   print(pygame.mouse.get_pos())
    pygame.display.update()
    if not events.exit():
        exec = False
    if keyboard.CleanScreen():
        paint.fill((255, 255, 255))
        ButtonUpdate()
    AlterAllColors()
    if draw.DrawableArea(700, 700, 320, 150):
        draw.DrawRect(paint, w, h, (red, green, blue))
        draw.DrawCircle(paint, d, (red, green, blue))

    pygame.time.delay(10)

    recognizingClicks()

    clock.tick(30)
pygame.quit()
