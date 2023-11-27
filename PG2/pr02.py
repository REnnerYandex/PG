import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True

    radius = 20
    x_pos = -radius
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for i in range(10000):
            screen.fill(pygame.Color('#{:02x}{:02x}{:02x}'.format(random.randrange(256),
                                                                  random.randrange(256), random.randrange(256))),
                        (random.random() * width,
                         random.random() * height, 1, 1))
        pygame.display.flip()

    pygame.quit()

