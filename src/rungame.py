# -*- coding:utf-8 -*-
'''
Created on 2013-5-13

@author: Elem
'''
import pyglet 
from pyglet.window import key

tank_image = pyglet.resource.path = ['../resource']
pyglet.resource.reindex()

tank_image = pyglet.resource.image('up.png')

import cocos
from cocos import tiles, actions, layer
from cocos.director import director

import resources

class DriveTank(actions.Driver):
    
    def step(self, dt):
        self.target.rotation += (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 150 * dt   
        self.target.acceleration = (keyboard[key.UP] - keyboard[key.DOWN]) * 400 * dt
        if keyboard[key.SPACE]: self.target.speed = 0
        super(DriveTank, self).step(dt)
        scroller.set_focus(self.target.x, self.target.y)
        
class TankController(actions.Action, tiles.RectMapCollider):
    
    MOVE_SPEED = 200
    GRAVITY = -1500
    
    def start(self):
        self.target.velocity = (0, 0)
        
    def step(self, dt):
        global  keyboard, scroller, game_map
        # 初始化速度
        dx, dy = self.target.velocity
        
        # 更新坦克速度
        dx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * self.MOVE_SPEED * dt
        dy = (keyboard[key.UP] - keyboard[key.DOWN]) * self.MOVE_SPEED * dt
        if keyboard[key.SPACE]: self.target.speed = 0
        
        # 获得坦克矩形边界
        last = self.target.get_rect()
        new = last.copy()
        new.x += dx
        new.y += dy
        
        # 运行碰撞机
        dx, dy = self.target.velocity = self.collide_map(game_map, last, new, dy, dx)
        
        # 坦克的位置被固定在图形矩形的中心
        self.target.position = new.center
        
        scroller.set_focus(*new.center)
        

def main():
    global keyboard, scroller, game_map
    # 初始化创建窗口
    director.init(width=800, height=640, do_not_scale=True, resizable=True)
    
    # 创建坦克图层
    tank_layer = layer.ScrollableLayer()
    
    # 创建坦克对象
    tank = cocos.sprite.Sprite(image=resources.tank_image, position = (340, 80))
    
    # 把坦克对象添加到坦克图层中
    tank_layer.add(tank)
    
    # 设置坦克的最大前进和后退速度
    tank.max_forward_speed = 200
    tank.max_reverse_speed = -100
    
    # 坦克对象执行一个action
    tank.do(TankController())
    
    # 创建滚动图层管理器，添加游戏背景图层和坦克图层到图层管理器
    scroller = layer.ScrollingManager()
    tank_map = tiles.load('test_tank.tmx')
    print type(tank_map)
    game_map = tank_map['backgroud']
    print type(game_map)
    
#    print tank_map.get_resource('tank_object')
#    tank_flag = tank_map['tank_object']
#    scroller.add(tank_flag, z=0)
    
#    print type(game_map),len(game_map.cells)
#    print len(game_map.cells[0])
#    for col in game_map.cells:
#        print col
    scroller.add(game_map, z=0)
    scroller.add(tank_layer, z=1)
    
    # set the player start using the player_start token from the tilemap
    print len(game_map.cells)
    start = game_map.cells[21]
    print len(start)
    start = start[4]
#    r = tank.get_rect()

    # align the mid bottom of the player with the mid bottom of the start cell
#    r.midbottom = start.midbottom

    # player image anchor (position) is in the center of the sprite
#    tank.position = r.center    
    
    # 创建游戏主场景scene
    main_scene = cocos.scene.Scene()
    main_scene.add(scroller)
    
    # 
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)
    
    def on_key_press(key, modifier):
        if key == pyglet.window.key.Z:
            if scroller.scale == 0.75:
                scroller.do(actions.ScaleTo(1, 2))
            else:
                scroller.do(actions.ScaleTo(0.75, 2))
        elif key == pyglet.window.key.D:
            game_map.set_debug(True)
            
    director.window.push_handlers(on_key_press)

    director.run(main_scene)    
        
if __name__ == '__main__':
    main()      
        
        
    