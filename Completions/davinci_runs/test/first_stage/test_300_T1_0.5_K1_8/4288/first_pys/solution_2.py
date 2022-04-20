

def is_poor_triple(a, b, c):
    if a == b == c:
        return False
    elif a == b or a == c or b == c:
        return True
    else:
        return False

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    if is_poor_triple(a, b, c):
        print('Yes')
    else:
        print('No')