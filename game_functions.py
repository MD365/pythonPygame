import sys
import pygame

# def check_events(ship):
#     """相应键盘和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 # 飞船向右移动
#                 ship.moving_right = True
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = True
#
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False
def check_keydown_events(event, ship):
    '''相应按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    '''相响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship):
    '''重绘屏幕'''
    # 每次循环都重绘屏幕
    # 屏幕背景颜色
    screen.fill(ai_settings.bg_color)
    # 在屏幕指定 位置绘制飞船
    ship.blitme()

    # 让最新绘制的屏幕可见
    pygame.display.flip()