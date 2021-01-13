import sys
import pygame

def check_events(ship):
    """相应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 飞船向右移动
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False



def update_screen(ai_settings, screen, ship):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环都重绘屏幕
    # 屏幕背景颜色
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最新绘制的屏幕可见
    pygame.display.flip()