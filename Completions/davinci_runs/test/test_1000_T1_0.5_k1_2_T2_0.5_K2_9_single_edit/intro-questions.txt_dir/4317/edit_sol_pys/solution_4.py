#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a, b = map(int, input().split())

print(max(a + b, a - b, a * b))
