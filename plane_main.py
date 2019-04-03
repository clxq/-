import pygame
from pygame模块.plane_sprites import *

class GamePlane():
    def __init__(self):
        print("游戏初始化")
        # 创建主窗口
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        #创建游戏时钟
        self.clock=pygame.time.Clock()
        #调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        #设置定时器事件-创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1 = Background('images/background.png')
        bg2 = Background("images/background.png")
        bg2.rect.y = -bg2.rect.height
        self.back_ground = pygame.sprite.Group(bg1, bg2)
        #敌机精灵组
        self.enemy_ground=pygame.sprite.Group()
        #创建英雄的精灵和精灵组
        self.hero=Hero()
        self.hero_group=pygame.sprite.Group(self.hero)



    def start_game(self):
        while True:
            #设置刷新帧率
            self.clock.tick(60)
            #事件监听
            self.__event_handler()
            #碰撞检测
            self.__check_collide()
            #更新/绘制精灵组
            self.__update_sprites()
            #更新显示
            pygame.display.update()

            #使用键盘提供的方法获取键盘按键 —按键元组
            keys_pressed=pygame.key.get_pressed()
            #判断元组中对应的按键索引值
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed=2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed=-2
            else:
                self.hero.speed=0

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.__game_over()
            elif event.type==CREATE_ENEMY_EVENT:
                #创建敌机精灵
                enemy=Enemy()

                #将敌机精灵添加到敌机精灵组
                self.enemy_ground.add(enemy)
            elif event.type==HERO_FIRE_EVENT:
                self.hero.fire()

    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_ground,True,True)
        #敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_ground,True)
        #判断列表时候有内容
        if len(enemies)>0:
            #让英雄牺牲
            self.hero.kill()
            #结束游戏
            GamePlane.__game_over(self)

    def __update_sprites(self):
        self.back_ground.update()
        self.back_ground.draw(self.screen)
        self.enemy_ground.update()
        self.enemy_ground.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()

if __name__=='__main__':
    gp=GamePlane()
    gp.start_game()