#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:35:19 2018

@author: jlopes

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3,
4. Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5,
6.

Peter and Colin roll their dice and compare totals: the highest total wins. The
result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer
rounded to seven decimal places in the form 0.abcdefg
"""

from itertools import product


def peter_wins(peter, colin):
    return peter > colin


def peter_wins_probability():
    peter_rolls = product(range(1, 5), repeat=9)
    colin_rolls = product(range(1, 7), repeat=6)
    peter_wins_count = 0
    for peter_roll in peter_rolls:
        for colin_roll in colin_rolls:
            if peter_wins(sum(peter_roll), sum(colin_roll)):
                peter_wins_count += 1
    return peter_wins_count / len(list(peter_rolls)) / len(list(colin_rolls))


if __name__ == "__main__":
    print(peter_wins_probability())
