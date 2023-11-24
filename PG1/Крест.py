import pygame
import random


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    pygame.draw.line(screen, "white", (0, 0), size, 5)
    pygame.draw.line(screen, "white", (0, height), (width, 0), 5)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
