#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# file
#
# Copyright (c) 2020 Kazuhiro KOBAYASHI <root.4mac@gmail.com>
#
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
#
# @version    1.0
# @date       2020-07-11
# @author     kzmr
#


#-----import-----



#-----main-----

a, b = map(int, input().split())

if a <= b:
    print(0)
else:
    print(a - b)
