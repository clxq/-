import pygame
from pygame模块.plane_sprites import GameSprite

pygame.init()
print('游戏程序代码')
#初始化游戏显示窗口
pygame.display.set_mode()
#窗口大小
screen=pygame.display.set_mode((480,700))
#加载图像数据
bg=pygame.image.load('images/background.png')
#图像指定位置
screen.blit(bg,(0,0))
#更新屏幕显示
pygame.display.update()

#加载英雄
hero=pygame.image.load('images/me1.png')
screen.blit(hero,(200,500))
pygame.display.update()
#pygame提供的时钟对象
clock=pygame.time.Clock()
#定义游戏初始位置
hero_rect=pygame.Rect(200,500,102,126)

#创建精灵和精灵组
enemy1=GameSprite('images/enemy1.png')
enemy2=GameSprite('images/enemy1.png',2)
enemy3=GameSprite('images/enemy1.png',4)
enemy4=GameSprite('images/enemy1.png',5)
enemy_group=pygame.sprite.Group(enemy1,enemy2,enemy3,enemy4)

while True:
    #修改帧率
    clock.tick(60)

    #监听事件
    # eventlist=pygame.event.get()
    # print(eventlist)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #卸载所有pygame模块
            pygame.quit()
            #退出系统
            exit()



    #修改飞机的位置（y轴）
    hero_rect.y -=1
    #飞机飞出屏幕时，从底部出来
    if hero_rect.y<0:
        hero_rect.y=700
    #调用blit()方法重新绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero, hero_rect)
    #update更新图像
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
pygame.quit()