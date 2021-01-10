import sys
import pygame
def run_game():
    # 初始化创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    # 窗口的标题
    pygame.display.set_caption("Alien Invasion")
    # 开始游戏主循环
    while True:
        # 监控键盘和鼠标
        for event in pygame.event.get():
            # 玩家点击quit
           if event.type == pygame.QUIT:
               sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
run_game()
