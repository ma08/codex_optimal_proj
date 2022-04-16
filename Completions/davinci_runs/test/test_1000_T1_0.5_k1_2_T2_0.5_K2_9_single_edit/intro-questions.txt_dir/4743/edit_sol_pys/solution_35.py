
import sys
import math

def nimionese(word):
    if word[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
        word = 'h' + word
    if word[0] in ['h']:
        word = 'g' + word[1:]
    if word[0] in ['l']:
        word = 'd' + word[1:]
    if word[0] in ['m']:
        word = 'n' + word[1:]
    if word[0] in ['f']:
        word = 'b' + word[1:]
    if word[0] in ['v']:
        word = 'c' + word[1:]
    if word[0] in ['s']:
        word = 'z' + word[1:]
    if word[0] in ['r']:
        word = 'd' + word[1:]
    if word[0] in ['j']:
        word = 'g' + word[1:]
    if word[0] in ['x']:
        word = 'k' + word[1:]
    if word[0] in ['q']:
        word = 'k' + word[1:]
    if word[0] in ['w']:
        word = 'p' + word[1:]
    if word[0] in ['z']:
        word = 't' + word[1:]
    word = word.replace('each', 'dach')
    word = word.replace('ch', word[0])
    word = word.replace('sh', word[0])
    word = word.replace('th', word[0])
    word = word.replace('ph', word[0])
    word = word.replace('wh', word[0])
    word = word.replace('gh', word[0])
    word = word.replace('dh', word[0])
    word = word.replace('bh', word[0])
    word = word.replace('kh', word[0])
    word = word.replace('zh', word[0])
    word = word.replace('ng', word[0])
    word = word.replace('nk', word[0])
    word = word.replace('nt', word[0])
    word = word.replace('nd', word[0])
    word = word.replace('mp', word[0])
    word = word.replace('mb', word[0])
    word = word.replace('nd', word[0])
    word = word.replace('pt', word[0])
    word = word.replace('pd', word[0])
    word = word.replace('bt', word[0])
    word = word.replace('bd', word[0])
    word = word.replace('kt', word[0])
    word = word.replace('kd', word[0])
    word = word.replace('zt', word[0])
    word = word.replace('zd', word[0])
    word = word.replace('dt', word[0])
    word = word.replace('dd', word[0])
    word = word.replace('gt', word[0])
    word = word.replace('gd', word[0])
    word = word.replace('ct', word[0])
    word = word.replace('cd', word[0])
    word = word.replace('st', word[0])
    word = word.replace('sd', word[0])
    word = word.replace('zd', word[0])
    word = word.replace('zt', word[0])
    word = word.replace('ps', word[0])
    word = word.replace('bs', word[0])
    word = word.replace('ks', word[0])
    word = word.replace('ds', word[0])
    word = word.replace('gs', word[0])
    word = word.replace('cs', word[0])
    word = word.replace('ts', word[0])
    word = word.replace('ns', word[0])
    word = word.replace('zs', word[0])
    if word[-1] in ['a', 'e', 'i', 'o', 'u', 'y']:
        word += 'h'
    if word[-1] in ['h']:
        word = word[:-1] + 'o'
    if word[-1] in ['l']:
        word = word[:-1] + 'ah'
    if word[-1] in ['m']:
        word = word[:-1] + 'oh'
    if word[-1] in ['f']:
        word = word[:-1] + 'uh'
    if word[-1] in ['v']:
        word = word[:-1] + 'uh'
    if word[-1] in ['s']:
        word = word[:-1] + 'uh'
    if word[-1] in ['r']:
        word = word[:-1] + 'ah'
    if word[-1] in ['j']:
        word = word[:-1] + 'oh'
    if word[-1] in ['x']:
        word = word[:-1] + 'uh'
    if word[-1] in ['q']:
        word = word[:-1] + 'uh'
    if word[-1] in ['w']:
        word = word[:-1] + 'uh'
    if word[-1] in ['z']:
        word = word[:-1] + 'uh'
    return word

def main():
    sentence = sys.stdin.readline()
    words = sentence.split()
    for word in words:
        print(nimionese(word), end = " ")

if __name__ == "__main__":
    main()
