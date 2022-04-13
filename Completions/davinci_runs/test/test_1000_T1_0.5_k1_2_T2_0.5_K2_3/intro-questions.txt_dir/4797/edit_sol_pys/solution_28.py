#!/usr/bin/env python
# -*- coding: utf-8 -*-


input_string = input()
output_string = ""

for i in range(len(input_string)):
    if input_string[i] == "<":
        output_string = output_string[:-1]
    else:
        output_string += input_string[i]

print(output_string)
