

import sys
#import math
#import collections

"""
---TODO---
- make a preprocessor that reads the string and builds a list of commands
- make a dict that stores the variables
- make a greedy function that feeds the golorp
- make a function that checks if the golorp can be fed
- make a function that finds the lexicographically smallest sequence of values
"""


class Golorp():
    def __init__(self, name):
        self.name = name
        self.jaws = []
        self.stomach = []
        self.preprocess()
        self.variables = {
            'a': None,
            'b': None,
            'c': None,
            'd': None,
            'e': None,
            'f': None,
            'g': None,
            'h': None,
            'i': None,
            'j': None,
            'k': None,
            'l': None,
            'm': None,
            'n': None,
            'o': None,
            'p': None,
            'q': None,
            'r': None,
            's': None,
            't': None,
            'u': None,
            'v': None,
            'w': None,
            'x': None,
            'y': None,
            'z': None
        }

    def preprocess(self):
        self.jaws = self.name[:self.name.find(':')].split('>')[0].split('(')[1].split(')')[0].split('/')
        self.stomach = self.name[self.name.find(':') + 1:].split(',')

    def feed(self, sequence):
        for c in sequence:
            for jaw in self.jaws:
                for i in range(len(jaw.split('+'))):
                    if jaw.split('+')[i] == '_':
                        jaw.split('+')[i] = c
                        break
        for jaw in self.jaws:
            if '_' in jaw.split('+'):
                return False
        for jaw in self.jaws:
            for i in range(len(jaw.split('+'))):
                if jaw.split('+')[i] == '+':
                    jaw.split('+')[i - 1] += jaw.split('+')[i + 1]
                    jaw.split('+')[i + 1] = None
                elif jaw.split('+')[i] == '-':
                    jaw.split('+')[i - 1] -= jaw.split('+')[i + 1]
                    jaw.split('+')[i + 1] = None
                elif jaw.split('+')[i] == '*':
                    jaw.split('+')[i - 1] *= jaw.split('+')[i + 1]
                    jaw.split('+')[i + 1] = None
            while None in jaw.split('+'):
                jaw.split('+').remove(None)
            self.variables[jaw.split('+')[0]] = jaw.split('+')[1]

        for stomach in self.stomach:
            for char in stomach:
                if self.variables[char] is None:
                    return False

            if stomach[0] == '<':
                if self.variables[stomach[1]] >= self.variables[stomach[2]]:
                    return False
            elif stomach[0] == '>':
                if self.variables[stomach[1]] <= self.variables[stomach[2]]:
                    return False
            else:
                if self.variables[stomach[0]] != self.variables[stomach[1]]:
                    return False

        return True

    def find_solution(self):

        def generate_sequences(l, n):
            if l == 0:
                return [[]]
            else:
                return [[x] + y for x in range(n) for y in generate_sequences(l - 1, n)]
        for sequence in generate_sequences(len(self.jaws), 10):
            if self.feed(sequence):
                return sequence

        return False



if __name__ == "__main__":
    golorp = Golorp(sys.stdin.readline()[:-1])
    print(golorp.find_solution())
