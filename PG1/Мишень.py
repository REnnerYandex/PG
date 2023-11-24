
if __name__ == '__main__':
    n, k = map(int, input().split()) # толщина и количество

    import pygame
    pygame.init()
    size = width, height = 2 * n * k, 2 * n * k
    screen = pygame.display.set_mode(size)
    xc, yc = width // 2, height // 2
    colors = ('red', 'green', 'blue')
    for i in range(k - 1, -1, -1):
        pygame.draw.circle(screen, colors[i % 3], (xc, xc), n * (i + 1))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
