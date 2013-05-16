# -*- coding:utf-8 -*-
'''
Created on 2013-5-13

@author: Elem
'''
import cocos

class PhysicalObject(cocos.sprite.Sprite):
    ''' '''
    def __init__(self, *args, **kwargs):
        super(self, PhysicalObject).__init__(*args, **kwargs)