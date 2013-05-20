# -*- coding:utf-8 -*-
'''
Created on 2013-5-16

@author: Elem
'''
from cocos import actions

import resources
import util

class Bullet(actions.Action):
    '''
    子弹类
    '''
    MOVE_SPEED = 200
    
    def __init__(self, *args, **kwargs):
        
        super(Bullet, self).__init__(resources.bullet_image, *args, **kwargs)
        
#        # 子弹不是一直存在的，0.5秒后消失
#        pyglet.clock.schedule_once(self.die, 0.5)
        self.is_bullet = True
        
    # 子弹不在窗口中则消失
    def out_bounds(self):
        if not self.dead:
            min_x = -self.image.width/2 
            min_y = -self.image.height/2
            max_x = 800 + self.image.width/2
            max_y = 640 + self.image.height/2 
            if self.x < min_x or self.x > max_x:
                return True
            if self.y < min_y or self.y > max_y:
                return True
            return False
        else:
            return True
        
    def die(self, dt):
        if self.out_bounds():
            self.dead = True
        else:
            self.dead = False
            
    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt        
        self.die(dt)
        

        
    
    
    