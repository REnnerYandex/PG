import random

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    radius = 20
    x_pos = -20
    y_pos = 200
    v = 400  # пикселей в секунду
    clock = pygame.time.Clock()
    color = pygame.Color('red')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen,color, (int(x_pos), y_pos), radius)
        x_pos += v * clock.tick() / 1000  # v * t в секундах
        if x_pos > width + radius:
            x_pos = -radius
            y_pos = random.randrange(400 - radius) + radius
            color = pygame.Color('#{:02x}{:02x}{:02x}'.format(random.randrange(256),
                                 random.randrange(256), random.randrange(256)))
        pygame.display.flip()
    pygame.quit()