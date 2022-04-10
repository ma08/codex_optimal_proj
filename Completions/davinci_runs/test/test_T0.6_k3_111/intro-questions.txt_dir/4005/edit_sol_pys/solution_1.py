# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:39:32 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,"我愛","Minecraft","也愛","Python")
