import pygame
import random


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    pygame.draw.rect(screen, 'red', pygame.Rect(1, 1, width - 2, height - 2), 0)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
