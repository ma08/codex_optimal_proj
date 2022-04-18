#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set et sw=4 sts=4 fdm=indent fdl=0 fdn=3 ft=python:
#
# Author: Riku Halonen
# Created: <2016-11-09 Wed>
#
# Description:
#
#
#

#-----main-----
n = int(input())
if n==1:
    print("Hello World!")
elif n==2:
    a,b=map(int,input().split())
    print(a+b)
