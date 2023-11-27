import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('желтый круг')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    v = 10
    clock = pygame.time.Clock()
    running = True
    screen.fill('blue')
    drawing = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill('blue')
                drawing = True
                x, y = event.pos
                radius = 0
        if drawing:
            radius += v / 1000
            pygame.draw.circle(screen, 'yellow', (x, y), radius)
        pygame.display.flip()

    pygame.quit()