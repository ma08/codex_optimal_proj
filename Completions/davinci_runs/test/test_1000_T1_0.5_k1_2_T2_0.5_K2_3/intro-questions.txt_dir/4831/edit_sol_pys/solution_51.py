

import sys
import math

def frame(ch):
    if ch == ' ': return '     '
    if ch.isalpha():
        if ch.isupper():
            ch = ch.lower()
        if ch == 'a': return '..#..'
        if ch == 'b': return '.#.#.'
        if ch == 'c': return '#..#.'
        if ch == 'd': return '#.#..'
        if ch == 'e': return '#...#'
        if ch == 'f': return '#..#.'
        if ch == 'g': return '##.##'
        if ch == 'h': return '#.##.'
        if ch == 'i': return '.#..#'
        if ch == 'j': return '.##.#'
        if ch == 'k': return '#.#.#'
        if ch == 'l': return '.###.'
        if ch == 'm': return '##..#'
        if ch == 'n': return '##.#.'
        if ch == 'o': return '###..'
        if ch == 'p': return '##...'
        if ch == 'q': return '##.#.'
        if ch == 'r': return '##..#'
        if ch == 's': return '#.#.#'
        if ch == 't': return '##...#'
        if ch == 'u': return '#.####'
        if ch == 'v': return '#.####'
        if ch == 'w': return '.#.##.'
        if ch == 'x': return '#.##.#'
        if ch == 'y': return '#.###.'
        if ch == 'z': return '###.#.'
        if ch == '.': return '..*..'
        if ch == ',': return '.*.*.'
        if ch == '!': return '*.!.*'
        if ch == '?': return '*?.!*'
        if ch == '-': return '*-.-*'
        if ch == '\'': return '*.*..'
        if ch == '"': return '*.*.*.'
        if ch == ':': return '*.::*'
        if ch == ';': return '*.:.*'
        if ch == '=': return '*=.=*'
        if ch == '+': return '*=.=*'
        if ch == '*': return '*.**.'
        if ch == '/': return '*/./*'
        if ch == '\\': return '*\\.*/'
        if ch == '@': return '*@.@*'
        if ch == '#': return '*#.#*'
        if ch == '$': return '*.$$.'
        if ch == '%': return '*%.%*'
        if ch == '^': return '*^.^*'
        if ch == '&': return '*.&&.'
        if ch == '(': return '*(.(*'
        if ch == ')': return '*)).*'
        if ch == '[': return '*[.[*'
        if ch == ']': return '*].]*'
        if ch == '{': return '*{.{*'
        if ch == '}': return '*}.}*'
        if ch == '<': return '*<.<*'
        if ch == '>': return '*>.>*'
        if ch == '_': return '*.__.'
        if ch == '~': return '*~.~*'
        if ch == '`': return '*.``.'
        if ch == '|': return '*.|.*'
        if ch == '0': return '###...#'
        if ch == '1': return '..##..#'
        if ch == '2': return '..#..##'
        if ch == '3': return '..###..'
        if ch == '4': return '.#.##..'
        if ch == '5': return '.#..##.'
        if ch == '6': return '.#...##'
        if ch == '7': return '##..#..'
        if ch == '8': return '##.#...'
        if ch == '9': return '##...#.'

def main():
    line = sys.stdin.readline()
    line = line.replace('\n','')
    line = line.replace('\r','')
    line = line.replace('\t','')
    line = line.replace(' ','')
    for i in range(5):
        for ch in line:
            sys.stdout.write(frame(ch)[i])
        sys.stdout.write('\n')

main()
