import random

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 2000)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
            if event.type == MYEVENTTYPE:
                screen.fill((0, 0, 0))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

    # https: // www.pygame.org / docs / ref/examples.html