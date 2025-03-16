import pygame

# 画面サイズ
GRID_SIZE = 30 # 1マスのサイズ(px)
GRID_WIDTH = 10 # 横のマス数
GRID_HEIGHT = 20 # 縦のマス数

SCREEN_WIDTH = GRID_SIZE * GRID_WIDTH
SCREEN_HEIGHT = GRID_SIZE * GRID_HEIGHT

# 色の定義
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# pygameの初期化
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # ウィンドウを作成(10 * 20)
pygame.display.set_caption("Tetris - Grid")

# グリッドを描画する関数
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            # マスを描画　pygame.draw.rect(画面, 色, (x座標, y座標, 幅, 高さ), 線の太さ)
            pygame.draw.rect(screen, GRAY, (x, y, GRID_SIZE, GRID_SIZE), 1)

running = True
while running:
    screen.fill(WHITE) # windowを白で塗りつぶし
    draw_grid() # グリッド描写
    pygame.display.flip() # 画面を更新

    # イベント処理(ウィンドウを閉じたら終了)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
