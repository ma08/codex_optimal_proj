
def solution(s):
    if len(s) % 2 == 0:
        return s[(len(s) // 2 - 1):(len(s) // 2 + 1)]
    else:
        return s[len(s) // 2]
#-----Solution-----#

s = 'abcde'
print(solution(s))
#-----Test-----#
