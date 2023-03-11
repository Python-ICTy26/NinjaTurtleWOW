import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        # Создание списка клеток
        # Добавил поле
        self.grid = self.create_grid(randomize=True)
        self.draw_grid(self.grid)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()
            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.grid = self.get_next_generation()
            self.draw_grid(self.grid)
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        if randomize:
            return [
                [random.randint(0, 1) for i in range(self.cell_width)]
                for i in range(self.cell_height)
            ]
        else:
            return [[0 for i in range(self.cell_width)] for i in range(self.cell_height)]

    def draw_grid(self, grid: list[list[int]]) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if grid[i][j] == 1:
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

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        height, width = cell
        cells = []
        if height == 0 and width == 0:
            cells.append(self.grid[0][1])
            cells.append(self.grid[1][0])
            cells.append(self.grid[1][1])
        elif height == 0 and width == self.cell_width - 1:
            cells.append(self.grid[0][width - 1])
            cells.append(self.grid[1][width])
            cells.append(self.grid[1][width - 1])
        elif height == self.cell_height - 1 and width == 0:
            cells.append(self.grid[height - 1][0])
            cells.append(self.grid[height - 1][1])
            cells.append(self.grid[height][1])
        elif height == self.cell_height - 1 and width == self.cell_width - 1:
            cells.append(self.grid[height - 1][width - 1])
            cells.append(self.grid[height][width - 1])
            cells.append(self.grid[height - 1][width])
        elif height == 0:
            cells.append(self.grid[0][width - 1])
            cells.append(self.grid[0][width + 1])
            cells.append(self.grid[1][width])
            cells.append(self.grid[1][width - 1])
            cells.append(self.grid[1][width + 1])
        elif width == 0:
            cells.append(self.grid[height - 1][0])
            cells.append(self.grid[height + 1][0])
            cells.append(self.grid[height][1])
            cells.append(self.grid[height - 1][1])
            cells.append(self.grid[height + 1][1])
        elif height == self.cell_height - 1:
            cells.append(self.grid[height][width - 1])
            cells.append(self.grid[height][width + 1])
            cells.append(self.grid[height - 1][width])
            cells.append(self.grid[height - 1][width - 1])
            cells.append(self.grid[height - 1][width + 1])
        elif width == self.cell_width - 1:
            cells.append(self.grid[height - 1][width])
            cells.append(self.grid[height + 1][width])
            cells.append(self.grid[height][width - 1])
            cells.append(self.grid[height - 1][width - 1])
            cells.append(self.grid[height + 1][width - 1])
        else:
            cells.append(self.grid[height][width - 1])
            cells.append(self.grid[height][width + 1])
            cells.append(self.grid[height - 1][width])
            cells.append(self.grid[height + 1][width])
            cells.append(self.grid[height - 1][width - 1])
            cells.append(self.grid[height - 1][width + 1])
            cells.append(self.grid[height + 1][width + 1])
            cells.append(self.grid[height + 1][width - 1])
        return cells

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        next_grid = [[0 for i in range(self.cell_width)] for i in range(self.cell_height)]
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j] == 1 and (
                    sum(self.get_neighbours((i, j))) == 2 or sum(self.get_neighbours((i, j))) == 3
                ):
                    next_grid[i][j] = 1
                elif self.grid[i][j] == 0 and sum(self.get_neighbours((i, j))) == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0
        return next_grid


if __name__ == "__main__":
    game = GameOfLife(width=640, height=480, cell_size=10, speed=10)
    game.run()
