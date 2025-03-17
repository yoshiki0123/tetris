import random 

class Tetromino:
    # class変数：クラスのすべてのインスタンス（オブジェクト）が共有する変数　
    SHAPES = [
        [[1, 1, 1], 
         [0, 1, 0]],  # T型
        [[1, 1, 1, 1]],  # I型
        [[1, 1], 
         [1, 1]],  # O型
        [[0, 1, 1], 
         [1, 1, 0]],  # S型
        [[1, 1, 0],
         [0, 1, 1]],  # Z型
        [[1, 1, 1], 
         [1, 0, 0]],  # L型
        [[1, 1, 1], 
         [0, 0, 1]],  # J型
    ]

    def __init__(self):
        self.shape = random.choice(self.SHAPES) # ランダムにブロックを選択
        self.x = 3
        self.y = 0
    
    def rotate(self):
        """90度回転させる"""
        self.shape = [list(row) for row in zip(*self.shape[::-1])]