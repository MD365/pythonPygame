
import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf
def run_game():
    # 初始化创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 绘制一个屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_hight)
    )
    # 窗口的标题
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 开始游戏主循环
    while True:
        # 监控键盘和鼠标
        gf.check_events(ship)

        ship.update()
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship)

run_game()
