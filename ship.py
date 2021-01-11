import pygame

class Ship():


    def __init__(self, screen):
        '''初始化飞船    '''
        self.screen = screen

        # 加载飞船图像并获取外形矩形
        self.image = pygame.image.load('images/ship.bmp')
        # 获取飞船的n多种属性
        self.rect = self.image.get_rect()
        #获取窗口的n多种属性
        self.screen_rect = screen.get_rect()
        # 将窗口的中间、底部坐标属性复制给飞船
        self.rect.centerx = self.screen_rect.centerx  #中间
        self.rect.bottom = self.screen_rect.bottom   #底部

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)