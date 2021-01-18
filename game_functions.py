import sys
import pygame
from bullet import Bullet
from alien import Alien
def check_keydown_events(event,ai_settings,screen, ship,bullets):
    '''相应按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship ,bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event, ship):
    '''相响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship,aliens,bullets):
    '''重绘屏幕'''
    # 每次循环都重绘屏幕
    # 屏幕背景颜色
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重回所有子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 在屏幕指定 位置绘制飞船
    ship.blitme()
    aliens.draw(screen)
    # 让最新绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 :
            bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
    """创建外星人机群"""
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width #获取外星人宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width #计算可以放外星飞船的水平空间
    number_aliens_x = int(available_space_x / (2 * alien_width)) # 计算可以放置的飞船数量

    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width +2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳的外星飞船"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2* alien_width*alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可以容纳多少外星人"""
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows