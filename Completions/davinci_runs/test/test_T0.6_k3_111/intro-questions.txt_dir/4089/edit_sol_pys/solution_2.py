# === Solution 1 ===

def convert(num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    base = len(alphabet)
    if num <= 0:
        return ''
    elif num <= base:
        return alphabet[num-1]
    else:
        return convert(num//base) + alphabet[(num%base)-1]
num = int(input())
print(convert(num))
