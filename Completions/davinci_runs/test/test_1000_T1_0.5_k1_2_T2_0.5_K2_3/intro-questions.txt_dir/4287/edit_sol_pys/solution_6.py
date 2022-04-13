
def solution(n):
    if n < 0:
        return False
    return len(str(n)) == len(set(str(n)))
#-----Solution-----#

print(solution(1213))
#-----Test-----#
