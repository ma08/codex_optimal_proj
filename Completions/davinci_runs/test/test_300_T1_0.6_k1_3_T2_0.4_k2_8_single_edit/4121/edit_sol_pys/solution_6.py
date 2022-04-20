#!/usr/bin/env python

import os

print(os.listdir('./'))

file = open('test.txt', 'w')
file.write('Hello World')
file.close()

file = open('test.txt', 'r')
print(file.read())
file.close()

file = open('test.txt', 'a')
file.write('\nHello again')
file.close()

file = open('test.txt', 'r')
print(file.read())
file.close()

file = open('test.txt', 'r')
print(file.readlines())
file.close()

with open('test.txt', 'r') as file:
    print(file.read())
