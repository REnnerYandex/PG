import os
import sys
import pygame
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Arrow(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("arrow.png")
        self.rect = self.image.get_rect()

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEMOTION:
            self.rect = args[0].pos


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    Arrow(all_sprites)

    running = True
    pygame.mouse.set_visible(False)
    while running:
        screen.fill(pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            all_sprites.update(event)

        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

