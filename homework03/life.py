import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        if randomize:
            return [[random.randint(0, 1) for i in range(self.rows)] for i in range(self.cols)]
        else:
            return [[0 for i in range(self.rows)] for i in range(self.cols)]

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        height, width = cell
        cells = []
        if height == 0 and width == 0:
            cells.append(self.curr_generation[0][1])
            cells.append(self.curr_generation[1][0])
            cells.append(self.curr_generation[1][1])
        elif height == 0 and width == self.cols - 1:
            cells.append(self.curr_generation[0][width - 1])
            cells.append(self.curr_generation[1][width])
            cells.append(self.curr_generation[1][width - 1])
        elif height == self.rows - 1 and width == 0:
            cells.append(self.curr_generation[height - 1][0])
            cells.append(self.curr_generation[height - 1][1])
            cells.append(self.curr_generation[height][1])
        elif height == self.rows - 1 and width == self.cols - 1:
            cells.append(self.curr_generation[height - 1][width - 1])
            cells.append(self.curr_generation[height][width - 1])
            cells.append(self.curr_generation[height - 1][width])
        elif height == 0:
            cells.append(self.curr_generation[0][width - 1])
            cells.append(self.curr_generation[0][width + 1])
            cells.append(self.curr_generation[1][width])
            cells.append(self.curr_generation[1][width - 1])
            cells.append(self.curr_generation[1][width + 1])
        elif width == 0:
            cells.append(self.curr_generation[height - 1][0])
            cells.append(self.curr_generation[height + 1][0])
            cells.append(self.curr_generation[height][1])
            cells.append(self.curr_generation[height - 1][1])
            cells.append(self.curr_generation[height + 1][1])
        elif height == self.rows - 1:
            cells.append(self.curr_generation[height][width - 1])
            cells.append(self.curr_generation[height][width + 1])
            cells.append(self.curr_generation[height - 1][width])
            cells.append(self.curr_generation[height - 1][width - 1])
            cells.append(self.curr_generation[height - 1][width + 1])
        elif width == self.cols - 1:
            cells.append(self.curr_generation[height - 1][width])
            cells.append(self.curr_generation[height + 1][width])
            cells.append(self.curr_generation[height][width - 1])
            cells.append(self.curr_generation[height - 1][width - 1])
            cells.append(self.curr_generation[height + 1][width - 1])
        else:
            cells.append(self.curr_generation[height][width - 1])
            cells.append(self.curr_generation[height][width + 1])
            cells.append(self.curr_generation[height - 1][width])
            cells.append(self.curr_generation[height + 1][width])
            cells.append(self.curr_generation[height - 1][width - 1])
            cells.append(self.curr_generation[height - 1][width + 1])
            cells.append(self.curr_generation[height + 1][width + 1])
            cells.append(self.curr_generation[height + 1][width - 1])
        return cells

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        next_grid = [[0 for i in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.curr_generation[i][j] == 1 and (
                        sum(self.get_neighbours((i, j))) == 2 or sum(self.get_neighbours((i, j))) == 3
                ):
                    next_grid[i][j] = 1
                elif self.curr_generation[i][j] == 0 and sum(self.get_neighbours((i, j))) == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0
        return next_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations == self.generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation == self.prev_generation:
            return False
        else:
            return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        f = open(filename, "r").readlines()
        grid = []
        for i in range(len(f)):
            r = list(map(int, f[i].split()))
            grid.append(r)
        life = GameOfLife(size=(len(grid), len(grid[0])), randomize=False)
        life.curr_generation = grid
        return life

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as f:
            for i in self.curr_generation:
                f.write("".join([str(j) for j in i]) + "\n")
