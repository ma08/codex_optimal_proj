

def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return "".join(s)

def is_valid(s, target):
    i = 0
    while i < len(s):
        if s[i] == target[i]:
            i += 1
        else:
            j = i + 1
            while j < len(s) and s[j] != target[i]:
                j += 1
            if j == len(s):
                return False
            else:
                s = swap(s, i, j)
                i += 1
    return True

def can_swap(s, target):
    i = 0
    while i < len(s):
        if s[i] != target[i]:
            j = i + 1
            while j < len(s) and s[j] != target[i]:
                j += 1
            if j == len(s):
                return False
    return True

def get_swap(s, target):
    swaps = []
    i = 0
    while i < len(s):
        if s[i] != target[i]:
            j = i + 1
            while j < len(s) and s[j] != target[i]:
                j += 1
            if j == len(s):
                return False
            swaps.append(j)
            s = swap(s, i, j)
        i += 1
    return swaps

def main():
    n = int(input())
    s = input()
    target = input()
    if can_swap(s, target):
        swaps = get_swap(s, target)
        print(len(swaps))
        print(" ".join(map(str, swaps)))
    else:
        print(-1)

if __name__ == "__main__":
    main()
