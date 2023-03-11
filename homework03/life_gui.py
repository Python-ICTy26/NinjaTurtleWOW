import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.width = life.rows * cell_size
        self.height = life.cols * cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.life.curr_generation[i][j] == 1:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("green"),
                        (
                            j * self.cell_size + 1,
                            i * self.cell_size + 1,
                            self.cell_size - 1,
                            self.cell_size - 1,
                        ),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("white"),
                        (
                            j * self.cell_size + 1,
                            i * self.cell_size + 1,
                            self.cell_size - 1,
                            self.cell_size - 1,
                        ),
                    )

    def myself(self, height, width) -> None:
        col = height // self.cell_size
        row = width // self.cell_size
        if self.life.curr_generation[row][col] == 0:
            self.life.curr_generation[row][col] = 1
        else:
            self.life.curr_generation[row][col] = 0

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = not pause
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    height, width = event.pos
                    self.myself(height, width)
                    self.draw_grid()
                    self.draw_lines()
                    pygame.display.flip()
                elif event.type == QUIT:
                    running = False
            if not self.life.is_changing:
                running = False
            elif self.life.is_max_generations_exceeded:
                running = False
            if not pause:
                self.life.step()
                self.draw_lines()
                self.draw_grid()
                pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    game = GameOfLife(size=(100, 100), randomize=True)
    gui = GUI(life=game, cell_size=10, speed=10)
    gui.run()
