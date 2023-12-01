import pygame


class Board:
    # создание поля
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                pygame.draw.rect(screen, "white",
                                 (self.left + self.cell_size * col, self.top + self.cell_size * row,
                                  self.cell_size, self.cell_size), 1)
                if self.board[row][col] == 1:
                    pygame.draw.rect(screen, "white",
                                     (self.left + self.cell_size * col, self.top + self.cell_size * row,
                                      self.cell_size, self.cell_size))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = mouse_pos[0] - self.left
        y = mouse_pos[1] - self.top
        if x < 0 or y < 0:
            return None
        col = x // self.cell_size
        row = y // self.cell_size
        if col >= self.width or row >= self.height:
            return None
        return col, row

    def on_click(self, cell_coords):
        if cell_coords:
            for row in range(self.height):
                self.board[row][cell_coords[0]] = (self.board[row][cell_coords[0]] + 1) % 2
            for col in range(self.width):
                self.board[cell_coords[1]][col] = (self.board[cell_coords[1]][col] + 1) % 2
            self.board[cell_coords[1]][cell_coords[0]] = (self.board[cell_coords[1]][cell_coords[0]] + 1) % 2


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Клетчатое поле')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    board = Board(8, 6)
    board.set_view(50, 20, 40)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()