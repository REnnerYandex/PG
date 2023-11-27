import random
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    v = 100
    radius = 10
    clock = pygame.time.Clock()
    balls = []
    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                color = pygame.Color('#{:02x}{:02x}{:02x}'.format(random.randrange(256),
                                 random.randrange(256), random.randrange(256)))
                v = random.randint(50, 100)
                balls.append([[event.pos[0], event.pos[1]], [-1, -1], color, v])

        for ball in balls:
            ball[0][0] += ball[1][0] * (ball[3] / 1000)
            ball[0][1] += ball[1][1] * (ball[3] / 1000)
            if ball[0][0] < radius:
                ball[0][0] = radius
                ball[1][0] *= -1
            if ball[0][1] < radius:
                ball[0][1] = radius
                ball[1][1] *= -1
            if ball[0][0] > width - radius:
                ball[0][0] = width - radius
                ball[1][0] *= -1
            if ball[0][1] > height - radius:
                ball[0][1] = height - radius
                ball[1][1] *= -1
        for ball in balls:
            pygame.draw.circle(screen, ball[2], ball[0], radius)
        pygame.display.flip()

    pygame.quit()