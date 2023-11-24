import pygame
import random


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    # здесь рисование

    for i in range(100000):
        screen.fill(pygame.Color('#{:02x}{:02x}{:02x}'.format(random.randrange(256),
                                 random.randrange(256), random.randrange(256))),
                    (random.random() * width,
                     random.random() * height, 1, 1))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
