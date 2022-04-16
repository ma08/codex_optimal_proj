#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Coosh

a1, a2, a3 = map(int, input().split())
if a1+a2+a3 >= 22:
    print('bust')
else:
    print('win')
