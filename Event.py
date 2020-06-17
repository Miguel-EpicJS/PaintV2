import pygame

class Events:

    def exit(exec):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exec = False

        return exec

