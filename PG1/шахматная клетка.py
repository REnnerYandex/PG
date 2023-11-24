
if __name__ == '__main__':
    print('ввод стороны окна и количесво клеток')
    w, n = map(int, input().split()) # тсторона окна и количество
    while w % n != 0:
        print('повторить ввод: W должно делиться на N')
        w, n = map(int, input().split())  # тсторона окна и количество


    import pygame
    pygame.init()
    size = width, height = w, w
    screen = pygame.display.set_mode(size)
    screen.fill('white')

    for r in range(n):
        for c in range(n):
            if (r + c) % 2 == 0:
                screen.fill('black', pygame.Rect(c * (w // n), r * (w // n), w // n, w // n))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
