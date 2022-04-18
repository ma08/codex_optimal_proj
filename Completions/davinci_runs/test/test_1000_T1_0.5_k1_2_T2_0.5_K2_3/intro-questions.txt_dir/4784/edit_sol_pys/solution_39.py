# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# Name:         file
# Purpose:      file
#
# Author:       Ivo
#
# Created:      03.02.2016
# Copyright:    (c) Ivo 2016
# Licence:      <your licence>
# ----------------------------------------------------------------------------


X = int(input())
N = int(input())

total = X
for i in range(N):
    total -= int(input())

print(total)
