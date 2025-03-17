import pygame
from settings import GRID_WIDTH, GRID_HEIGHT

class Grid:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def is_row_full(self, row):
        """指定した行が一列そろっているか確認"""
        return all(cell != 0 for cell in self.grid[row])
    
    def clear_row(self, row):
        """行を消去し、上の行を一段下げる"""
        del self.grid[row]
        self.grid.insert(0, [0 for _ in range(self.width)])

