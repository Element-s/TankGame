# -*- coding:utf-8 -*-
'''
Created on 2013-5-13

@author: Elem
'''
import cocos

import util

class PhysicalObject(cocos.sprite.Sprite):
    ''' '''
    MOVE_SPEED = 200
    
    def __init__(self, *args, **kwargs):
        super(self, PhysicalObject).__init__(*args, **kwargs)
        
        self.event_handlers = []
    
    # 判断与另外一个对象是否发生碰撞        
    def collides_with(self, other_object):
        if not self.reacts_to_bullets and other_object.is_bullet:
            return False
        if self.is_bullet and not other_object.reacts_to_bullets:
            return False
            
        collision_distance = self.image.width*0.5*self.scale \
                                + other_object.image.width*0.5*other_object.scale
        actual_distance = util.distance(self.position, other_object.position)
        
        return (actual_distance <= collision_distance)
    
    # Sprite发生碰撞则消失
    def handle_collision_with(self, other_object):
        if self.__class__ == other_object.__class__:
            self.dead = False
        else:
            self.dead = True
        