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


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows):
        super().__init__()
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = random.randrange(len(self.frames))
        self.image = self.frames[self.cur_frame]
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(height - self.rect.height)
        while pygame.sprite.spritecollide(self, all_sprites, False):
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(height - self.rect.height)
        all_sprites.add(self)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 600
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    running = True
    FPS = 10
    clock = pygame.time.Clock()
    for _ in range(10):
        AnimatedSprite(load_image("dragon_sheet8x2.png"), 8, 2)

    while running:
        screen.fill(pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        all_sprites.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
